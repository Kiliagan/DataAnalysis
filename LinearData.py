#LinearData.py by Kiliagan

def readFile(file):
	with open(file) as f:
		for row in f:
			print row
	
if __name__ == "__main__":
	file = 'Cordinates.csv'
	readFile(file)