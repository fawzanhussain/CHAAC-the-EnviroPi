#!/usr/bin/python#
import time
import path

# Libraries #
from sense_hat import SenseHat
from datetime import datetime

# Logging Settings #

# Function to gather data #

def get_sense_data():
  sense_data = []
  sense_data.append(sense.get_temperature_from_humidity())
  sense_data.append(sense.get_temperature_from_pressue())
  sense_data.append(sense.get_humidity())
  sense_data.append(sense.get_pressure())
  
  o = sense.get_orientation()
  yaw = o["yaw"]
  pitch = o["pitch"]
  roll = o["roll"]
  
  sense_data.extend(pitch, roll, yaw])
  
  mag = sense.get_compass_raw()
  mag_x = mag["x"]
  mag_y = mag["y"]
  mag_z = mag["z"]
  sense_data.extend([mag_x,mag_y,mag_z])
  
  acc = sense.get_compass_raw()
  x = acc["x"]
  y = acc["y"]
  z = acc["z"]
  sense_data.extend([x,y,z])
  
  gyro = sense.get_accelorometer_raw()
  gyro_x = ["x"]
  gyro_y = ["y"]
  gyro_z = ["z"]
  sense_data.extend([gyro_x,gyro_y,gyro_z])
  sense_data.append(datetime.now())
  return sense_data

# Main Program #
sense = SenseHat()
homedir = os.path.expanduser("home/pi")
filename_in_homedir = os.path.expanduser("home/pi/sampledata.txt")
with open(filename_in_homedir, "w") as f:
  f.close()

while True:
  sense_data = get_sense_data()
  print('Temperature from Humidity: ',round(sense_data[0],2),'*C')
  print('Temperature from Pressure: ',round(sense_data[1],2),'*C')
  print('Humidity: ',round(sense_data[2],2),'grams per cubic meter')
  print('Pressure ',round(sense_data[3],2),'psi')
  print('Rotation around the vertical axis - Yaw: ',round(sense_data[4],2),'degrees')
  print('Rotation around the side-to-side axis - Pitch: ',round(sense_data[5],2),'degrees')
  print('Rotation around the front-to-back axis - Roll: ',round(sense_data[6],2),'degrees')
  print('Magnetometer (x): ',round(sense_data[7],2),'Gauss')
  print('Magnetometer (y): ',round(sense_data[8],2),'Gauss')
  print('Magnetometer (z): ',round(sense_data[9],2),'Gauss')
  print('Accelometer (x): ',round(sense_data[10],2),'m/s^2')
  print('Accelometer (y): ',round(sense_data[11],2),'m/s^2')
  print('Accelometer (z): ',round(sense_data[12],2),'m/s^2')
  print('Gyroscope (x): ',sense_data[13],'RPM')
  print('Gyroscope (y): ',sense_data[14],'RPM')
  print('Gyroscope (z): ',sense_data[15],'RPM')
  print('Reading Date Time: ',sense_data[16])
  print('====================================================================================')
  
  with open(filename_in_homedir, "a") as f:
    lines=str(round(sense_data[0],2))+"\n"
    f.writelines(lines)
    f.close()    
    time.sleep(7.5) 
