from downloader import *

# 装扮的id
#id = 114514
#输入装扮的id
id = input('装扮id：')

info_url = 'https://api.bilibili.com/x/garb/v2/mall/suit/detail?from=&from_id=&item_id=' + \
    str(id)

info = parse(get_json(info_url))
suit_if_exist(info)

title = info['data']['name']

suit_create_dir(title)

save_json(title, info_url)
download_bg(title, info)
download_emoji(title, info)
