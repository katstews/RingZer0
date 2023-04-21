from PIL import Image, ImageChops
import time
im1 = Image.open('frame_17_delay-0.03s.png')

for x in range(31):
    paddedx = str(x).zfill(2)
    im2 = Image.open(f'frame_{paddedx}_delay-0.03s.png')

    im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
    im3.show()
