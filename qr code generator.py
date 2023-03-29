import qrcode


text = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(text)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("yourqrcode.png")
