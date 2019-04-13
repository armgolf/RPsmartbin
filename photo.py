from picamera import PiCamera
from time import sleep
import os
import datetime

def photo():
    path = '/home/pi/Documents/smartbin3-master/images'
    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)
    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    lastfile = sorted_filename_list[-1]
    ending = lastfile[6:]
    string = ending[:-4]
    number = int(float(string))
    imagename = "-image"+str(number+1)+".jpg"
    print(imagename)
    camera = PiCamera()
    camera.resolution = (1200, 800)
    camera.rotation = 180
    sleep(1)
    camera.capture('/home/pi/Documents/smartbin3-master/images/'+imagename)
    camera.close()

print(datetime.datetime.now())
photo()

#for i in range(1, 5):
#    photo()

#print(datetime.datetime.now())
