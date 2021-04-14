from pms7003 import Pms7003Sensor, PmsSensorException
import serial
from datetime import datetime
import time
import numpy as np
import configparser  #Module pour gérer l import d un fichier de configuration
import argparse #Module pour ajouter des paramètres lors de l appel du script 
from influxdb import InfluxDBClient  #Module pour gérer l export des données vers la base InfluxDB
import os
import argparse
import sys
#sensor='PMS7003'

#############################################
#INFO A REMPLIR AVANT LANCEMENT DU FICHIER

#port = '/dev/ttyUSB3'
moyenne=10
#num_serie_capteur = 'test3'
site='test'


###########################################

if __name__ == '__main__':

    all_args = argparse.ArgumentParser()
    try:
       
       # Should have exactly two options
        print(all_args)
        #print ('usage: comptage.py -p <port> -n <nom>')
        all_args.add_argument("-p", "--Port", required=True, help="Port")
        all_args.add_argument("-n", "--Nom", required=True, help="Nom")
        args = vars(all_args.parse_args())
        sensor = Pms7003Sensor('/dev/'+args['Port'])
        day = datetime.now().strftime("%d")
        fichier=open("donnees_{}_{}.txt".format(args['Nom'],datetime.now().strftime("%Y%m%d")),"w") 
        while True:
          if day!=datetime.now().strftime("%d"):
              fichier.close()
              fichier=open("donnees_{}_{}.txt".format(args['Nom'],datetime.now().strftime("%Y%m%d")),"w") 
              day = datetime.now().strftime("%d")
              dic= sensor.read()
              #print (dic)
              #print((datetime.now().strftime("%Y/%m/%d %H:%M:%S"),dic['pm1_0'],dic['pm2_5'],dic['pm10'],dic['n0_3'],dic['n0_5'],dic['n1_0'],dic['n2_5'],dic['n5_0'],dic['n10']))
              fichier.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" %(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),dic['pm1_0'],dic['pm2_5'],dic['pm10'],dic['n0_3'],dic['n0_5'],dic['n1_0'],dic['n2_5'],dic['n5_0'],dic['n10']))
          else :
              dic= sensor.read()
              #print (dic)
              #print((datetime.now().strftime("%Y/%m/%d %H:%M:%S"),dic['pm1_0'],dic['pm2_5'],dic['pm10'],dic['n0_3'],dic['n0_5'],dic['n1_0'],dic['n2_5'],dic['n5_0'],dic['n10']))
              fichier.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" %(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),dic['pm1_0'],dic['pm2_5'],dic['pm10'],dic['n0_3'],dic['n0_5'],dic['n1_0'],dic['n2_5'],dic['n5_0'],dic['n10']))
          time.sleep(2)
    except KeyboardInterrupt: 
        fichier.close()    
        sensor.close()
