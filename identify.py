import requests
import os
import json

def identify():
    url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
    path = '/home/pi/Documents/smartbin3-master/images'
    name_list = os.listdir(path)
    full_list = [os.path.join(path,i) for i in name_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)
    sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
    lastfile = sorted_filename_list[-1]
    data = {'file': open('/home/pi/Documents/smartbin3-master/images/'+lastfile, 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}
    #data = {'file': open('./images/image2.jpg', 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}
    response = requests.post(url, auth= requests.auth.HTTPBasicAuth('GvqHLwBkqU4tpSyXDU471CG6K1y5XYw8', ''), files=data)
    #print(response.text)
    data = json.loads(response.text)
    a = data["result"][0]["prediction"][0]["label"]
    print(a)
    return(a)
