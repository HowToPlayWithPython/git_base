import requests
import re
import json


base_url = 'https://www.anruan.com/'
main_url = 'https://www.anruan.com/rjxz/list_5_1_1_1.html'
main_page = requests.get(main_url).text
url_list = re.findall('<a href="(.*?)"   >(.*?)<i></i></a>', main_page)


def main():
    save_path = './data/'
    for tup in url_list:
        app_type_name = tup[1]
        print(app_type_name)
        with open(save_path + app_type_name, 'w', encoding='utf-8') as saver:
            app_type_page_url = tup[0]
            this_page_url = base_url + app_type_page_url
            while True:
                this_page = requests.get(this_page_url).text
                app_name_list = re.findall('<a href="https://.*?" target="_blank" class="name">(.*?)</a>', this_page)
                print(app_name_list)
                for item in app_name_list:
                    saver.write(item + '\n')
                next_page_url = re.findall("<a href='([^<]*?)' class='next'>下一页</a>", this_page)
                if not next_page_url:
                    break
                this_page_url = base_url + next_page_url[0]


if __name__ == '__main__':
    main()
























