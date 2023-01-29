import base64

with open('./jpeg.jpeg','rb') as imagefile:
    byteform=base64.b64encode(imagefile.read())
    f=open('output.bin','wb')
    f.write(byteform)
    f.close()
