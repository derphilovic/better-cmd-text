# bettercmd

Better CMD Text utilities for Python.

## Installation

```bash
pip install bettercmd
```
## Usage
How to use bettercmd:
```python
#import the module
import bettercmd as bcm
#run the function with the wanted .pdat file
bcm.beautify('test.pdat')
```
### PDAT file syntax
```bash
#every line starts with { and ends with }.
{header : Hello Guys!}.
#the first word is the type of word/line,
#the : is the seperation and everything after that is the output
{empty : 1}.
#is an empty line if the number is 1 it is one empty line
#if the number is 2 it is 2 empty lines and so on
{color : 161 ; this text is red}.
#makes a colored line with the specified 8bit color
{textblock : hallo welt}.
#its just a simple line of text
