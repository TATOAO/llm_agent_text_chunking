from typing import Generator

def get_more_text() -> Generator['str', None, None]:

    f = open('./raw_spans.txt', 'r')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)//10 + 1):
        yield '\n'.join(lines[i:i+10])

#
def load_more_raw_text() -> str:
    """You are ready to parse more text"""
    return next(get_more_text())

def main():

    while 1:
        jj = load_more_raw_text()
        print(jj)

if __name__ == "__main__":
    main()

