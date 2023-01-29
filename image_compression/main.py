import PIL
from PIL import Image
# from tkinter.filedialog import *

img = Image.open("./jjj.jpg")
# file_path = askopenfilename()
# img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

def encode(message):
	encoded_message=""
	i=0
	while(i<=len(message)-1):
		count=1
		ch=message[i]
		j=i
		while(j<len(message)-1):
			if(message[j]==message[j+1]):
				count=count+1
				j=j+1
			else:
				break
		encoded_message=encoded_message+str(count)+ch
		i=j+1
	return encoded_message

img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
# save_path = askopenfilename()

img.save("./resize.jpg")

