#LinearData.py by Kiliagan

def readFile(file):
	xPos = []
	yPos = []
	with open(file) as f:
		for row in f:
			holder = row.replace('\n','').split(',')
			xPos.append(holder[0])
			yPos.extend([holder[1]])
	return xPos, yPos
if __name__ == "__main__":
	file = 'Cordinates.csv'
	xPos,yPos = readFile(file)
	print xPos
	print yPos