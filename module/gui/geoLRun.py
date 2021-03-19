#!/usr/bin/python
#by bafomet
import os, sys
import time
import math
import socket
import urllib.request
from urllib.request import urlopen
from json import load
from PIL import Image, ImageDraw

import wx  # use wx to build the UI.
from geopy.distance import geodesic

import geoLGobal as gv
import geoLPanel as gp

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class GeoLFrame(wx.Frame):
    """ URL/IP gps position finder main UI frame."""
    def __init__(self, parent, id, title):
        """ Init the UI and parameters """
        wx.Frame.__init__(self, parent, id, title, size=(1200, 560))
        self.SetBackgroundColour(wx.Colour(0, 0, 360))
        self.SetIcon(wx.Icon(gv.ICO_PATH))
        gv.iGeoMgr = self.geoMgr = GeoMgr(self)
        gv.iDCPosMgr = DataCenterMgr(self)
        self.SetSizer(self._buidUISizer())

#--GeoLFrame-------------------------------------------------------------------
    def _buidUISizer(self):
        """ Build the main UI Sizer. """
        flagsR = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL
        mSizer = wx.BoxSizer(wx.HORIZONTAL)
        mSizer.AddSpacer(5)
        gv.iMapPanel = self.mapPanel = gp.PanelMap(self)
        mSizer.Add(self.mapPanel, flag=flagsR, border=2)
        mSizer.AddSpacer(5)
        mSizer.Add(wx.StaticLine(self, wx.ID_ANY, size=(-1, 560),
                                 style=wx.LI_VERTICAL), flag=flagsR, border=2)
        mSizer.AddSpacer(5)
        gv.iCtrlPanel = gp.PanelCtrl(self)
        mSizer.Add(gv.iCtrlPanel)
        return mSizer

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class GeoMgr(object):
    """ Manager module to handle the geo position calculation."""
    def __init__(self, parent):
        self.parent = parent
        self.scIPaddr = ''      # url ip address

#--GeoMgr----------------------------------------------------------------------
    def checkIPValid(self, ipAddr):
        """ Check whether a IP address is a valid one."""
        try:
            socket.inet_aton(ipAddr)
            return True
        except socket.error:
            return False

#--GeoMgr----------------------------------------------------------------------
    def getGpsPos(self, ipaddr):
        """ Connect to the https://ipinfo.io to get the input ipaddr's gps position
            under float decimal format.
        """
        data, lat, lon = load(urlopen('https://ipinfo.io/' + str(ipaddr) + '/json')), 0, 0
        for attr in data.keys():
            if gv.iCtrlPanel:
                gv.iCtrlPanel.updateDetail(str(attr).ljust(13)+data[attr])
            if attr == 'loc': (lat, lon) = data[attr].split(',')
        return (float(lat), float(lon))

#--GeoMgr----------------------------------------------------------------------
    def urlToIp(self, url):
        """ Convert the URL to ip address."""
        return str(socket.gethostbyname(url))

#--GeoMgr----------------------------------------------------------------------
    def getGoogleMap(self, lat, lng, wTileN, hTileN, zoom):
        """ Download the google map tile based on the GPS position and combine
            the tiles to one image.
        """
        start_x, start_y = self.getStartTlXY(lat, lng, zoom)
        width, height = 256 * wTileN, 256 * hTileN
        map_img = Image.new('RGB', (width, height))
        for x in range(0, wTileN):
            for y in range(0, hTileN):
                url = 'https://mt0.google.com/vt?x=' + \
                    str(start_x+x)+'&y='+str(start_y+y)+'&z='+str(zoom)
                current_tile = str(x)+'-'+str(y)
                urllib.request.urlretrieve(url, current_tile)
                map_img.paste(Image.open(current_tile), (x*256, y*256))
                os.remove(current_tile)
        return map_img

#--GeoMgr----------------------------------------------------------------------
    def getStartTlXY(self, lat, lng,zoom):
        """ Generates an X,Y tile coordinate based on the latitude, longitude 
            and zoom level
            Returns:    An X,Y tile coordinate
        """
        tile_size = 256
        # Use a left shift to get the power of 2
        # i.e. a zoom level of 2 will have 2^2 = 4 tiles
        numTiles = 1 << zoom
        # Find the x_point given the longitude
        point_x = (tile_size/ 2 + lng * tile_size / 360.0) * numTiles // tile_size
        # Convert the latitude to radians and take the sine
        sin_y = math.sin(lat * (math.pi / 180.0))
        # Calulate the y coorindate
        point_y = ((tile_size / 2) + 0.5 * math.log((1+sin_y)/(1-sin_y)) * -(tile_size / (2 * math.pi))) * numTiles // tile_size
        return int(point_x), int(point_y)

#--GeoMgr----------------------------------------------------------------------
    def PIL2wx(self, image):
        """ Convert the PIL image to wx bitmap."""
        width, height = image.size
        return wx.BitmapFromBuffer(width, height, image.tobytes())

#--GeoMgr----------------------------------------------------------------------
    def wx2PIL(self, bitmap):
        """ Convert the wxBitmap to PIL image."""
        size = tuple(bitmap.GetSize())
        try:
            buf = size[0]*size[1]*3*"\x00"
            bitmap.CopyToBuffer(buf)
        except:
            del buf
            buf = bitmap.ConvertToImage().GetData()
        return Image.frombuffer("RGB", size, buf, "raw", "RGB", 0, 1)


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class DataCenterMgr(object):
    """ Data center manager.
    """
    def __init__(self, parent):
        self.parent = parent
        self.centerDict = {} # data center dict
        self.loadDCPos()

#-----------------------------------------------------------------------------
    def loadDCPos(self):
        """ Load the data center position."""
        with open(gv.DC_POS_PATH, 'r') as fh: 
            for line in fh:
                dcID, _, dcPos  = line.rstrip().split(';')
                self.centerDict[dcID] = [float(i) for i in dcPos.split(',')]

#-----------------------------------------------------------------------------
    def fineNear(self, pos):
        """ Return the nearest data ceter position and distance.
        """
        dcID, dist = None, 0
        for key in self.centerDict.keys():
            tmp = geodesic(pos, self.centerDict[key]).miles*1.60934  # mile to km
            if dist == 0 or dist > tmp:
                dcID, dist = key, tmp
        return (dcID, dist)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class MyApp(wx.App):
    def OnInit(self):
        mainFrame = GeoLFrame(None, -1, gv.APP_NAME)
        mainFrame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
