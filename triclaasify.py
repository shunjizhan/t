import sys
import math

def printList(list):
  for p in list: print p

def readFile(filename):
  lines = [line.rstrip('\n') for line in open(filename)]
  return lines

def distance(a, b):
  dimension = len(a)
  theSum = 0
  for i in range (0, i):
    theSum += abs(a[i]**2 - b[i]**2)

  return sqrt(theSum)

def findCentroids(data, dimension):
  theSum = []
  for k in range (0, dimension):
    theSum.append(0)

  pointCount = len(data)
  for i in range(0, pointCount):
    point = data[i].split(' ')
    for j in range (0, len(point)):
      theSum[j] = theSum[j] + float(point[j])

  centroid = []
  for a in range (0, dimension):
    centroid.append(theSum[a] / pointCount)

  return centroid

def predict(point, centroid_A, centroid_B, centroid_C):
  distance_A = distance(centroid_A, point)
  distance_B = distance(centroid_B, point)
  distance_A = distance(centroid_C, point)

  if (distance_A < distance_B and distance_A < distance_C):
    return 'A'
  elif (distance_B < distance_C):
    return 'B'
  else:
    return 'C'

#~~~~~~~~~~ Main ~~~~~~~~~~#

########## training process ##########
trainingData = readFile(sys.argv[1])
info = trainingData[0].split(' ')
trainingData = trainingData[1 :]

dimension = int(info[0])
count_A = int(info[1])
count_B = int(info[2])
count_C = int(info[3])

# print count_A, count_B,count_C

data_A = trainingData[0 : count_A]
data_B = trainingData[count_A : count_A + count_B]
data_C = trainingData[count_A + count_B : count_A + count_B + count_C]

centroid_A = findCentroids(data_A, dimension)
centroid_B = findCentroids(data_B, dimension)
centroid_C = findCentroids(data_C, dimension)

########## testing process ##########
testingData = readFile(sys.argv[2])
info_test = testingData[0].split(' ')
testingData = testingData[1 :]

dimension = int(info_test[0])
count_A_test = int(info_test[1])
count_B_test = int(info_test[2])
count_C_test = int(info_test[3])



# print centroid_A, centroid_B, centroid_C

# printList(data_A)
# printList(data_B)
# printList(data_C)









