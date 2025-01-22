import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

def convert_csv(file_to,new_file):
    my_data = genfromtxt(file_to, delimiter=',')
    plt.imshow(my_data,cmap="gray")
    plt.axis("off")
    plt.savefig(new_file)
    plt.show()

convert_csv("/its/home/drs25/image.csv",
             "/its/home/drs25/Pictures/output_image_rgb.png")
    
