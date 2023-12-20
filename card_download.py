
from downloader import *
#收藏集id
#id = 113

id = input('收藏集id：')

info_url = 'https://api.bilibili.com/x/vas/dlc_act/act/basic?act_id=' + str(id)
item_url = 'https://api.bilibili.com/x/vas/dlc_act/act/item/list?act_id=' + \
    str(id)

# download(info_url)
info = parse(get_json(info_url))
item = parse(get_json(item_url))

card_if_exist(info)

title = info['data']['act_title']

card_create_dir(title)

download_card(title, item)
