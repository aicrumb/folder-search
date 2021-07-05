from classify import load, classify, encode
import torch
import os
import cv2
folder = "folder"
filenames = os.listdir(folder)

# get encodings for every image stored with the title
encodings = []

for i in filenames:
	filename = f"{folder}/{i}"
	encodings.append(encode(filename))

while True:
	query = input("Query: ")
	encoding = encode(query)
	dists = [torch.dist(encoding, i).item() for i in encodings]
	min_ind = dists.index(min(dists))
	print("Your File Is: {}".format(folder+"/"+filenames[min_ind]))

	my_img = cv2.imread(folder+"/"+filenames[min_ind])
	#print(my_img)
	cv2.imshow("My image", my_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()