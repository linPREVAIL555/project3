v = input("go: ")
a = []

vord = v.lower()
dout='';
for d in range(len(vord)):
	if (d%2) == 1:
		dout = dout + vord[d].upper();
	else:
		dout = dout + vord[d].lower();
print (dout)

y = set(["A","E","I","O","U"])

x = set(["(",")"])

word = v.lower()
out = '';
for c in range(0,len(word)):
	if (word[c] in x):
		out = out + word[c];
print (out)

