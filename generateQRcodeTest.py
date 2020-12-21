import qrcode

img = qrcode.make('Some data here')
img.save("img.png","PNG")
