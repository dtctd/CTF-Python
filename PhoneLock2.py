import hashlib, itertools, re, random, string
import multiprocessing as mp

characters = '01234567890'
characters2 = '01234567890abcdef'
#salt="67d46047e06242422adc38bfxxxxxxxx"
#valid="fc34d007cd68dff4a7xxxxxxxxxxxxxx"
hash="67d46047e06242422adc38bf"

# Define an output queue
output = mp.Queue()

def check_password(password):
    pw = "%s%s%s" % (hash, ''.join(salt), password)
    if re.match('^fc34d007cd68dff4a7',(hashlib.md5(pw.encode('utf-8')).hexdigest())):
        return  password[-4:]

gen = itertools.product(characters,repeat=4)
for password in gen:
    print ("passwords tested: " + str(testedpw))
    check_password(''.join(password))

# define a example function
def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                    string.ascii_lowercase
                    + string.ascii_uppercase
                    + string.digits)
               for i in range(length))
    output.put(rand_str)

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=(5, output)) for x in range(4)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)