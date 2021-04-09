#!/usr/bin/env python3
import asyncio
import logging
import maigret
WHSL = C = "\033[32;1m"
ENDL = W = "\033[0m"
REDL = R = "\033[0;31m"
GNSL = G = "\033[1;34m"

O = "\033[45m"


# top popular sites from the Maigret database
TOP_SITES_COUNT = 300
# Maigret HTTP requests timeout
TIMEOUT = 10
# max parallel requests
MAX_CONNECTIONS = 50


if __name__ == '__main__':
    # setup logging and asyncio
    logger = logging.getLogger('maigret')
    logger.setLevel(logging.WARNING)
    loop = asyncio.get_event_loop()

    # setup Maigret
    db = maigret.MaigretDatabase().load_from_file('./maigret/resources/data.json')
    # also can be downloaded from web
    # db = MaigretDatabase().load_from_url(MAIGRET_DB_URL)

    # user input
    username = input(f' {R}──>{C} Введите имя пользователя для поиска:{W} ')

    sites_count_raw = input(f'\n {R}──>{C} Выберите количество сайтов для поиска {W}({TOP_SITES_COUNT} for default, {len(db.sites_dict)} max): ')
    sites_count = int(sites_count_raw) or TOP_SITES_COUNT

    sites = db.ranked_sites_dict(top=sites_count)

    show_progressbar_raw = input(f'\n {R}──>{C} Показать индикатор выполнения ? [Yn]{W} ')
    show_progressbar = show_progressbar_raw.lower() != 'n' 

    extract_info_raw = input(f'\n {R}──>{C} Хотите извлечь дополнительную информацию из аккаунтов?\' pages ? [Yn]{W} ')
    extract_info = extract_info_raw.lower() != 'n' 

    use_notifier_raw = input(f'\n {R}──>{C} Вы хотите использовать уведомление для отображения результатов при поиске ? [Yn]{W} ')
    print("")
    use_notifier = use_notifier_raw.lower() != 'n'

    notifier = None
    if use_notifier:
        notifier = maigret.Notifier(print_found_only=True, skip_check_errors=True)

    # search!
    search_func = maigret.search(username=username,
                                 site_dict=sites,
                                 timeout=TIMEOUT,
                                 logger=logger,
                                 max_connections=MAX_CONNECTIONS,
                                 query_notify=notifier,
                                 no_progressbar=(not show_progressbar),
                                 is_parsing_enabled=extract_info,
                                 )

    results = loop.run_until_complete(search_func)

    input(f' {R}──>{C} Поиск завершен. Нажмите любую клавишу, чтобы показать результаты.')

    for sitename, data in results.items():
        is_found = data['status'].is_found()
        print(f'{sitename} - {"Найден!" if is_found else "Не найден"}')
