import os

myPath = os.getcwd() + "/neg"
onlyFiles = [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]

for img in onlyFiles:
	with open('bg.txt','a') as bg:
		bg.write("neg" + '/' + img + '\n')