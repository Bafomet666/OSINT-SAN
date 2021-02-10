import webbrowser
from PIL import Image
from PIL.ExifTags import *


def get_exif(fn):
    print('[ + ]' + 'Проверка Metadata...' + '\n')
    try:
        i = Image.open(fn)
    except IOError:
        print("Error: Файл не найден")
        return -1

    info = i._getexif()
    if not info:
        print("Метаданные не очень информативны:")
        return -1

    ret = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value

    return ret


def gps_analyzer(img_path):
    exif_data = get_exif(img_path)

    if exif_data == -1:
        return

    for x, y in exif_data.items():
        print(f"{x} : {y}")

    gps_info = exif_data.get("GPSInfo")

    if gps_info:
        lat = [float(x) / float(y) for x, y in gps_info[2]]
        latref = gps_info[1]

        lon = [float(x) / float(y) for x, y in gps_info[4]]
        lonref = gps_info[3]

        lat = lat[0] + lat[1] / 60 + lat[2] / 3600
        lon = lon[0] + lon[1] / 60 + lon[2] / 3600
        if latref == 'S':
            lat = -lat
        if lonref == 'W':
            lon = -lon

        map_it(lat, lon)

    else:
        print('')
        print("GPS локация не найдена")


def map_it(lat, lon):
    # Prints latitude and longitude values
    print()
    print(f"Accurate Latitude  : {lat}")
    print(f"Accurate Longitude : {lon}")
    print()
    # Prompts the user to launch a web browser with the map
    query = f"{lat},+{lon}"
    maps_url = f"https://maps.google.com/maps?q={query}"

    openWeb = input("Open GPS location in web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)
