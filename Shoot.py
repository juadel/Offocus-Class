from  skimage.color import rgb2gray
from skimage.restoration import estimate_sigma
from scipy.ndimage import variance
from skimage.filters import laplace 
import requests
import cv2


class Shoot:
    def __init__(self, image):
       self.img = image 
       self.clear_state = None
       self.Variance = None
       self.Noise = None
    
    def __str__(self):
       print("creates a Offocus object image to perform Variance and noise analysis ") 

    def Get_Parameters(self):
        if len(self.img.shape) == 3:
            self.img =rgb2gray(self.img)
        self.Variance = variance(laplace(self.img, ksize=3))
        self.Noise = estimate_sigma(self.img)


    def CheckBlurry(self):
        values = {"Variance" : self.Variance, "Noise": self.Noise}
        r = requests.get('http://ec2-99-79-44-109.ca-central-1.compute.amazonaws.com:5000/api', json=values)
        json_response = r.json()
        self.clear_state = json_response["ESTIMATE"] 
    
    def PrintImage(self):
        cv2.putText(self.img, "{}: {:.2f}".format(self.clear_state, self.Variance),(10,31),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,256),3)
        cv2.imshow("Image", self.img)
        cv2.waitkey(0)
        cv2.destroyAllWindows()
        