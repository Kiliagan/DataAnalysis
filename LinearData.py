#LinearData.py by Kiliagan
import numpy as np
from scipy.optimize import curve_fit

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
	
def fn(x,a,b,c):
	return a + b*x[0] + c*x[1]
	

if __name__ == "__main__":
	file = 'Cordinates.csv'
	xPos,yPos = readFile(file)
	
	
	intercept = np.random.random_sample()
	slopeX = np.random.random_sample()
	slopeY = np.random.random_sample()
	data = []
	for i,row in enumerate(xPos):
		data.append(genData(intercept,slopeX,slopeY,xPos[i],yPos[i]))
	
	popt, pcon = curve_fit(fn,[xPos,yPos],data)
	#print [intercept, slopeX, slopeY]
	#print popt
	
	predData = []
	dataResd = [] 
	for i,row in enumerate(xPos):
		predData.append(fn([xPos[i],yPos[i]],popt[0],popt[1],popt[2]))
		dataResd.append(data[i]-predData[i])
		print [xPos[i],yPos[i],data[i],predData[i],dataResd[i]]
	