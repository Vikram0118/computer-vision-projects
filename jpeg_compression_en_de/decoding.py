import base64

file=open('./output.bin','rb')
byte=file.read()
file.close()
fh=open('./ee.jpeg','wb')
fh.write(base64.b64decode((byte)))
fh.close()