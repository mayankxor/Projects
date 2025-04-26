import qrcode

qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L, 
	box_size=12,
	border=2
	)
string = "google"
qr.add_data(string)

img = qr.make_image(
	fill_color="black",
	back_color="white")
img.save(f"qrcode.png")