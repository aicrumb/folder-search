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
	images = input("number: ")

	encoding = encode(query)
	dists = [torch.mean(torch.abs(encoding-i)).item() for i in encodings]
	sorted_dists = sorted(dists, reverse=False)

	# print(dists.index(min(dists)))
	# print(filenames[dists.index(min(dists))])
	indices = [dists.index(dist) for dist in sorted_dists]
	for i in range(int(images)):
		min_ind = indices[i]
		my_img = cv2.imread(folder+"/"+filenames[min_ind])
		cv2.imshow("My image", my_img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
