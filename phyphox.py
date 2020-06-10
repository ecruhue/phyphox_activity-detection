import urllib.request
import time
import webbrowser  
import datetime
import pandas as pd
import os
import wget

os.chdir('/Users/huerzhen/Downloads')

IPAddress = '192.168.0.143'  #IP address and port This is different for each person and specified by the phyphox app
num_data = 5 #Take 5 data chunks
pause_tm = 5 #The amount of time to wait in between data collections

save_dat = 'http://' + IPAddress + '/export?format=0'  #Saving data
clear_dat = 'http://' + IPAddress + '/control?cmd=clear'  #Clearing a data collection
start_dat = 'http://' + IPAddress + '/control?cmd=start'  #Starting a data collection

urllib.request.urlopen(start_dat)
all_files=[]
sensor_name="Acceleration with g "
for v in range(0,num_data):
    file=urllib.request.urlretrieve(save_dat,"/Users/huerzhen/Downloads/file_"+str(v)+".xls")
    all_files.append(file)
    time.sleep(pause_tm) #Wait a bit before collecting data again
#re
urllib.request.urlopen(clear_dat)  #Clear the data Collection
