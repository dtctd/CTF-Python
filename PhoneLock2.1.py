import hashlib, itertools, re

characters = '01234567890abcdef'

def check_password(password):
    pw = "%s%s" % ("dee1a7334aed0349b6e4a295", password)
    if re.match('^8b76d02e4bbc2d89bc',(hashlib.md5(pw.encode('utf-8')).hexdigest())):
        print ("the phone password could be " + password[-4:])
        print (hashlib.md5(pw.encode('utf-8')).hexdigest())

gen = itertools.product(characters,repeat=12)
for password in gen:
    check_password(''.join(password))