from core.menu import Menu
from core.plugin import plugin_PRO
from core.utils import console

POST_OPTION_BANNER = f"""
{console.red("└──>")}  {console.green("Обратно в OSINT Menu....")} {console.blue("[")} {console.red("99")} {console.blue("]")}
{console.red("└──>")}  {console.green("Очистить... ")} {console.blue("[")} {console.red("66")} {console.blue("]")}
"""


second_page_menu = Menu(
    name="Вторая страница",
    description="",
    post_option_banner=POST_OPTION_BANNER,
)

second_page_menu.new_options(
    runners=[plugin_PRO]*45,
)

if __name__ == '__main__':
    second_page_menu.run()
