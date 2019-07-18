import urllib.request
import cv2, os

def store_raw_images(posOrNeg):
	if posOrNeg not in ['pos', 'neg']:
		print('choose pos or neg images to download')
		return
	else:
		if not os.path.exists(posOrNeg):
			os.makedirs(posOrNeg)
		if not os.path.exists(posOrNeg + '/origSize'):
			os.makedirs(posOrNeg + '/origSize')
		
		lines = [line.rstrip('\n') for line in open(posOrNeg + 'URLS.txt')]
		
		pic_num = 1
		for i in lines:
			try:
				print(i)
				urllib.request.urlretrieve(i, posOrNeg + "/origSize/" + str(pic_num) + ".jpg")
				img = cv2.imread(posOrNeg + "/origSize/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
				cv2.imwrite(posOrNeg + "/origSize/" + str(pic_num) + ".jpg", img)
				pic_num += 1
			except Exception as e:
				print(str(e))