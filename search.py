from classify import load, classify, encode
import torch
import os
import cv2
folder = "folder"
filenames = os.listdir(folder)

# get encodings for every image stored with the title
encodings = []

# for i in filenames:
# 	filename = f"{folder}/{i}"
# 	encodings.append(encode(filename))

def getFirstFrame(videofile):
    vidcap = cv2.VideoCapture(videofile)
    success, image = vidcap.read()
    if success:
        cv2.imwrite("../first_frame.jpg", image)  # save frame as JPEG file
def rescan():
	global encodings
	global filenames

	filenames = os.listdir(folder)
	encodings = []
	for i in filenames:
		if i.split(".")[-1] not in ["mov", "webp", "gif", "mp4", "avi"]:
			filename = f"{folder}/{i}"
			encodings.append(encode(filename))
		else:
			filename = "../first_frame.jpg"
			getFirstFrame(f"{folder}/{i}")
			encodings.append(encode(filename))
rescan()


while True:
	query = input("Query: ")
	if(query!="do!rescan"):
		images = input("number: ")

		encoding = encode(query)
		dists = [torch.mean(torch.abs(encoding-i)).item() for i in encodings]
		sorted_dists = sorted(dists, reverse=False)

		# print(dists.index(min(dists)))
		# print(filenames[dists.index(min(dists))])
		indices = [dists.index(dist) for dist in sorted_dists]
		for i in range(int(images)):
			min_ind = indices[i]
			print(filenames[min_ind])
			if filenames[min_ind].split(".")[-1] not in ["mov", "webp", "gif", "mp4", "avi"]:
				my_img = cv2.imread(folder+"/"+filenames[min_ind])
				cv2.imshow("My image", my_img)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
			else:
				print("Could not show video with audio, you have to navigate to the file yourself.")
				cap = cv2.VideoCapture(folder+"/"+filenames[min_ind])
				if (cap.isOpened()== False):
				  print("Error opening video stream or file")
				while(cap.isOpened()):
				  ret, frame = cap.read()
				  if ret == True:
				    cv2.imshow('Frame',frame)
				    if cv2.waitKey(25) & 0xFF == ord('q'):
				      break
				  else:
				    break
				cap.release()
				cv2.destroyAllWindows()
	else:
		rescan()
		print("Scanned images.")
