from PIL import Image
import re
import webbrowser
import pikepdf
import datetime
import pycountry
from exif import Image
import reverse_geocoder as rg

from dateutil.tz import tzutc, tzoffset
from module.utils import COLORS


# extract EXIF data


def metaexit(filename):
    with open(f"{filename}", "rb") as palm_1_file:
        palm_1_image = Image(palm_1_file)

    images = [palm_1_image]

    image_members = []

    for image in images:
        image_members.append(dir(image))

    for index, image in enumerate(images):
        print(f" {COLORS.WHSL}Объектив и ОС — изображение{COLORS.GNSL} {index}")
        print(f" {COLORS.REDL}---------------------{COLORS.GNSL}")
        print(f" {COLORS.WHSL}Марка объектива:{COLORS.GNSL} {image.get('lens_make', 'Unknown')}")
        print(f" {COLORS.WHSL}Модель объектива:{COLORS.GNSL} {image.get('lens_model', 'Unknown')}")
        print(f" {COLORS.WHSL}Спецификация объектива:{COLORS.GNSL} {image.get('lens_specification', 'Unknown')}")
        print(f" {COLORS.WHSL}Версия OS:{COLORS.GNSL} {image.get('software', 'Unknown')}\n")

    for index, image in enumerate(images):
        print(f" Дата/время съемки - Изображение {index}")
        print(f" {COLORS.REDL}-------------------------{COLORS.WHSL}")
        print(f"{image.datetime_original}.{image.subsec_time_original} {image.get('offset_time', '')}\n")

    def format_dms_coordinates(coordinates):
        return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""

    def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
        decimal_degrees = coordinates[0] + \
                          coordinates[1] / 60 + \
                          coordinates[2] / 3600

        if coordinates_ref == "S" or coordinates_ref == "W":
            decimal_degrees = -decimal_degrees

        return decimal_degrees

    for index, image in enumerate(images):
        print(f" Координаты — изображение {index}")
        print("---------------------")
        print(f" Широта (DMS): {format_dms_coordinates(image.gps_latitude)} {image.gps_latitude_ref}")
        print(f" Долгота (DMS): {format_dms_coordinates(image.gps_longitude)} {image.gps_longitude_ref}\n")
        print(f" Широта (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
        print(f" Долгота (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n")

    def degrees_to_direction(degrees):
        COMPASS_DIRECTIONS = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW"
        ]

        compass_directions_count = len(COMPASS_DIRECTIONS)
        compass_direction_arc = 360 / compass_directions_count
        return COMPASS_DIRECTIONS[int(degrees / compass_direction_arc) % compass_directions_count]

    def format_direction_ref(direction_ref):
        direction_ref_text = "(истинный или магнитный север не указан)"
        if direction_ref == "T":
            direction_ref_text = " Истинный север"
        elif direction_ref == "M":
            direction_ref_text = " Магнитный север"
        return direction_ref_text

    # Import images
    lake_images = []

    # Display camera direction for each image
    for index, image in enumerate(lake_images):
        print(f" Направление изображения - Изображение {index}")
        print(f" -------------------------")
        print(f" Направление изображения: {degrees_to_direction(image.gps_img_direction)} ({image.gps_img_direction}°)")
        print(f" Ссылка направления изображения: {format_direction_ref(image.gps_img_direction_ref)}\n")

    def format_altitude(altitude, altitude_ref):
        altitude_ref_text = " (выше или ниже уровня моря не указано)"
        if altitude_ref == 0:
            altitude_ref_text = " Над уровнем моря"
        elif altitude_ref == 1:
            altitude_ref_text = " Ниже уровня моря"
        return f"{altitude}meters {altitude_ref_text}"

    # Import images
    altitude_images = []
    for i in range(1, 3):
        with open(f"{filename}", "rb") as current_file:
            altitude_images.append(Image(current_file))

    # Display camera altitude for each image
    for index, image in enumerate(altitude_images):
        print(f" {COLORS.FIOL}Высота уровня моря {index}")
        print(f" ------------------")
        print(f" {format_altitude(image.gps_altitude, image.gps_altitude_ref)}\n")

    def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
        decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
        decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
        openWeb = input(f"\n {COLORS.REDL}Открыть GPS координаты в браузере? y/n:{COLORS.REDL} ")
        if openWeb == 'y':
            url = f"https://earth.google.com/web/search/{decimal_latitude},{decimal_longitude}"
            webbrowser.open(url)

        elif openWeb == 'n':
            print(f'\n Надеюсь мы смогли вам помочь !!! \n')
            return

    for index, image in enumerate(images):
        draw_map_for_location(image.gps_latitude,
                              image.gps_latitude_ref,
                              image.gps_longitude,
                              image.gps_longitude_ref)

    for index, image in enumerate(images):
        print(f" {COLORS.WHSL}Дополнительная информация по местоположению")
        print(f" {COLORS.REDL}-----------------------{COLORS.WHSL}")
        decimal_latitude = dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)
        decimal_longitude = dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)
        coordinates = (decimal_latitude, decimal_longitude)
        location_info = rg.search(coordinates)[0]
        location_info['country'] = pycountry.countries.get(alpha_2=location_info['cc'])
        print(f"{location_info}\n")


# /home/apashe/Desktop/puzi.jpg  Проверка фото

# /home/apashe/Desktop/puk.pdf Проверка pdf


def pdf(pdf_filename):
    def transform_date(date_str):
        """
        Convert a pdf date such as "D:20120321183444+07'00'" into a usable datetime
        http://www.verypdf.com/pdfinfoeditor/pdf-date-format.htm
        (D:YYYYMMDDHHmmSSOHH'mm')
        :param date_str: pdf date string
        :return: datetime object
        """
        pdf_date_pattern = re.compile(''.join([
            r"(D:)?",
            r"(?P<year>\d\d\d\d)",
            r"(?P<month>\d\d)",
            r"(?P<day>\d\d)",
            r"(?P<hour>\d\d)",
            r"(?P<minute>\d\d)",
            r"(?P<second>\d\d)",
            r"(?P<tz_offset>[+-zZ])?",
            r"(?P<tz_hour>\d\d)?",
            r"'?(?P<tz_minute>\d\d)?'?"]))

        match = re.match(pdf_date_pattern, date_str)
        if match:
            date_info = match.groupdict()

            for k, v in date_info.items():  # transform values
                if v is None:
                    pass
                elif k == 'tz_offset':
                    date_info[k] = v.lower()  # so we can treat Z as z
                else:
                    date_info[k] = int(v)

            if date_info['tz_offset'] in ('z', None):  # UTC
                date_info['tzinfo'] = tzutc()
            else:
                multiplier = 1 if date_info['tz_offset'] == '+' else -1
                date_info['tzinfo'] = tzoffset(None,
                                               multiplier * (3600 * date_info['tz_hour'] + 60 * date_info['tz_minute']))

            for k in ('tz_offset', 'tz_hour', 'tz_minute'):  # no longer needed
                del date_info[k]

            return datetime.datetime(**date_info)

    # read the pdf file
    pdf = pikepdf.Pdf.open(pdf_filename)
    docinfo = pdf.docinfo
    for key, value in docinfo.items():
        if str(value).startswith("D:"):
            # pdf datetime format, convert to python datetime
            value = transform_date(str(pdf.docinfo["/CreationDate"]))
        print(key, ":", value)
