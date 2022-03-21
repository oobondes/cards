#row-4-column-4.png
img_file = r"P:\GolfCard\GolfCard\static\content\cards\temp\row-4-column-4.png"

from PIL import Image

img = Image.open(img_file)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255 and item[3] == 0:
        pass#newData.append((255, 255, 255, 0)) # This is for checking white pixels, replace transparent. Do
        # if item[3] == 0 to check for transparent pixels.
    else:
        newData.append(item)

img.putdata(newData)
img.save("img2.png", "PNG")


