import qrcode
from PIL import Image

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,  # or 0 if cropping
)

qr.add_data("https://mkusssa.netlify.app/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
bbox = img.getbbox()
cropped_img = img.crop(bbox)

cropped_img.save("mkusssa_qr_cropped.png")
print("Saved cropped QR code!")
