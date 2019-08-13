from  skimage.color import rgb2gray
from skimage.restoration import estimate_sigma
from scipy.ndimage import variance
from skimage.filters import laplace 
from skimage import io 
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
        copy_img = self.img
        if len(self.img.shape) == 3:
            copy_img =rgb2gray(self.img)
        
        self.Variance = variance(laplace(copy_img, ksize=3))
        self.Noise = estimate_sigma(copy_img)


    def CheckBlurry(self):
        values = {"Variance" : self.Variance, "Noise": self.Noise}
        r = requests.get('http://ec2-35-182-106-153.ca-central-1.compute.amazonaws.com:5000/api', json=values)
        json_response = r.json()
        text ="CLEAR"
        if json_response["ESTIMATE"]==1:
            text = "BLURRY"
        self.clear_state = text
        
    
    def PrintShoot(self,text="Image"):
        cv2.putText(self.img, "{}".format(self.clear_state),(10,31),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,256),3)
        cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        cv2.imshow(text , self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        