import cv2
import socket

class Camera :
    def __init__(self, ppassword, purl, pIp, puser="admin"):
        self.user =puser
        self.password = ppassword
        self.url =purl
        self.ip = pIp

    def __str__(self):
        return print( "Camera information: IP: %s, url : %s, User : %s, Password: %s" %(self.ip, self.url , self.user, self.password))
    
    def GetImage(self):
        vidcap = cv2.VideoCapture("rtsp://%s:%s@%s:554/%s" %(self.user, self.password,self.ip, self.url))
        if vidcap.isOpened():
            success, image = vidcap.read()
            return image

    def cam_status(self):
        print("tryin ip: %s" %(self.ip) )
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            sock.connect((self.ip,554))
            return True
        except:
            return False

   




