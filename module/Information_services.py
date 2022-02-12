# Developer by Bafomёd
from module.utils.ban import page_26
from module.utils import COLORS
from module.utils import information_services_data
from core.core import clear_screen
from core.core import show_banner

option_to_page = {
    1: information_services_data.page_nicknames_2,
    2: information_services_data.page_mail,
    3: information_services_data.page_numbers,
    4: information_services_data.page_maps,
    5: information_services_data.page_telegram_osint,
    6: information_services_data.page_br_gov,
    7: information_services_data.page_millitary,
    8: information_services_data.page_ru_gov,
    9: information_services_data.page_equipment,
    10: information_services_data.page_social_osint,
    11: information_services_data.page_sun_geolocation,
    12: information_services_data.page_deanon_face,
    13: information_services_data.page_instagram_osint,
    14: information_services_data.page_offenosint,
    15: information_services_data.page_vk_osint,
    16: information_services_data.page_restore,
    17: information_services_data.page_ip,
    18: information_services_data.page_browsers,
    19: information_services_data.page_fio,
    20: information_services_data.page_resources,
    21: information_services_data.page_shodan,
    22: information_services_data.page_restokz,
    23: information_services_data.page_aresti,
    24: information_services_data.page_uzbusa,
    25: information_services_data.page_scam_and_spam_nomber,
    26: information_services_data.page_reddit,
    27: information_services_data.page_facebook,
    28: information_services_data.page_suite_searche,
    29: information_services_data.page_system_claster,
    30: information_services_data.page_searche_system,
    31: information_services_data.page_msearche_system,
    32: information_services_data.page_twitter,
    33: information_services_data.page_doc_searche,
    34: information_services_data.page_flight_tracking,
    35: information_services_data.page_cryptocurrency_investigations,
    36: information_services_data.page_auto_searche,
    37: information_services_data.page_marine_cargo_tracking,
    38: information_services_data.page_forum,
    39: information_services_data.page_classifieds,
    40: information_services_data.page_countrycrt,
    41: information_services_data.page_maps1,
    42: information_services_data.page_admru,
    43: information_services_data.page_airport,
    44: information_services_data.page_kirgizia,
    45: information_services_data.page_polsha,
    46: information_services_data.page_mogilki,
    47: information_services_data.page_data_publuck,
    48: information_services_data.page_data_bots_telegram,
    49: information_services_data.page_data_carding,

}


def show_page(page):
    while True:
        clear_screen()
        print(information_services_data.banner)
        print(page)
        print(information_services_data.banner_end)

        try:
            option = input(f"{COLORS.REDL}  └──>{COLORS.ENDL} Введите опцию: {COLORS.ENDL}")
        except KeyboardInterrupt:
            break

        if option == "99":
            break


def information_menu():
    while True:
        clear_screen()
        print(page_26)
        try:
            option = input(f"{COLORS.REDL}  └──>{COLORS.ENDL} Введите опцию:{COLORS.ENDL} ")
        except KeyboardInterrupt:
            return

        try:
            page = int(option)
        except ValueError:
            continue

        if page == 99:
            show_banner(clear=True)
            return

        else:
            page = option_to_page.get(page)
            if page:
                show_page(page)


if __name__ == '__main__':
    information_menu()
