#qr code generator 
import qrcode
img = qrcode.make('RadhaKrishna')
type(img)  # qrcode.image.pil.PilImage
img.save("radhakrishna.png")

#wifi using qr code 
wifi_type = "WPA"
wifi_ssid = "herosima_5"
wifi_password = "CLB2629822"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")

#sms using qrcode generated image
phone_number = 9849105556
message = "hello qr- sms"
sms = f"SMSTO:{phone_number}:{message}"
type(img)
img = qrcode.make(sms)
img.save("sms.png")



#mecard
name = "Radha Krishna Shrestha"
phone = 9849100000
email_id = "aasmin0070608@gmail.com"
e_card = f"MECARD:N:{name};TEL:{phone};EMAIL:{email_id};;;"
type(img)
img = qrcode.make(e_card)
img.save("ecard.png")

