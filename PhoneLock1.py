import hashlib, itertools

characters = '0123456789'
password_length = 4
salt="b4fbd04efda015a6b251d1a825ec4015"
valid="e3ac60df779cf55440e188a4b827daa3"

def check_password(password):
    pw = "%s%s" % (''.join(salt), password)
    if (hashlib.md5(pw.encode('utf-8')).hexdigest()== valid):
        print ("the phone password is " + password)
        print (hashlib.md5(pw.encode('utf-8')).hexdigest())

gen = itertools.product(characters,repeat=4)
for password in gen:
    check_password(''.join(password))


