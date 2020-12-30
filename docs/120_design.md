# Design

## UI Items

1. [[Sample]]: Button. `<input type="button" value="Sample"/>`
1. [ ] or [Sample]: Input Box. `<input type="text" value="Sample"/>`
1. { }: Check Box. `<input type="checkbox"/>
1. {V}: Checked Check Box. `<input type="checkbox" checked/>
1. ( ): Radio Button. `<input type="radio"/>
1. (V): Checked Radio Button. `<input type="radio" checked/>
1. @ @V or @Sample@V: Drop-down List. `<select><option>Sample</option></select>`
1. !Sample!: Table Header Cell. `<th>Sample</th>`
1. |Sample|: Table Cell. `<td>Sample</td>`

## Table

1. Users must surround contents by `<table>` and `</table>` tags.
1. If a user wants to change background color of titles, uses just a CSS.

## Converter

1. Any HTML tags aren't converted.
1. Any texts are not changed except the UI items.
1. If a user doesn’t specify a CSS file, use the default.css file.
