import qrcode


'''
qr=qrcode.make("Hi!")
data="https://www.linkedin.com/in/venkata-ganesh-11802955/"
qr=qrcode.make(data)
qr.save("linkedinprofile.png")
qr.show()
'''


qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("enter your name:")
age=int(input("enter your age:"))
email=input("enter your email:")
mobile=int(input("enter your mobile:"))
data={"Name":name,"Age":age,"Email":email,"Mobile":mobile}
qr.add_data(data)
img=qr.make_image()
img.save("mydetails.png")
img.show()



