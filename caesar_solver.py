import sys


def dec_caesar(encstr, key):
    res = ''
    for char in list(encstr):
        if char == ' ':
            res = res + ' '
            continue
        elif char == '_':
            res = res + '_'
            continue
        ascii_code = ord(char)
        tmp = ascii_code - 97
        tmp = (tmp - key) % 26
        ascii_code = tmp + 97
        res += chr(ascii_code)
    return res


def normal():
    while True:
        key = int(input('Please input some key >> '))
        res = dec_caesar(chal_str, key)
        print('Result >> ' + res)
        ans = input('Was the result correct? (Y/N) >> ')
        if ans == 'Y':
            break
        elif ans == 'N':
            print('Okay, please retry with different key.')
        else:
            print('Error!! Invalid value detected!!')
            exit(1)


def brute():
    keys = list(range(27))
    for key in keys:
        res = dec_caesar(chal_str, key)
        print('Result: ' + res + ' ,,, Key: ' + str(key))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python ' + sys.argv[0] + ' [CIPHERTEXT] [brute/normal]')
        exit(1)
    chal_str = sys.argv[1]
    if sys.argv[2] == 'brute':
            brute()
    elif sys.argv[2] == 'normal':
        normal()
    else:
        print('Error: Undefined parameter')
        exit(1)
