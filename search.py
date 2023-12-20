from downloader import *

while (True):
    # search='薇steria'
    print('输入0退出')
    search = input('搜索：')

    if search == '0':
        exit()

    url = 'https://api.bilibili.com/x/garb/v2/mall/home/search?key_word='+search

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }

    info = parse(get_json(url))

    if info['data']['list'] == []:
        print('没有找到相关商品')
    else:

        for i in info['data']['list']:
            if i['part_id'] == 6:
                print('装扮')
                print(i['name'])
                print(i['item_id'])
                print('----------------------')
            if i['part_id'] == 0:
                print('收藏集')
                print(i['name'])
                print(i['properties']['dlc_act_id'])
                print('----------------------')
