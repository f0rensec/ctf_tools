import hashlib
import requests

target = ''
uri = ''

algorithm = 'MD5'
response = ''
md5_a1 = ''
md5_a2 = hashlib.md5(('GET:' + uri).encode('utf-8')).hexdigest()
cnonce = ''
nonce = ''
realm = ''
user = ''
qop = ''
nc = ''

if target == '':
    print('Usage: Write the parameters inside the script')
    exit(1)

print('[*] Requesting nonce parameter to server...')
res = requests.get(target)
nonce = res.headers['WWW-Authenticate'].split('"')[3]
print('[+] Nonce: ' + nonce)

print('[*] Generating the response to server...')
response = md5_a1 + ':' + nonce + ':' + nc + ':' + cnonce + ':' + qop + ':' + md5_a2
print('[+] Response has been generated!')
print('---> ' + response)
print('[*] Generating the header for authorization...')
auth_header = {'Authorization' : 'Digest username="' + user + '", realm="' + realm + '", nonce="' + nonce + '",uri="' + uri + '", algorithm=' + algorithm + ', response="' + hashlib.md5(response.encode('utf-8')).hexdigest() + '", qop=' + qop + ', nc=' + nc + ', cnonce="' + cnonce + '"'}
print('[+] Header has been generated!!')
print('---> ' + str(auth_header))

print('[*] Requesting the target page...')
res = requests.get(target, headers=auth_header)
print('[+] Done! Result will be printed out!')
print(res.text)
