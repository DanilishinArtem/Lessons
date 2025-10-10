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