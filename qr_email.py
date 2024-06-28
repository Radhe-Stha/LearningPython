#send email using qr code genetaror
import qrcode
email_address = "aasmin0070608@gmail.com"
subject = "My First Email Using Python."
body = "Hello , this is my first email using Python."
email = f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(email)
type(img)
img.save("email.png")