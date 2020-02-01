import sys

if len(sys.argv) < 2:
	print('usage: python3 {} (text file name)'.format(sys.argv[0]))
	exit()

try:
	f = open(sys.argv[1])
except:
	print('Cannot open file {}'.format(sys.argv[1]))
	exit()

statemap = {};
while True:
	line = f.readline()
	if (len(line) == 0):
		break;
	line = line.rstrip('\n')
	pair = line.split(',')
	state = pair[0].capitalize()
	capitol = pair[1].capitalize()
	statemap[state] = capitol;
	statemap[capitol] = state;
f.close()

b = True
while b:
	a = input("Type state/capital: ")
	a = a.capitalize()
	if a in statemap:
		print(statemap[a])
	elif a == "Quit":
		b = False
	else:
		print('nil');
