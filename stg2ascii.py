import sys

if len(sys.argv) < 3:
    print('Usage: python ' + sys.argv[0] + ' [MODE] [DATA]')
    print('     : This script will convert various base number to ASCII letter.')
    print('Mode : bin2ascii , hex2ascii , oct2ascii')
    print('Designed for picoCTF 2018 "what base us this?" challenge.')
    exit(1)

if sys.argv[1] == 'bin2ascii':
    res = ''
    for arg in sys.argv[2:]:
        target = int(arg, 2)
        res = res + chr(target)
    print(res)
elif sys.argv[1] == 'hex2ascii':
    res = ''
    tlist = [(i + j) for (i, j) in zip(sys.argv[2][::2], sys.argv[2][1::2])]
    for letter in tlist:
        res = res + chr(int(letter, 16))
    print(res)
elif sys.argv[1] == 'oct2ascii':
    res = ''
    for arg in sys.argv[2:]:
        target = int(arg, 8)
        res = res + chr(target)
    print(res)
else:
    print('Error: Mode not found')
    exit(0)
