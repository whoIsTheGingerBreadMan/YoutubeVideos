import requests

from io import BytesIO
from PIL import Image
import numpy as np

def get_image_from_url(url,save_to):
    """
    provide a url string of an image and a path to save to and saves the image at the location given.
    """
    img_request = requests.get(url)
    Image.open(BytesIO(img_request.content)).save(save_to)
    
def show_image(url):
    """
    provide a URL string and output a PIL image.
    """
    img_request = requests.get(url)
    img = Image.open(BytesIO(img_request.content))
    return img

def get_image_as_numpy(url,target_size=None):
    """
    provide a URL string and output a numpy image.
    """
    img = show_image(url)
    if target_size == None:     
        return np.array(img)
    else:
        img = np.array(img.resize(target_size))
        return img