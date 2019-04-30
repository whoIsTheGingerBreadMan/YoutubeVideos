import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from IPython.display import HTML

def plot_image_grid(images,num_rows=1):
    """
    input a list of images and it plots them with num_rows rows."""
    n= len(images)
    num_cols = np.ceil(n/num_rows)
    fig,axes = plt.subplots(ncols=int(num_cols),nrows=int(num_rows))
    axes = axes.flatten()
    fig.set_size_inches((15,15))
    for i,image in enumerate(images):
        axes[i].imshow(image)

def place_video(location_of_video):
    """
    location_of_video: location of mp4 video"""
    video = io.open(location_of_video, 'r+b').read()
    encoded = base64.b64encode(video)
    return HTML(data='''<video alt="test" controls><source src="data:video/mp4;base64,{0}" type="video/mp4" /></video>'''.format(encoded.decode('ascii')))
    