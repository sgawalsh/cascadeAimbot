import cv2
import os

posOrNegString = "pos"
resizeTuple = (35, 50)

myPath = os.getcwd() + "\\" + posOrNegString + "\\origsize"

onlyFiles = [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]

for file in onlyFiles:
	try:
		img = cv2.imread(myPath + "/" + file)
		img = cv2.resize(img, resizeTuple)
		cv2.imwrite(os.getcwd() + "/" + posOrNegString + "/" + file, img)
	except Exception as e:
		print(str(e))