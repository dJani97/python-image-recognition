import numpy as np
from PIL import Image

"""
opening & printing sample image
"""
img = Image.open('../images/dot.png')
img_arr = np.asarray(img)
print(img_arr)


