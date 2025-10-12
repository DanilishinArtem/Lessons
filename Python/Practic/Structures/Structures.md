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