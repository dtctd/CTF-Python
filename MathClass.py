infile = open("math-class.in","r")
outfile = open("math-class.out","w")

l = infile.readline().split()
cl = [int(f) if f.isdigit() else f for f in l]
if cl[0] == "add":
	output = cl[1] + cl[2]
elif cl[0] == "subtract":
	output = abs(cl[1] - cl[2])

outfile.write(str(output))
outfile.write("\n")
