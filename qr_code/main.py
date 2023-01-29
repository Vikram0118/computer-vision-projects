import qrcode
import cv2

features = qrcode.QRCode(version=1,box_size=40, border=3)
features.add_data("https://www.youtube.com")
features.make(fit=True)
generate_qr = features.make_image(fill_color="#FFFFFF", back_color= "#000000")
generate_qr.save("./qr_link.png")


generate_qr_2 = qrcode.make("ICT SEMESTER EXAMINATION IS GOING ")
generate_qr_2.save("./qr_message.png")


decode = cv2.QRCodeDetector()
val, points, straignt_qrcode = decode.detectAndDecode(cv2.imread("./qr_message.png"))
print(val)

