#LinearData.py by Kiliagan
import numpy as np

def readFile(file):
	xPos = []
	yPos = []
	with open(file) as f:
		for row in f:
			holder = row.replace('\n','').split(',')
			xPos.append(float(holder[0]))
			yPos.extend([float(holder[1])])
	return xPos, yPos
	
def genData(intercept,slopeX,slopeY,xPos,yPos):
	delta = np.random.random_sample()
	return intercept + (slopeX * xPos) + (slopeY * yPos) + delta
	

if __name__ == "__main__":
	file = 'Cordinates.csv'
	xPos,yPos = readFile(file)
	intercept = np.random.random_sample()
	slopeX = np.random.random_sample()
	slopeY = np.random.random_sample()
	data = []
	for i,row in enumerate(xPos):
		data.append(genData(intercept,slopeX,slopeY,xPos[i],yPos[i]))
	print data