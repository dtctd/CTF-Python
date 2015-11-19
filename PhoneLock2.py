import hashlib, itertools, re

characters = '01234567890'
characters2 = '01234567890abcdef'
salt=   "67d46047e06242422adc38bfxxxxxxxx"
valid=  "fc34d007cd68dff4a7xxxxxxxxxxxxxx"

def check_password(password):
    gen2 = itertools.product(characters2,repeat=8)
    for salt in gen2:
        
        pw = "67d46047e06242422adc38bf" + ''.join(salt) + password
        #print ("password =" + pw)
        check = hashlib.md5(pw.encode('utf-8')).hexdigest()
        #print ("hash =" + check)
        if re.match('^fc34d007cd68dff4a7',check):
            print ("the phone password could be " + password)
            print (hashlib.md5(pw.encode('utf-8')).hexdigest())

gen = itertools.product(characters,repeat=4)
for password in gen:
    check_password(''.join(password))
