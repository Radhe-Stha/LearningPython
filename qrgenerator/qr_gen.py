import qrcode
img = qrcode.make("apple")
type(img)
img.save("apple.png")