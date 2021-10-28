# Bafomet developer
# osint-san

import requests
from module.utils.bear_system import searchGoogle
from module.utils import COLORS


def google(nom):
    print(f" {COLORS.GNSL} Ваш поисковой запрос отфильтрован {COLORS.REDL}системой Медведь.\n")
    print(f" \n  Найдено в настоящее время:\n")
    url = "https://www.google.com/search?num=30&q=\\%s\\"
    try:
        nom2 = nom.split(" ")
        nom = nom2[0] + '+' + nom2[1]
    except:
        pass
    requete = requests.get(url % (nom))
    searchGoogle(requete=requete)
