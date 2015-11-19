import hashlib, itertools, re

characters = '01234567890abcdef'

def check_password(password):
    pw = "%s%s" % ("67d46047e06242422adc38bf", password)
    if re.match('^fc34d007cd68dff4a7',(hashlib.md5(pw.encode('utf-8')).hexdigest())):
        print ("the phone password could be " + password[-4:])
        print (hashlib.md5(pw.encode('utf-8')).hexdigest())

gen = itertools.product(characters,repeat=12)
for password in gen:
    check_password(''.join(password))