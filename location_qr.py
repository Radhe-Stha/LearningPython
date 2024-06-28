# Program to find exact location using latitude and longitude via qr code generation

import qrcode

latitude = 27.6705997
longitude = 85.4265476

location = f"https://www.google.com/maps?q=<latitude>,<longitude>"

img = qrcode.make(location)
type(img)
img.save("location.png")
