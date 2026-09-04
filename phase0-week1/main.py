import sys

def main():
    if len(sys.argv) == 1:
        print('please provide the greeting param')
    elif len(sys.argv) == 2 and sys.argv[1].lower() == 'greeting':
        print('='*10)
        print('hello world')
        print('='*10)
    else:
        print('wrong params.')

if __name__ == '__main__':
    main()