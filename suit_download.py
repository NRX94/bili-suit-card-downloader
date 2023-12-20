from downloader import *

while(True):
    # 装扮id
    #id = 114514
    #输入装扮的id
    print('输入0退出')
    id = input('装扮id：')
    
    if id == '0':
        exit()

    info_url = 'https://api.bilibili.com/x/garb/v2/mall/suit/detail?from=&from_id=&item_id=' + \
        str(id)

    info = parse(get_json(info_url))
    
    if suit_if_exist(info)==False:
        continue

    title = info['data']['name']

    suit_create_dir(title)

    save_json(title, info_url)

    download_bg(title, info)

    download_emoji(title, info)
