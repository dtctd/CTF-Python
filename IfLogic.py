infile = open("if-logic.in","r")
outfile = open("if-logic.out","w")

l = infile.read().split(",")
l = map(int, l)

print(l)
output = ""

for x in l:
    if x > -1 and x < 51:
        outfile.write("hi\n")
    elif x > 49 and x < 101:
        outfile.write("hey\n")
    else:
        outfile.write("hello\n")
