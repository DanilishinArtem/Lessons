# Files and Folders
Example of creation and writing in the file
```python
if __name__ == "__main__":
    fout = open('ooops.txt', 'wt')
    print('Ooops, I crated a file.', file=fout)
    fout.close()
```
```python
if __name__ == "__main__":
    # Writing in the file
    poem =  '''There was a young lady named Bright, WHose speed was far faster than light;
                She started on day in a realative way,
                And returned on the previous night.
            '''
    fout = open('relativity.txt', 'wt')
    fout.write(poem)
    print(f'[INFO] Write {len(poem)} symbols from file relativity')
    fout.close()
    # Reading from the file
    fin = open('relativity.txt', 'rt')
    poem = fin.read()
    print(f'[INFO] Read {len(poem)} symbols from file relativity')
    fin.close()
```
Reading line by line
```python
if __name__ == "__main__":
    # Writing in the file
    poem =  '''There was a young lady named Bright, WHose speed was far faster than light;
                She started on day in a realative way,
                And returned on the previous night.
            '''
    fout = open('relativity.txt', 'wt')
    fout.write(poem)
    print(f'[INFO] Write {len(poem)} symbols from file relativity')
    fout.close()
    # Reading from the file
    fin = open('relativity.txt', 'rt')
    counter = 0
    while True:
        line = fin.readline()
        if not line:
            break
        poem += line
        counter += 1
        print(f'[INFO] Read line {counter}')
    fin.close()
```
Reading by using iterator
```python
if __name__ == "__main__":
    # Writing in the file
    poem =  '''There was a young lady named Bright, WHose speed was far faster than light;
                She started on day in a realative way,
                And returned on the previous night.
            '''
    fout = open('relativity.txt', 'wt')
    fout.write(poem)
    print(f'[INFO] Write {len(poem)} symbols from file relativity')
    fout.close()
    # Reading from the file by using iterator
    fin = open('relativity.txt', 'rt')
    for index, line in enumerate(fin):
        poem += line
        print(f'[INFO] Read line {index}')
    fin.close()
```
Using WITH
```python

if __name__ == "__main__":
    # Writing in the file
    poem =  '''There was a young lady named Bright, WHose speed was far faster than light;
                She started on day in a realative way,
                And returned on the previous night.
            '''
    # Using with
    with open('relativity.txt', 'wt') as fout:
        fout.write(poem)
```
## Seek and Tell functions
- Function tell() return current location 
- Function seek() let to shift current location
## File operations
File Existence
```python
import os

def check_file(name: str):
    if os.path.exists(name):
        print(f'[INFO] File {name} exits')
    else:
        print(f'[FINO] File {name} is not exits')

if __name__ == "__main__":
    # Writing in the file
    poem =  '''There was a young lady named Bright, WHose speed was far faster than light;
                She started on day in a realative way,
                And returned on the previous night.
            '''
    check_file('relativity.txt')
    print(f'[INFO] File relativity is exi')
    with open('relativity.txt', 'wt') as fout:
        fout.write(poem)
    check_file('relativity.txt')
```
<!-- 192 -->