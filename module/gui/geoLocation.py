import re
import json
# from urllib2 import urlopen python2
#By bafomet
# https://pypi.org/project/geoip2/

from urllib.request import urlopen

import socket
url1 = 'aws.amazon.com'
url2 = 'www.datacenterdynamics.com'
url3 = 'www.nus.edu.sg'
ipaddr = str(socket.gethostbyname(url3))

#url = '172.217.194.105'
url = ipaddr
#url = '137.132.212.202'
# url = 'https://www.datacenterdynamics.com'
# method 1

gpsPos = None

def ipInfo(addr=''):
    global gpsPos
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    for attr in data.keys():
        #will print the data line by line
        print(attr, ' '*13+'\t->\t', data[attr])
        if attr == 'loc':
            print(data[attr])
            gpsPos = data[attr]

ipInfo(url)

#========================

#!/usr/bin/python
# GoogleMapDownloader.py 
#By bafomet

import urllib.request
from PIL import Image, ImageDraw
import os
import math

class GoogleMapDownloader:
    """
        A class which generates high resolution google maps images given
        a longitude, latitude and zoom level
    """

    def __init__(self, lat, lng, zoom=12):
        """
            GoogleMapDownloader Constructor
            Args:
                lat:    The latitude of the location required
                lng:    The longitude of the location required
                zoom:   The zoom level of the location required, ranges from 0 - 23
                        defaults to 12
        """
        self._lat = lat
        self._lng = lng
        self._zoom = zoom

    def getXY(self):
        """
            Generates an X,Y tile coordinate based on the latitude, longitude 
            and zoom level
            Returns:    An X,Y tile coordinate
        """
        
        tile_size = 256

        # Use a left shift to get the power of 2
        # i.e. a zoom level of 2 will have 2^2 = 4 tiles
        numTiles = 1 << self._zoom

        # Find the x_point given the longitude
        point_x = (tile_size/ 2 + self._lng * tile_size / 360.0) * numTiles // tile_size

        # Convert the latitude to radians and take the sine
        sin_y = math.sin(self._lat * (math.pi / 180.0))

        # Calulate the y coorindate
        point_y = ((tile_size / 2) + 0.5 * math.log((1+sin_y)/(1-sin_y)) * -(tile_size / (2 * math.pi))) * numTiles // tile_size

        return int(point_x), int(point_y)

    def generateImage(self, **kwargs):
        """
            Generates an image by stitching a number of google map tiles together.
            
            Args:
                start_x:        The top-left x-tile coordinate
                start_y:        The top-left y-tile coordinate
                tile_width:     The number of tiles wide the image should be -
                                defaults to 5
                tile_height:    The number of tiles high the image should be -
                                defaults to 5
            Returns:
                A high-resolution Goole Map image.
        """

        start_x = kwargs.get('start_x', None)
        start_y = kwargs.get('start_y', None)
        tile_width = kwargs.get('tile_width', 5)
        tile_height = kwargs.get('tile_height', 5)

        # Check that we have x and y tile coordinates
        if start_x == None or start_y == None :
            start_x, start_y = self.getXY()

        # Determine the size of the image
        width, height = 256 * tile_width, 256 * tile_height

        #Create a new image of the size require
        map_img = Image.new('RGB', (width,height))

        for x in range(0, tile_width):
            for y in range(0, tile_height) :
                url = 'https://mt0.google.com/vt?x='+str(start_x+x)+'&y='+str(start_y+y)+'&z='+str(self._zoom)

                current_tile = str(x)+'-'+str(y)
                urllib.request.urlretrieve(url, current_tile)
            
                im = Image.open(current_tile)
                map_img.paste(im, (x*256, y*256))
              
                os.remove(current_tile)

        return map_img


(lat, lon) = gpsPos.split(',')

print((lat, lon))

# Create a new instance of GoogleMap Downloader
gmd = GoogleMapDownloader(float(lat),float(lon), 18)

print("The tile coorindates are {}".format(gmd.getXY()))

try:
    # Get the high resolution image
    img = gmd.generateImage()
except IOError:
    print("Could not generate the image - try adjusting the zoom level and checking your coordinates")
else:
    #Save the image to disk
    img.save("high_resolution_image.png")
    print("The map has successfully been created")


im = Image.open("high_resolution_image.png")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save("test.png", "PNG")



exit()
# method 2
response = urlopen('https://www.datacenterdynamics.com')
data = json.load(response)

IP = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('Your IP detail\n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(
    org, region, country, city, IP))
