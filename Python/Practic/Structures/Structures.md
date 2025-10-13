# Structures
### CSV format
Example of writing in and reading out of the csv file.
```python
import csv

if __name__ == "__main__":
    text = [
        ['1','2'],
        ['3','4'],
        ['5','6'],
        ['7','8'],
        ['9','10']
    ]
    # part of writing to the file
    with open('text.csv', 'wt') as fout: # manager of the context
        csvout = csv.writer(fout)
        csvout.writerows(text)
    # part of reading from the file
    with open('text.csv', 'rt') as fin:
        csvin = csv.reader(fin)
        output = [row for row in csvin]
```
Example of using with headers
```python
import csv

if __name__ == "__main__":
    villains = [
        {'first': 'Doctor', 'last': 'No'},
        {'first': 'Rosa', 'last': 'Klebb'},
        {'first': 'Mister', 'last': 'Big'},
        {'first': 'Auric', 'last': 'Goldfinger'},
        {'first': 'Ernst', 'last': 'Blofeld'},
    ]
    # part of writing
    with open('villains.csv', 'wt') as fout:
        cout = csv.DictWriter(fout, ['first', 'last'])
        cout.writeheader()
        cout.writerows(villains)
    # part of reading
    with open('villains.csv', 'rt') as fin:
        cin = csv.DictReader(fin)
        output = [row for row in cin]
    print(f'[INFO] Result of reading: {output}')
```
### XML format
```python
import xml.etree.ElementTree as et

if __name__ == "__main__":
    tree = et.ElementTree(file='./additional_files/example.xml')
    root = tree.getroot()
    print(f'[ROOT] Tag: {root.tag}')
    for child in root:
        print(f'[CHILD] tag: {child.tag}, attributes: {child.attrib}')
        for grandchild in child:
            print(f'[GRANDCHILD] tag: {grandchild.tag}, attributes: {grandchild.attrib}')
```
### JSON format
```python
import json

if __name__ == "__main__":
    with open('./additional_files/example.json', 'rt') as jf:
        example = json.load(jf)
    print(example['breakfast'])
    
```
### Configurations files
```python
import configparser

if __name__ == "__main__":
    cfg = configparser.ConfigParser()
    cfg.read('./additional_files/example.cfg')
    print(f'[INFO] cfg: {cfg}')
    print(f'[INFO] cfg french: {cfg['french']}')
    print(f'[INFO] cfg french: {cfg['french']['greeting']}')
# output:
# [INFO] cfg: <configparser.ConfigParser object at 0x7f831ac1b890>
# [INFO] cfg french: <Section: french>
# [INFO] cfg french: Bonjour
```