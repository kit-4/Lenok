from PIL import Image
import os
path = "/var/www/u1208057/data/www/lenok.space/static/catalog/images"
l = os.listdir(path=path)

for image in l:
    path_name = os.path.join(path, image)
    img = Image.open(path_name)
    img.save(path_name, 'JPEG', dpi=[300,300], quality=65)

