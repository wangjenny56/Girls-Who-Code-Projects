from PIL import Image
im = Image.open("JennyWangPhoto.jpg")
im.show()



h = im.height
w = im.width

for x in range(w):
	for y in range(h):
		s = im.getpixel((x,y)) 
	
		if (s[0] > s[1] and s[0] > s[2]):
			im.putpixel((x,y), (217, 26, 33))
		elif (s[1] > s[2] and s[1] > s[0]):
			im.putpixel ((x,y), (0, 51, 76))
		else:
			im.putpixel ((x,y), (252, 227, 166))
	

im.show()
im.save("output.jpg", "jpeg")


darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
	
