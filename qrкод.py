import qrcode

text = input("")
img = qrcode.make(text)
img.save('qr.png')