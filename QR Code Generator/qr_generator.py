import qrcode.image.svg

'''qr = qrcode.QRCode(version=1, 
				   error_correction=qrcode.constants.ERROR_CORRECT_L,
				   box_size = 20,
				   border=2)

qr.add_data("https://www.youtube.com")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")'''

#------------- For svg Image -------------
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World !", image_factory=factory)
svg_img.save("svgqr.svg")