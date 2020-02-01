import random
e = True
f = 0
a = ["apple", "brain", "cause", "dread", "elegy", "flame", "great", "hello", "intro", "jelly", "krill", "leave", "month", "novel", "olive", "pearl", "quest", "river", "stone", "treat", "usurp", "venom", "watch", "xenon", "yeast", "zebra"]

b = random.randint(0,len(a)-1)
c = a[b]
print (c[0])

d = input("Your guess? ")

while e:
	if f == 9 and d != c:
		print("game over")
		e = False
	elif d == "":
		print("you wasted a guess")
		d = input("Your guess: ")
		f = f+1
	elif len(d) != 5:
		print("1 2 3 4 5 that's how we count to five")
		d = input("Your guess ")
		f = f+1
	elif d[0] != c[0]:
		print("abcdefghijklmnopqrstuvwxyz")
		d = input("Your guess: ")
		f = f+1
	elif d == c:
		print("good job")
		e = False
	else:
		print("wrong")
		d = input("Your guess? ")
		f = f+1
