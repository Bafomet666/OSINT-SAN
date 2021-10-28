#!/usr/bin/python
# -*- coding: utf-8 -*-
from module.utils import COLORS
from osintsan import shodan_api_key
from module.utils.ban import page_25
import shodan
import time
import datetime
import os


def showdam():
    def logger(data:str, log_file):
        file = open("module/db/" + log_file, "a", encoding="utf-8")
        file.write(data)
        file.close()

    os.system('clear')
    print(page_25)
    try:
        api = shodan.Shodan(shodan_api_key)
        counter = 1

        b00m = input(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Введите ключевой запрос поиска: ")
        limit = int(input(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Укажите лимит вывода данных от 5 до 500:{COLORS.WHSL} "))
        data_start = input(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Выполнить сохранение результата в файле со своим именем? y/n:{COLORS.WHSL} ").strip()

        if data_start.startswith("y" or "Y"):
            log_file = input(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Дайте название файлу: {COLORS.WHSL}") + '.txt'
            print("")
            print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Данные будут сохранены в файл: OSINT-SAN /module/db/{log_file}")
            print(f"\n" + "  " + "»" * 85 + "\n")
        else:
            log_file = b00m.strip() + '--' + datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S") + '.txt'
            print(f"\n {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Данные будут сохранены в файл: OSINT-SAN /module/db/{log_file} !!! \n")
            print(f"\n" + "  " + "»" * 85 + "\n")

        print("")
        counter = counter + 1
        resalt = api.search_cursor(b00m)
        # print(list(resalt))
        try:
            if next(resalt):
                pass
            for banner in resalt:
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}IP address  :{COLORS.GNSL}  " + (banner["ip_str"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Порт        :{COLORS.GNSL}  " + str(banner["port"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Организация :{COLORS.GNSL}  " + str(banner["org"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Геолокация  :{COLORS.GNSL}  " + str(banner["location"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Layer       :{COLORS.GNSL}  " + (banner["transport"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Domains     :{COLORS.GNSL}  " + str(banner["domains"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Hostnames   :{COLORS.GNSL}  " + str(banner["hostnames"]))
                print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Результат № :  %s. Search query: %s" % (str(counter), str(b00m)))

                data = ("\nIP: " + banner["ip_str"]) + ("\nPort: " + str(banner["port"])) + (
                            "\nOrganisation: " + str(banner["org"])) + ("\nLocation: " + str(banner["location"])) + (
                                   "\nLayer: " + banner["transport"]) + ("\nDomains: " + str(banner["domains"])) + (
                                   "\nHostnames: " + str(banner["hostnames"])) + ("\nData\n" + banner["data"])

                logger(data, log_file)
                time.sleep(0.1)
                print("\n" + " " + f"{COLORS.REDL}»" * 85 + "\n")


                counter += 1
                if counter >= limit:
                    print(f' {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Выполнено\n')
                    exit()


        except:
            print(f' {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Благорим за использование ...\n')
            print(f' Откройте txt документ в module/db там расширенная информация по вашему запросу.')
            exit()


    except KeyboardInterrupt:
        print("\n")
        print(" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Выполняем обратный переход")
        time.sleep(0.5)

    except shodan.APIError as oeps:
        print(f" {COLORS.GNSL}[ {COLORS.REDL}+ {COLORS.GNSL}] {COLORS.WHSL}Суточные лимиты ключа привышены, попробуйте завтра.")


# =====# Main #===== #
# bafomet
if __name__ == "__main__":
    showdam()
