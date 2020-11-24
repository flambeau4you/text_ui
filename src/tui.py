#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import re
import codecs
from os import path

help = """
* [[Sample]]: Button. '<input type="button" value="Sample"/>'
* '[ ]' or [Sample]: Input Box. '<input type="text" value="Sample"/>'
* { }: Check Box. '<input type="checkbox"/>'
* {V}: Checked Check Box. '<input type="checkbox" checked/>'
* ( ): Radio Button. '<input type="radio"/>'
* (V): Checked Radio Button. '<input type="radio" checked/>'
* @ @V or @Sample@V: Drop-down List. '<select><option>Sample</option></select>'
* !Sample!: Table Header Cell. '<th>Sample</th>'
* |Sample|: Table Cell. '<td>Sample</td>'
"""

# Defines arguments.
parser = argparse.ArgumentParser(description='Text UI Converter\n' + help, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-o", "--output", help="Output HTML file name.")
parser.add_argument("-c", "--css", help="Use the css file.")
parser.add_argument('text_files', nargs='+', help="Text files")

def convert(text):
    if text == '':
        return '<p/>'

    text = re.sub(r'\[\[([^\]]+)\]\]', r'<input type="button" value="\1"/>', text)
    text = re.sub(r'\[ \]', r'<input type="textbox"/>', text)
    text = re.sub(r'\[([^\]]+)\]', r'<input type="textbox" value="\1"/>', text)
    text = re.sub(r'\{ \}', r'<input type="checkbox"/>', text)
    text = re.sub(r'\{V\}', r'<input type="checkbox" checked/>', text)
    text = re.sub(r'\( \)', r'<input type="radio"/>', text)
    text = re.sub(r'\(V\)', r'<input type="radio" checked/>', text)
    text = re.sub(r'@ @V', r'<select><option>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</option></select>', text)
    text = re.sub(r'@([^@]+)@V', r'<select><option>\1</option></select>', text)
    
    # Titles
    if text.startswith('!') and text.endswith('!'):
        text = re.sub(r'^!', r'<tr><th>', text)
        text = re.sub(r'!$', r'</th></tr>', text)
        text = re.sub(r'!', r'</th><th>', text)

    if text.startswith('|') and text.endswith('|'):
        text = re.sub(r'^\|', r'<tr><td>', text)
        text = re.sub(r'\|$', r'</td></tr>', text)
        text = re.sub(r'\|', r'</td><td>', text)
        
    return text

def convert_file(text_file):
    html = ''
    f = open(text_file)
    while True:
        line = f.readline()
        if not line: break
        html += convert(line.strip()) + '\n'
    f.close()

    if args.css: 
        html = '<link rel="stylesheet" href="' + args.css + '">\n' + html
    elif path.exists('default.css'):
        html = '<link rel="stylesheet" href="default.css">\n' + html

    html = '<html><body>\n' + html + '\n</body></html>\n'
    return html

def write_file(path, html):
    fo = codecs.open(path, encoding='utf-8', mode='w')
    fo.write(html)
    fo.close()


# Main
args = parser.parse_args()


if args.output:
    html = convert_file(args.text_file)
    write_file(args.output, html)
else:
    for text_file in args.text_files:
        html = convert_file(text_file)
        filename, file_extension = path.splitext(text_file)
        write_file(filename + ".html", html)
