# GPSPhoto
# Programmer: Jess Williams
# EMail: stripes.denomino@gmail.com
# Purpose: extracts and converts GPS Data from Photos

# Import Modules
import sys
import webbrowser
import exifread
import json
if sys.version_info.major == 2:
    import urllib
    urlopen = urllib.urlopen
else:
    import urllib.request
    urlopen = urllib.request.urlopen
from PIL import Image
from piexif import load, dump
from datetime import datetime

VER = (2, 2, 2)


class InvalidLatitude(ValueError):
    '''Invalid Latitude Exception'''

    pass


class InvalidLongitude(ValueError):
    '''Invalid Longitude Exception'''

    pass


class InvalidMinutes(ValueError):
    '''Invalid Minutes Exception'''

    pass


class InvalidSeconds(ValueError):
    '''Invalid Seconds Exception'''

    pass


class InvalidApiKey(ValueError):
    '''Invalid API Key Exception'''

    pass


class GPSInfo(object):
    """Object to represent GPS Data to be added or modified to Image File"""

    def __init__(self, coord, alt=0, timeStamp=None, googleApiKey=None):
        """GPSInfo(coord, alt, timeStamp)
        Constructor takes three arguments
            coord     - tuple or list of two floats representing the gps
                        coordinates i.e. (35.104860, -106.628915)
            alt       - int representing altitude, defaults to 0
            timeStamp - str or datetime representing date and time
                        i.e. '1970:01:01 09:05:05', defaults to None"""

        self.__validateArguments(coord, alt, timeStamp)
        self.__googleApiKey = googleApiKey
        self.getElevation()

    def __validateArguments(self, coord, alt, timeStamp):
        """Validates Arguments"""

        self.__validateCoord(coord)
        self.__validateAlt(alt)
        self.__validateTimeStamp(timeStamp)

    def __validateCoord(self, coord):
        """Validates coord"""
        if not (isinstance(coord, tuple) or isinstance(coord, list)):
            raise ValueError("coord must be of type tuple or list")
        elif not len(coord) == 2:
            raise ValueError("coord length must be 2")
        elif (not (isinstance(coord[0], float) or isinstance(coord[1], float))):
            raise ValueError("coord values must be of type float")
        elif coord[0] > 89.999999 or coord[0] < -89.999999:
            raise InvalidLatitude(str("Invalid latitude %f, valid range " +
                    "(-89.999999-89.999999)") % (coord[0]))
        elif coord[1] > 179.999999 or coord[1] < -179.999999:
            raise InvalidLongitude(str("Invalid longitude %f, valid range " +
                    "(-179.999999-179.999999)") % (coord[1]))
        self.__coord = coord

    def __validateAlt(self, alt):
        """Validate alt"""
        if not (isinstance(alt, int)):
            raise ValueError("alt must be of type int")
        self.__alt = alt

    def __validateTimeStamp(self, timeStamp):
        """Validate timeStamp"""
        if not (timeStamp is None or
                isinstance(timeStamp, datetime) or
                isinstance(timeStamp, str)):
            raise ValueError("timeStamp must be of type None, datetime, or str")
        elif isinstance(timeStamp, str):
            try:
                self.__timeStamp = datetime.strptime(timeStamp,
                        '%Y:%m:%d %H:%M:%S')
            except:
                raise ValueError(str("timeStamp '%s' invalid format, valid " +
                        "format 'YYYY:MM:DD hh:mm:ss' " +
                        "i.e.'1970:01:01 09:05:05'") % (timeStamp))
        elif timeStamp is None:
            self.__timeStamp = datetime.now()
        else:
            self.__timeStamp = timeStamp

    def getKey(self):
        """Returns Google Api Key"""

        return self.__googleApiKey

    def setKey(self, apiKey):
        """setKey(apiKey)

        Sets Google Api Key for Elevation Calls. Takes One Parameter.

        apiKey - str of Google Api Key"""

        self.__googleApiKey = apiKey
        self.getElevation()

    apiKey = property(getKey, setKey)

    def getCoord(self):
        """Returns coord - represents gps coordinates"""

        return self.__coord

    def setCoord(self, coord):
        """setCoord(coord)

        Sets coord, takes one argument
            coord - tuple or list of two floats i.e. (35.104860, -106.628915)"""

        self.__validateCoord(coord)

    coord = property(getCoord, setCoord)

    def getAlt(self):
        """Returns alt - represents altitude or elevation"""

        return self.__alt

    def setAlt(self, alt):
        """setAlt(alt)

        Sets alt, takes one argument
            alt - int or float representing altitude or elevation"""

        self.__validateAlt(alt)

    alt = property(getAlt, setAlt)

    def getDateTime(self):
        """Returns datetime object timeStamp"""

        return self.__timeStamp

    def getGPSFormattedDate(self):
        """Returns GPS Formatted Date in str form
            i.e. '1970:05:01'"""

        return b'%s' % str.encode(self.timeStamp.split(' ')[0])

    def getGPSFormattedTime(self):
        """Returns GPS Formatted Time in tuple of tuples form
            i.e. ((18, 1), (29, 1), (22,1))"""

        time = self.__timeStamp
        return ((time.hour, 1), (time.minute, 1), (time.second, 1))

    def getTimeStamp(self):
        """Returns str of timeStamp -  represents timeStamp"""

        nowTime = self.__timeStamp.time().isoformat()
        nowTime = nowTime[:nowTime.find('.')]
        nowDate = self.__timeStamp.date().isoformat().replace('-', ':')
        now = nowDate + " " + nowTime
        return now

    def setTimeStamp(self, timeStamp):
        """setTimeStamp(timeStamp)

        Sets timeStamp, takes one argument
            timeStamp - None, str or datetime representing time and date,
                        None will default to time now"""

        self.__validateTimeStamp(timeStamp)

    timeStamp = property(getTimeStamp, setTimeStamp)

    def getElevation(self):
        """getElevation(coords, googleApiKey)

           Returns an int representing the elevation from Google in reference to
           GPS Coordinates. Takes two arguments.

                coord        - tuple or list of two floats representing the
                               decimal coordinates.
                googleApiKey - str of the Google Api Key
        """

        if not self.__googleApiKey is None:
            coords = self.__coord
            url = str("https://maps.googleapis.com/maps/api/elevation/json?" +
                        "locations=" + str(coords[0]) + "," + str(coords[1]) +
                        str("&key=%s" % self.__googleApiKey))
            website = urlopen(url)
            jsonData = json.loads(website.read())
            if jsonData['status'] == 'OK':
                results = jsonData['results'][0]
                self.__alt = int(round(results['elevation']))
            else:
                raise InvalidApiKey("%s, %s" % (jsonData['status'],
                        jsonData['error_message']))


class GPSPhoto(object):
    """GPSPhoto(object) -> GPSPhoto Object

    Creates an Object for the modification, extraction, and removal of GPS Exif
    Tag info on JPEG and Tiff formatted images"""

    def __init__(self, filename=""):
        """Constructor - Takes String argument defaults to empty string

        if argument is passed in will initialize object with filename
        example:
            GPSPhoto("test.jpg")
            or
            GPSPhoto()"""

        # determine if file is loaded or not
        try:
            self.loadFile(filename)
        except IOError:
            self.__gpsRawDict = None

        self.__getGPSData()

    def loadFile(self, filename):
        """loadFile(filename)

        Loads Image file for extraction takes one argument
            filename - str of the path/to/imagefile"""

        # Validate filename type
        if not isinstance(filename, str):
            raise ValueError("filename needs to be of type str")

        self.__filename = filename
        self.__getRawData()
        self.__getGPSData()

    def __validateCoordAndQuadArguments(self, coord, quad):
        """Validates arguments coord and quad"""

        # Validate coord type
        if not isinstance(coord, tuple) and not isinstance(coord, list):
            raise ValueError("coord must be of type tuple or list")
        # Validate coord length
        elif len(coord) < 2 or len(coord) > 3:
            raise ValueError("len(coord) must be 2 or 3")
        # Validate quad type
        elif not isinstance(quad, str):
            raise ValueError("quad must be of type str")

        # Validate quad value
        if (not str(quad).upper()[0] == 'N' and not str(quad).upper()[0] == 'S'
                and not str(quad).upper()[0] == 'E' and
                not str(quad).upper()[0] == 'W'):
            raise ValueError("quad value must be one of the following N S E W")

        # Validate coord values type for degrees and minutes
        if len(coord) >= 2:
            # Validate degree type
            if (not (isinstance(coord[0], int))):
                raise ValueError("coord degree value must be of types int ")

            # Validate minute type
            if (not (isinstance(coord[1], int) or isinstance(coord[1], float))):
                raise ValueError("coord minute value must be of types int or " +
                        "float")

            # Check the values of degrees for latitude
            if (str(quad).upper()[0] == 'N' or str(quad).upper()[0] == 'S'):
                if coord[0] < 0 or coord[0] > 89:
                    raise InvalidLatitude(str("Invalid latitude degrees %d, " +
                            "valid range (0-89)") % (coord[0]))
            # Check the values of degrees for longitude
            else:
                if coord[0] < 0 or coord[0] > 179:
                    raise InvalidLongitude(str("Invalid longitude degrees %d, "
                            + "valid range (0-179)") % (coord[0]))

            # Check value of minutes
            if coord[1] < 0 or coord[1] > 59:
                raise InvalidMinutes("Invalid minutes %d, valid range (0-59)" %
                        (coord[1]))

        # Validate coord value type for seconds
        if len(coord) == 3:
            if (not(isinstance(coord[2], int) or isinstance(coord[2], float))):
                raise ValueError("coord values must be of types int or float")
            # Validate value for seconds
            if coord[2] < 0 or coord[2] > 59.999999:
                raise InvalidSeconds(str("Invalid seconds %f, valid range " +
                        "(0-59.999999)") % (coord[2]))

    def __validateCoord(self, coord):
        """Validates coord"""

        # Validate coord type
        if not (isinstance(coord, tuple) or isinstance(coord, list)):
            raise ValueError("coord must be of type tuple or list")

        # Validate length of coord
        if not len(coord) == 2:
            raise ValueError("coord must contain 2 floats")

        # Validate value types of coord
        if (not (isinstance(coord[0], float) or isinstance(coord[1], float))):
            raise ValueError("coord values must be of type float")

        # Validate values of coord latitude
        if coord[0] < -89.999999 or coord[0] > 89.999999:
            raise InvalidLatitude(str("Invalid Latitude %f, valid range " +
                    "(-89.999999-89.999999)") % (coord[0]))

        # Validate values of coord longitude
        if coord[1] < -179.999999 or coord[1] > 179.999999:
            raise InvalidLongitude(str("Invalid Longitude %f, valid range " +
                    "(-179.999999-179.999999)") % (coord[1]))

    def __validateModData(self, gpsInfo, newFileName):
        """Validates Mod Arguments"""

        # Validate Coordinates
        if not (isinstance(gpsInfo, GPSInfo)):
            raise ValueError("gpsInfo must be of type GPSInfo")
        elif not isinstance(newFileName, str):
            raise ValueError("newFileName must be of type str")

    def __validateLoad(self):
        """Validates Object State, whether file is successfully loaded or not"""

        if self.__gpsRawDict is None:
            if not self.__filename == "":
                raise IOError("%s file did not load, corrupt or invalid file" %
                        self.__filename)
            else:
                raise IOError("no file loaded")

    def coord2decimal(self, coord, quad):
        """coord2decimal(coord, quad)

        Converts Degrees, Minutes and Seconds to decimal.

        Arguments:
            coord - tuple or list consisting of degree, minute, and second or
                    degree and minute.
            quad  - str reference of the character 'N','S','E','W'
                    representing North, South, East, West. This also specifies
                    latitude or longitude"""

        # Validate Arguments
        self.__validateCoordAndQuadArguments(coord, quad)

        # Determine which type is being passed
        degree = coord[0]
        minute = coord[1]
        decimal = (minute / 60.0) + degree
        if len(coord) == 3:
            second = coord[2]
            decimal = decimal + (second / 3600.0)

        # Determine Quadrant
        if str(quad).upper()[0] == 'W' or str(quad).upper()[0] == 'S':
            modifier = -1
        else:
            modifier = 1

        return decimal * modifier

    def decimal2Degree(self, coord):
        """decimal2Degree(coord)

        Convert Decimal Coordinates to Degrees, Minutes, Seconds
        and determines Quadrant, takes one argument
            coord - tuple or list of 2 floats

        Returns a dictionary of latitude and longitude"""

        # Validate Arguments
        self.__validateCoord(coord)

        # Declare Local Variables
        gpsDict = {}
        lat = coord[0]
        lon = coord[1]

        # Determine the quadrant of latitude
        if lat < 0:
            gpsDict[1] = b"S"
            lat = lat * -1
        else:
            gpsDict[1] = b"N"

        # Determine the quadrant of longitude
        if lon < 0:
            gpsDict[3] = b"W"
            lon = lon * -1
        else:
            gpsDict[3] = b"E"

        # Build Variables
        degLat = int(lat)
        degLon = int(lon)
        minLat = int((lat - degLat) * 60)
        minLon = int((lon - degLon) * 60)
        secLat = int(round(((lat - int(lat)) -
                (float(minLat) / 60)) * 36000000))
        secLon = int(round(((lon - int(lon)) -
                (float(minLon) / 60)) * 36000000))

        # Populate Dictionary
        gpsDict[2] = ((degLat, 1), (minLat, 1), (secLat, 10000))
        gpsDict[4] = ((degLon, 1), (minLon, 1), (secLon, 10000))

        return gpsDict

    def __getRawData(self):
        ''' Returns the raw GPS Data returned from ExifRead'''

        # Declare Local Variables
        self.__gpsRawDict = {}

        # Open images file for reading (binary mode)
        image = open(self.__filename, 'rb')

        # Return Exif tags
        tags = exifread.process_file(image)

        # Get GPS Tags List
        tagKeys = []
        self.__foundGPS = False
        for tag in list(tags.keys()):
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename',
                    'EXIF MakerNote'):
                # Search For GPS Data
                if tag.find('GPS') > -1:
                    self.__foundGPS = True
                    tagKeys.append(tag)

        # Build Dictionary
        for tag in tagKeys:
            self.__gpsRawDict[tag] = tags[tag]

    def getRawData(self):
        """Returns Raw GPS Exif Data"""
        return self.__gpsRawDict

    rawData = property(getRawData)
    """Property for getting raw GPS Exif Data"""

    def __getGPSData(self):
        """Gets GPS Data from Image

        There are 3 different types of Longitude and Latitude data stored.
                1 - type is already in decimal format
                    Assumption no Ref Value
                2 - type is in degree and minute format
                    Assumption [100, 44.5678]
                3 - type is in degree, minute and second
                    Assumption [100, 44,95521/5000]
        This function will assume the assumptions are correct and parse the
        strings and return a list of floating elements, takes an parameter of
        list of strings"""

        def parseItude(tude):
            """Internal Function for parsing string from the dictionary key
            tude"""
            #Declare Local Variables
            coordList = []

            # Determine which type
            if len(tude) == 3:
                coordList.append(int(tude[0].strip()))
                if tude[1].find('/') > -1:
                    minutes = tude[1].strip().split('/')
                    val = float(minutes[0]) / float(minutes[1])
                    coordList.append(val)
                else:
                    coordList.append(float(tude[1].strip()))
                if itude[2].find('/') > -1:
                    seconds = tude[2].strip().split('/')
                    val = float(seconds[0]) / float(seconds[1])
                else:
                    val = float(tude[2].strip())
                coordList.append(val)
            elif len(itude) == 2:
                coordList.append(int(tude[0].strip()))
                coordList.append(float(tude[1].strip()))
            else:
                coordList.append(float(tude[0].strip()))

            return coordList

        self.__gpsDict = None

        # Check that file loaded properly
        if not self.__gpsRawDict is None:
            tags = self.__gpsRawDict

            self.__gpsDict = {}

            for tag in list(tags.keys()):
                if tag == 'GPS GPSTimeStamp':
                    t = [x.strip() for x in
                         str(tags[tag]).strip('[').strip(']').split(',')]
                    m = (t[2] if '/' not in t[2] else
                         str(int(t[2].split('/')[0]) / int(t[2].split('/')[1])))
                    self.__gpsDict['UTC-Time'] = t[0] + ":" + t[1] + ":" + m
                elif tag == 'GPS GPSDate':
                    d = str(tags[tag]).split(':')
                    self.__gpsDict['Date'] = str(str(d[1]) + "/" + str(d[2]) +
                            "/" + str(d[0]))
                elif tag == 'GPS GPSLatitude':
                    itude = str(tags[tag]).strip('[').strip(']').split(',')
                    var = parseItude(itude)
                    if len(var) > 1:
                        lat = self.coord2decimal(var,
                                str(tags['GPS GPSLatitudeRef']))
                    else:
                        lat = float(var[0])
                    self.__gpsDict['Latitude'] = lat
                elif tag == 'GPS GPSLongitude':
                    itude = str(tags[tag]).strip('[').strip(']').split(',')
                    var = parseItude(itude)
                    if len(var) > 1:
                        lng = self.coord2decimal(var,
                                str(tags['GPS GPSLongitudeRef']))
                    else:
                        lng = float(var[0])
                    self.__gpsDict['Longitude'] = lng
                elif tag == 'GPS GPSAltitude':
                    if str(tags[tag]).find('/') > -1:
                        alt = str(tags[tag]).split('/')
                        altitude = int(alt[0]) / int(alt[1])
                    else:
                        altitude = int(str(tags[tag]))
                    try:
                        ref = int(str(tags['GPS GPSAltitudeRef']))
                        if ref == 1:
                            altitude = altitude * -1
                        self.__gpsDict['Altitude'] = altitude
                    except:
                        self.__gpsDict['Altitude'] = altitude

    def getGPSData(self):
        """Returns GPS Data Dictionary"""
        return self.__gpsDict

    gpsData = property(getGPSData)
    """Property for getting GPS Data"""

    def stripData(self, newFileName):
        """stripData(newFileName)

        Strips all exif data from photo and saves to new jpeg,
        takes one argument
            filename - str of /path/to/newImageFile"""

        self.__validateLoad()

        # Open Image and get ExifData
        im = Image.open(self.__filename)
        exif_dict = load(im.info["exif"])

        # Remove GPS Data from Photo
        exif_dict.pop('GPS', None)

        # Convert ExifData back and save in new file
        exif_bytes = dump(exif_dict)
        im.save(newFileName, "jpeg", exif=exif_bytes)

    def modGPSData(self, gpsInfo, newFileName):
        """modGPSData(coord, newFileName, alt)

        Modifies GPS Data, takes three arguments
            coord       - a list or tuple of (latitude,longitude)
            newFileName - str of /path/to/newImageFile
            alt         - int or float of the altitude"""

        # makes base exif tag info
        def getBaseExif(timeStamp):
            """Creates Base Exif Info"""

            exif = {}
            exif["Exif"] = {}
            exif["Exif"][36867] = b'%s' % str.encode(timeStamp)
            exif["0th"] = {}
            exif["0th"][34665] = 58
            exif["0th"][306] = b'%s' % str.encode(timeStamp)
            exif["Interop"] = {}
            exif["1st"] = {}
            exif["1st"][513] = 126
            exif["1st"][514] = 0
            exif["thumbnail"] = None
            exif["GPS"] = {}
            return exif

        self.__validateModData(gpsInfo, newFileName)

        gpsDict = {}

        # Open Image and get ExifData
        im = Image.open(self.__filename)

        try:
            exif_dict = load(im.info["exif"])
        # If jpeg has no exif data, make generic exif
        except (KeyError, UnboundLocalError):
            exif_dict = getBaseExif(gpsInfo.timeStamp)

        # Get Coord Data and initialize dictionary
        gpsDict = self.decimal2Degree(gpsInfo.coord)
        gpsDict[5] = 1 if gpsInfo.alt < 0 else 0  # Altitude
        gpsDict[6] = (abs(gpsInfo.alt) * 1000, 1000)  # Altitude
        gpsDict[27] = b'%s' % (b'ASCII\x00\x00\x00GPS')

        # Get Time
        gpsDict[7] = gpsInfo.getGPSFormattedTime()
        gpsDict[29] = b'%s' % gpsInfo.getGPSFormattedDate()

        # Modify Exif Data
        for key in gpsDict:
            exif_dict["GPS"][key] = gpsDict[key]

        # Convert ExifData back and save in new file
        exif_bytes = dump(exif_dict)
        im.save(newFileName, "jpeg", exif=exif_bytes)


def getElevation(coords, apiKey):
    """getElevation(coords, apiKey)

       Returns an int representing the elevation from Google in reference to
       GPS Coordinates. Takes two arguments.

            coord  - tuple or list of two floats representing the decimal
                     coordinates.
            apiKey - str of the Google Api Key
    """

    return GPSInfo(coord=coords, googleApiKey=apiKey).alt


def coord2decimal(coord, quad):
    """coord2decimal(coord, quad)

    Converts Degrees, Minutes and Seconds to decimal.

    Arguments:
        coord - tuple or list consisting of degree, minute, and second or
                degree and minute.
        quad  - str reference of the character 'N','S','E','W'
                representing North, South, East, West. This also specifies
                latitude or longitude"""

    return GPSPhoto().coord2decimal(coord, quad)


def decimal2Degree(coord):
    """decimal2Degree(coord)

    Convert Decimal Coordinates to Degrees, Minutes, Seconds
    and determines Quadrant, takes one argument
        coord - tuple or list of 2 floats

    Returns a dictionary of latitude and longitude"""

    data = GPSPhoto().decimal2Degree(coord)
    gpsData = {}
    gpsData["latitude"] = {}
    gpsData["longitude"] = {}
    gpsData["latitude"]["quad"] = data[1]
    gpsData["longitude"]["quad"] = data[3]
    gpsData["latitude"]["coord"] = (data[2][0][0] / data[2][0][1],
            data[2][1][0] / data[2][1][1],
            float(data[2][2][0]) / float(data[2][2][1]))
    gpsData["longitude"]["coord"] = (data[4][0][0] / data[4][0][1],
            data[4][1][0] / data[4][1][1],
            float(data[4][2][0]) / float(data[4][2][1]))

    return gpsData


def getGPSData(fileName):
    """getGPSData(filename)
    Gets GPS Data from Image, takes one argument
        fileName - str of path/to/image

    There are 3 different types of Longitude and Latitude data stored.
            1 - type is already in decimal format
                Assumption no Ref Value
            2 - type is in degree and minute format
                Assumption [100, 44.5678]
            3 - type is in degree, minute and second
                Assumption [100, 44,95521/5000]
    This function will assume the assumptions are correct and parse the
    strings and return a list of floating elements, takes an parameter of
    list of strings"""

    return GPSPhoto(fileName).getGPSData()


def getRawData(fileName):
    """getRawData(fileName)
    Returns the raw GPS Data returned from ExifRead, takes one argument
        fileName - str of path/to/image"""
    return GPSPhoto(fileName).getRawData()


def stripGPSData(oldFile, newFile):
    '''stripGPSData(oldFile, newFile)

    Strips all exif data from photo and saves to new jpeg, takes two arguments
        oldFile - str of /path/to/image of image to be stripped
        newFile - str of /path/to/image of the new stripped image'''

    GPSPhoto(oldFile).stripData(newFile)

if __name__ == "__main__":
    exit_value = 0

    def printHelp():
        """Prints Help for Command Line Operation

        Return Decimal Coordinates if used in command line
        Call command as follows:
        python gpsphoto.py "/path/to/1st/photo" "/path/to/2nd/photo"
        """
        print(('gpsphoto.py version %d.%d.%d' % (VER[0], VER[1], VER[2])))
        print(('    Reads, modifies, and strips GPS Data from Images.\n' +
                '    outputs to jpeg format.\n'))
        print(('Usage:\n    python gpsphoto.py <options> "/path/to/1st/photo"' +
                ' "/path/to/2nd/photo" ...\n'))
        print(('Options:\n' +
                '    -H - This Help Menu\n' +
                '    -D - Output Raw Data\n' +
                '    -O <image to open> - Opens Image in Google Maps\n' +
                '    -E latitude longitude GoogleApiKey -  returns elevation' +
                '    -S <image to strip> <new image> - Strips GPS Data\n' +
                '    -M <image to modify> <new image> lat=float lon=float \ ' +
                '        alt=int date=YYYY:MM:DD time=HH:MM:SS \ ' +
                '        stamp="YYYY:MM:DD HH:MM:SS" key=<ApiKey>\n' +
                '        alt is optional - will default to 0\n' +
                '        stamp is optional - will default to now\n' +
                '        date is optional - do not use with time, use stamp\n' +
                '        time is optional - do not use with date, use stamp\n' +
                '        key is optional - use if you want auto elevation\n\n'
                'Example:\n' +
                '    python gpsphoto.py -E 35.104860 -106.628915 <some-key>'
                '    python gpsphoto.py -S /path/to/image /path/to/newImage\n' +
                '    python gpsphoto.py -M /path/to/image /path/to/newImage \ '
                + '\n        lat=35.104860 lon=-106.628915 alt=1765 \ ' +
                '  \n        stamp="1989:05:29 06:01:00"\n'))

    def notEnoughArguments():
        """Exit With Not Enough Arguments Error"""

        sys.stderr.write("Error - Not enough arguments\n")
        printHelp()
        sys.exit(1)

    def printData(filename, data):
        """Prints Data Dictionary to STDOUT"""
        if len(list(data.keys())) == 0:
            print(("%s does not contain any GPS Info" % (filename)))
            return 1
        else:
            print(("\n" + filename + ":"))
            for tag in list(data.keys()):
                print(("%s: %s" % (tag, data[tag])))
            return 0

    if len(sys.argv) > 1:
        if sys.argv[1][0] == '-':
            try:
                if sys.argv[1].upper()[1] == 'H':
                    printHelp()
                elif sys.argv[1].upper()[1] == 'D':
                    if len(sys.argv) > 2:
                        for i in range(2, len(sys.argv)):
                            try:
                                data = getRawData(sys.argv[i])
                                exit_value = printData(sys.argv[i], data)
                            except AttributeError:
                                sys.stderr.write("Error - Invalid File %s\n" %
                                        sys.argv[i])
                    else:
                        notEnoughArguments()
                elif sys.argv[1].upper()[1] == 'S':
                    if len(sys.argv) < 4:
                        notEnoughArguments()
                    stripGPSData(sys.argv[2], sys.argv[3])
                elif sys.argv[1].upper()[1] == 'M':
                    if len(sys.argv) < 6:
                        notEnoughArguments()
                    args = sys.argv[4:]
                    coords = [0, 0]
                    alt = 0
                    timeStamp = None
                    key = None
                    for arg in args:
                        lst = arg.split('=')
                        argName = lst[0]
                        val = lst[1]
                        if  argName.find('lat') == 0:
                            coords[0] = float(val)
                        elif  argName.find('lon') == 0:
                            coords[1] = float(val)
                        elif  argName.find('key') >= 0:
                            key = val
                        elif  argName.find('alt') >= 0:
                            alt = int(val)
                        elif  argName.find('time') >= 0:
                            date = datetime.strftime(datetime.now(), "%Y:%m:%d")
                            timeStamp = date + " " + val
                        elif  argName.find('date') >= 0:
                            time = datetime.strftime(datetime.now(), "%H:%M:%S")
                            timeStamp = val + " " + time
                        elif  argName.find('stamp') >= 0:
                            timeStamp = val
                    info = GPSInfo(coords, alt, timeStamp, key)
                    GPSPhoto(sys.argv[2]).modGPSData(info, sys.argv[3])
                elif sys.argv[1].upper()[1] == 'O':
                    if len(sys.argv) < 3:
                        notEnoughArguments()
                    data = getGPSData(sys.argv[2])
                    try:
                        lat = data['Latitude']
                        lon = data['Longitude']
                        url = str("https://www.google.com/maps/place/%f,%f" %
                                (lat, lon))
                        webbrowser.open_new(url)
                    except KeyError as e:
                        sys.stderr.write(str("%s does not contain GPS "
                                + "Data\n") % (sys.argv[2]))
                        sys.exit(1)
                elif sys.argv[1].upper()[1] == 'E':
                    if len(sys.argv) < 5:
                        notEnoughArguments()
                    alt = getElevation((float(sys.argv[2]), float(sys.argv[3])),
                            sys.argv[4])
                    print(("Elevation: %d meters\n" % alt))
                    sys.exit(0)
                else:
                    sys.stderr.write("Error - Invalid Option %s" % sys.argv[1])
                    printHelp()
                    sys.exit(1)
            except KeyError:
                sys.stderr.write("%s Not a jpeg or tiff file format\n" %
                        sys.argv[2])
                sys.exit(1)
            except (InvalidLatitude, InvalidLongitude, OSError, ValueError,
                    IOError) as e:
                sys.stderr.write("\n" + str(e) + "\n")
                sys.exit(1)
            except InvalidApiKey as e:
                sys.stderr.write(e.message)
                sys.exit(1)
            except TypeError as e:
                sys.stderr.write("\nImage %s Contains no GPS Coordinates\n" %
                        (sys.argv[2]))
                sys.exit(1)
        else:
            for i in range(1, len(sys.argv)):
                try:
                    data = getGPSData(sys.argv[i])
                    exit_value = printData(sys.argv[i], data)
                except AttributeError:
                    sys.stderr.write("Error - Invalid File %s\n" % sys.argv[i])
    else:
        notEnoughArguments()
    sys.exit(exit_value)
