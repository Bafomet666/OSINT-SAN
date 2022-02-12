
import asyncio
import logging
import maigret

WHSL = C = "\033[39m"
ENDL = W = "\033[0m"
REDL = R = "\033[0;31m"
FIOL = H = "\033[95m"

# top popular sites from the Maigret database
TOP_SITES_COUNT = 300
# Maigret HTTP requests timeout
TIMEOUT = 10
# max parallel requests
MAX_CONNECTIONS = 50


def userfull(username):
    # setup logging and asyncio
    logger = logging.getLogger('maigret')
    logger.setLevel(logging.WARNING)
    loop = asyncio.get_event_loop()

    # setup Maigret
    db = maigret.MaigretDatabase().load_from_file('./module/maigret/resources/data.json')
    # also can be downloaded from web
    # db = MaigretDatabase().load_from_url(MAIGRET_DB_URL)

    # user input
    print('')
    print(f'{FIOL} Дата обновления базы данных 20.01.2022')
    print(f'{WHSL} Советую вписать:{REDL} 2500')
    print(f'{WHSL} Осущесвляется максимальный поиск со всеми аргументами кроме выгрузки данных в формат pdf')
    sites_count_raw = input(f'\n {WHSL}Выберите количество сайтов для поиска {FIOL}({TOP_SITES_COUNT} for default, {len(db.sites_dict)} max):{REDL} ')
    sites_count = int(sites_count_raw) or TOP_SITES_COUNT

    sites = db.ranked_sites_dict(top=sites_count)

    show_progressbar_raw = W
    show_progressbar = show_progressbar_raw

    extract_info_raw = W
    extract_info = extract_info_raw

    use_notifier_raw = W
    print("")
    use_notifier = use_notifier_raw

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

    input(f'\n {REDL}Поиск завершен. Нажмите любую клавишу, чтобы показать результаты.{WHSL}\n')

    for sitename, data in results.items():
        is_found = data['status'].is_found()
        print(f'{sitename} - {"Найден!" if is_found else "Не найден"}')
