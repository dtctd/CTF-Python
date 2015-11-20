import multiprocessing, hashlib, re
from itertools import product

alphabet = "abcdef12234567890"
num_parts = 4
part_size = len(alphabet) // num_parts

def do_job(first_bits):
    for password in product(first_bits, alphabet, alphabet, alphabet, alphabet, alphabet, alphabet, alphabet, alphabet, alphabet, alphabet, alphabet):
        pw = "%s%s" % ("dee1a7334aed0349b6e4a295", password)
        if re.match('^8b76d02e4bbc2d89bc',(hashlib.md5(pw.encode('utf-8')).hexdigest())):
            print ("the phone password could be " + password[-4:])
            print (hashlib.md5(pw.encode('utf-8')).hexdigest())

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    results = []
    for i in range(num_parts):
        if i == num_parts - 1:
            first_bit = alphabet[part_size * i :]
        else:
            first_bit = alphabet[part_size * i : part_size * (i+1)]
        results.append(pool.apply_async(do_job(first_bit)))

    pool.close()
    pool.join()