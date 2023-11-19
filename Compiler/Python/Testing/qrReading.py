import glob
import cv2
import pandas as pd
import pathlib
from PIL import Image
import numpy as np

def processImage(imagePath) :



    file = Image.open(imagePath)
    levels = np.array(file).ravel()
    thsh = np.quantile(levels, 0.35) 
    def fn(x): return 255 if x > thsh else 0
    file = file.convert('L').point(fn, mode='1')
    
    file.save("Compiler/Output/QRTestProc.jpeg")




def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
    
    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    
    # value, points, straight_qrcode = detect.detectAndDecode(img)
    return detect.detectAndDecode(img)
    
processImage("Compiler/Output/QRTest2.jpeg")

print(read_qr_code("Compiler/Output/QRTestProc.jpeg"))

