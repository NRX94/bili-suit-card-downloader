from downloader import *


while (True):
    # 收藏集id
    # id = 113
    print('输入0退出')
    id = input('收藏集id：')

    if id == '0':
        exit()

    info_url = 'https://api.bilibili.com/x/vas/dlc_act/act/basic?act_id=' + \
        str(id)
    item_url = 'https://api.bilibili.com/x/vas/dlc_act/act/item/list?act_id=' + \
        str(id)

    # download(info_url)
    info = parse(get_json(info_url))
    item = parse(get_json(item_url))

    # card_if_exist(info)
    if card_if_exist(info) == False:
        continue

    title = info['data']['act_title']

    card_create_dir(title)

    download_card(title, item)
