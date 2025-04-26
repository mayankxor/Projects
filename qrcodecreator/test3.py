import qrcode
import qrcode.image.svg

# if method=='basic':
# 	# Simple factory, just a set of rects
# 	factory = qrcode.image.svg.SvgImage
# elif method == 'fragment':
# 	# Fragment factory, just a set of rects
# 	factory = qrcode.image.svg.SvgFragmentImage
# else:
# 	# Combined path factory, fixed whitespaces.
# 	factory = qrcode.image.svg.SvgPathImage

img = qrcode.make("qr code data", image_factory=qrcode.image.svg.SvgPathFillImage)
img.save("qrcode.svg")