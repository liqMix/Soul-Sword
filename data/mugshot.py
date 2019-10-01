
from constants import MUGSHOT
import requests
import os
from PIL import Image
import numpy as np

scale_factor = MUGSHOT['scale_factor']
intensity_correction = MUGSHOT['intensity_correction']
width_correction = MUGSHOT['width_correction']
x_pos = MUGSHOT['x_pos']
y_pos = MUGSHOT['y_pos']
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))


def download_image(source, path):
    response = requests.get(source, verify=False)
    path = path + '/' + source[-20:]
    if not os.path.exists(path):
        print(path)
        with open(path, mode='xb') as f:
            f.write(response.content)
    return path


def delete_image(path):
    if os.path.exists(path):
        os.remove(path)


# Sourced from cdiener
# asciinator.py
# https://gist.github.com/cdiener/10567484
def process_image(image, temp=True):
    img = Image.open(image)
    s = (round(img.size[0] * scale_factor * width_correction),
         round(img.size[1] * scale_factor))
    img = np.sum(np.asarray(img.resize(s)), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** intensity_correction * (chars.size - 1)

    if temp:
        delete_image(image)
    return list("".join(r) for r in chars[img.astype(int)])


class Mugshot:
    def __init__(self, source):
        path = './data/temp'
        if not os.path.isdir(path):
            os.mkdir(path)
        print(source)
        if source == 'style/img/male.jpg' or source == 'style/img/female.jpg':
            self.image = process_image('./data/default.png', temp=False)
        else:
            try:
                img_path = download_image(source, path)
                self.image = process_image(img_path)
            except OSError:
                delete_image(img_path)
                self.image = process_image('./data/default.png', temp=False)

    def draw(self, con):
        offset = 0
        increment = 1

        for line in self.image:
            con.print(x_pos, y_pos + offset, line)
            offset += increment


