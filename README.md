# Text UI Converter

## Introduction

Text UI Converter is converter from text-based UI design files to HTML files.

## Files

1. tui.py: The main script file.
1. default.css: Default style file.

## UI Items

1. [[Sample]]: Button. `<input type="button" value="Sample"/>`
1. `[ ]` or [Sample]: Input Box. `<input type="text" value="Sample"/>`
1. { }: Check Box. `<input type="checkbox"/>`
1. {V}: Checked Check Box. `<input type="checkbox" checked/>`
1. ( ): Radio Button. `<input type="radio"/>`
1. (V): Checked Radio Button. `<input type="radio" checked/>`
1. @ @V or @Sample@V: Drop-down List. `<select><option>Sample</option></select>`
1. !Sample!: Table Header Cell. `<th>Sample</th>`
1. |Sample|: Table Cell. `<td>Sample</td>`
1. End with two spaces: Line break. `<br/>`
1. Blank line: Paragraph break. `<p/>`

## Run

### Convert

`tui.py FILE.txt`

This makes a converted FILE.html.

### Help

`tui.py -h`

## Documentation

1. [Project Overview](docs/010_project_overview.md)
1. [Requirements](docs/030_requirements.md)
1. [Design](docs/120_design.md)

## Source Code

1. Main: [tui.py](src/tui.py)
1. Default CSS: [default.css](src/default.css)
