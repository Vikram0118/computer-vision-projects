import pytesseract
import PIL.Image
import pyttsx3

File_Name = "text.png"

myconfig = r"--psm 6 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open(File_Name), config = myconfig)
print("RECOGNIZIED TEXT :")
print(text)

file = open("output.txt", "w")
file.write(text)
file.close()




