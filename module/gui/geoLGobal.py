import os

dirpath = os.path.dirname(os.path.realpath(__file__))
APP_NAME = 'OSINT SAN Геолокация'

#------<IMAGES PATH>-------------------------------------------------------------
IMG_FD = 'img'
ICO_PATH = os.path.join(dirpath, IMG_FD, "geoIcon.ico")
BGIMG_PATH = os.path.join(dirpath, IMG_FD, "background.jpg")
DC_POS_PATH = os.path.join(dirpath, "awsRecord.txt")

#-------<GLOBAL PARAMTERS>-----------------------------------------------------
iCtrlPanel = None   # panel to do the control
iMapPanel = None    # panel to display the google map.
iGeoMgr = None      # program control manager.
iDCPosMgr = None    # data ceter position manager.
