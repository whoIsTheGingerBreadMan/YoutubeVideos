from PIL import Image
import numpy as np

def load_image(location,target_size=None):
    """
    provide a location and output a numpy image.
    """
    img = Image.open(location)
    if target_size == None:     
        return np.array(img)
    else:
        img = np.array(img.resize(target_size))
        return img