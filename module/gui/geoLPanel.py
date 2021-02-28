from module.gui import geoLGobal as gv

import wx
import webbrowser
from datetime import datetime


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class PanelMap(wx.Panel):
    """ Map panel to show the google map."""
    def __init__(self, parent, panelSize=(768, 512)):
        wx.Panel.__init__(self, parent,  size=panelSize)
        self.SetBackgroundColour(wx.Colour(0, 200, 200))
        self.panelSize = panelSize
        self.bmp = wx.Bitmap(gv.BGIMG_PATH, wx.BITMAP_TYPE_ANY)
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.SetDoubleBuffered(True)

#--PanelMap--------------------------------------------------------------------
    def onPaint(self, evt):
        """ Draw the map bitmap and mark the gps position."""
        dc = wx.PaintDC(self)
        l, (w, h) = 25, self.panelSize  # set the bm size and the marker size.
        dc.DrawBitmap(self._scaleBitmap(self.bmp, w, h), 0, 0)
        dc.SetPen(wx.Pen('BLUE', width=1, style=wx.PENSTYLE_SOLID))
        w, h = w//2, h//2
        dc.DrawLine(w-l, h, w+l, h)
        dc.DrawLine(w, h-l, w, h+l)

#--PanelMap--------------------------------------------------------------------
    def _scaleBitmap(self, bitmap, width, height):
        """ Resize a input bitmap.(bitmap-> image -> resize image -> bitmap)"""
        #image = wx.ImageFromBitmap(bitmap) # used below 2.7
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        #result = wx.BitmapFromImage(image) # used below 2.7
        result = wx.Bitmap(image, depth=wx.BITMAP_SCREEN_DEPTH)
        return result

#--PanelMap--------------------------------------------------------------------
    def updateBitmap(self, bitMap):
        """ Update the panel bitmap image."""
        if not bitMap: return
        self.bmp = bitMap

#--PanelMap--------------------------------------------------------------------
    def updateDisplay(self, updateFlag=None):
        """ Set/Update the display: if called as updateDisplay() the function will 
            update the panel, if called as updateDisplay(updateFlag=?) the function
            will set the self update flag.
        """
        self.Refresh(False)
        self.Update()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class PanelCtrl(wx.Panel):
    """ Function control panel."""
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.Colour(0, 0, 360))
        self.gpsPos = None
        self.SetSizer(self._buidUISizer())
    
#--PanelCtrl-------------------------------------------------------------------
    def _buidUISizer(self):
        """ build the control panel sizer. """
        flagsR = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL
        ctSizer = wx.BoxSizer(wx.VERTICAL)
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        ctSizer.AddSpacer(5)
        # Row idx 0: show the search key and map zoom in level.
        hbox0.Add(wx.StaticText(self, label="Варианты : ".ljust(15)),
                  flag=flagsR, border=2)
        self.scKeyCB = wx.ComboBox(
            self, -1, choices=['IPv4', 'URL'], size=(80, 22), style=wx.CB_READONLY)
        self.scKeyCB.SetSelection(0)
        hbox0.Add(self.scKeyCB, flag=flagsR, border=2)
        hbox0.AddSpacer(17)
        hbox0.Add(wx.StaticText(
            self, label="Размеры карты : ".ljust(20)), flag=flagsR, border=2)
        self.zoomInCB = wx.ComboBox(
            self, -1, choices=[str(i) for i in range(10, 19)], size=(80, 22), style=wx.CB_READONLY)
        self.zoomInCB.SetSelection(3)
        hbox0.Add(self.zoomInCB, border=2)  # flagsR = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL
        ctSizer.Add(hbox0, border=2) # flag=flagsR, border=2)
        ctSizer.AddSpacer(5)
        # Row idx 1: URL/IP fill in text field.
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.StaticText(self, label="IP/URL : "),
                  flag=flagsR, border=2)
        self.scValTC = wx.TextCtrl(self, size=(241, 22))
        hbox1.Add(self.scValTC, flag=flagsR, border=2)
        hbox1.AddSpacer(2)
        self.searchBt = wx.Button(self, label='Поиск', size=(80, 22))
        self.searchBt.Bind(wx.EVT_BUTTON, self.onSearch)
        hbox1.Add(self.searchBt, flag=flagsR, border=2)
        ctSizer.Add(hbox1, border=2)  # flag=flagsR
        ctSizer.AddSpacer(5)
        # Row idx 2: url parse detail information display area.
        ctSizer.Add(wx.StaticText(self, label="Полная информация : "), border=2)  # ,
                    # flag=flagsR, )
        ctSizer.AddSpacer(5)
        self.detailTC = wx.TextCtrl(
            self, size=(381, 410), style=wx.TE_MULTILINE)
        ctSizer.Add(self.detailTC, border=2) #  , #  flag=flagsR, )
        ctSizer.AddSpacer(5)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.clearBt = wx.Button(self, label='Очистить', size=(70, 22))
        self.clearBt.Bind(wx.EVT_BUTTON, self.onClear)
        hbox2.Add(self.clearBt, flag=flagsR, border=2)
        hbox2.AddSpacer(10)
        self.searchBt = wx.Button(
            self, label='Открыть GPS координаты на карте : ', size=(300, 22))
        self.searchBt.Bind(wx.EVT_BUTTON, self.onMark)
        hbox2.Add(self.searchBt, flag=flagsR, border=2)
        ctSizer.Add(hbox2, border=2)  #  flag=flagsR, )
        return ctSizer

#--PanelCtrl-------------------------------------------------------------------
    def onClear(self, event):
        """ Clear all the text field."""
        self.updateDetail(None)

#--PanelCtrl-------------------------------------------------------------------
    def onMark(self, event):
        """ Creat the google map gps position marked url and open the url by the 
            system default browser.
        """
        url = "http://maps.google.com/maps?z=12&t=m&q=loc:" + \
            str(self.gpsPos[0])+"+"+str(self.gpsPos[1])
        webbrowser.open(url)

#--PanelCtrl-------------------------------------------------------------------
    def onSearch(self, event):
        """ Convert a url to the IP address, find the GPS position of the IP 
            address and draw it on the map.
        """
        self.updateDetail("----- %s -----" % str(datetime.today()))
        scIPaddr = val = self.scValTC.GetValue()
        # Convert the URL to ip address if needed.
        if self.scKeyCB.GetSelection():
            url = str(
                val.split('//')[1]).split('/')[0] if 'http' in val else val.split('/')[0]
            self.updateDetail(url)
            scIPaddr = gv.iGeoMgr.urlToIp(url)
        if gv.iGeoMgr.checkIPValid(scIPaddr):
            self.updateDetail(scIPaddr)
        else:
            self.updateDetail(" The IP address [%s] is invalid." %str(scIPaddr))
            return None
        # get the gps pocition:
        self.gpsPos = (lat, lon) = gv.iGeoMgr.getGpsPos(scIPaddr)
        self.updateDetail('Server GPS position[%s]' % str((lat, lon)))
        (dcId, dist) = gv.iDCPosMgr.fineNear(self.gpsPos)
        self.updateDetail('Nearest AWS data center[%s]' % str(dcId))
        self.updateDetail('Distance [%s] Km' % str(dist))
        # get the position google map and update the display
        bitmap = gv.iGeoMgr.PIL2wx(gv.iGeoMgr.getGoogleMap(
            lat, lon, 3, 2, int(self.zoomInCB.GetValue())))
        if gv.iMapPanel:
            gv.iMapPanel.updateBitmap(bitmap)
            gv.iMapPanel.updateDisplay()
        self.updateDetail("----- Finished ----- \n")

#--PanelCtrl-------------------------------------------------------------------
    def updateDetail(self, data):
        """ Update the data in the detail text field. Input 'None' will clear the 
            detail information text field.
        """
        if data is None:
            self.scValTC.Clear()
            self.detailTC.Clear()
        else:
            self.detailTC.AppendText(" - %s \n" %str(data))
