#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2020 Jung Bong-Hwa
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
* End with two spaces: Line break. '<br/>'
* Blank line: Paragraph break. '<p/>'
"""

# Defines arguments.
parser = argparse.ArgumentParser(description='Text UI Converter\n' + help, 
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-f", "--file", help="Output HTML file name.")
parser.add_argument("-c", "--css", help="Use the css file.")
parser.add_argument("-p", "--print_output", action='store_true', help="Print output without file")
parser.add_argument('text_files', nargs='+', help="Text files")

def convert(text):
    if text == '':
        return '<p/>'
    text = re.sub(r'  $', r'<br/>', text)
    text = text.strip()

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

def convert_text(text_file):
    html = ''
    f = open(text_file, 'r', encoding='utf-8', errors='ignore')
    while True:
        line = f.readline()
        if not line: break
        html += convert(line) + '\n'
    f.close()

    return html

def convert_text_to_html_file(text_file):
    html = convert_text(text_file)

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


if args.file:
    html = convert_text_to_html_file(args.text_files[0])
    write_file(args.file, html)
elif args.print_output:
    html = convert_text(args.text_files[0])
    print(html)
else:
    for text_file in args.text_files:
        html = convert_text_to_html_file(text_file)
        filename, file_extension = path.splitext(text_file)
        write_file(filename + ".html", html)
