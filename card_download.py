from downloader import *

import json
import requests
import os

id = 113
info_url='https://api.bilibili.com/x/vas/dlc_act/act/basic?act_id=' + str(id)

item_url='https://api.bilibili.com/x/vas/dlc_act/act/item/list?act_id=' + str(id)
#
#with open('item.json', 'w', encoding='utf-8') as f:
#    json.dump(requests.get(item_url).json(), f, indent=4, ensure_ascii=False)


'''
def download(name, url):
    r = requests.get(url)
    r.raise_for_status()
    with open(name, 'wb') as f:
        f.write(r.content)'''





def download(item):
    

    for card in item['data']['item_list']:
        name = card['card_item']['card_name']
        img_url = card['card_item']['card_img']
        try:
            video_url = card['card_item']['video_list'][0]
        except:
            video_url = -1
        print(name, img_url, video_url)

        img_name = name + '.png'
        response = requests.get(img_url)
        image_path = os.path.join(title, img_name)
        with open(image_path, 'wb') as f:
            f.write(response.content)
            
        if video_url != -1:
            headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }
            video_name = name + '.mp4'
            response = requests.get(video_url,headers=headers, stream=True)
            video_path = os.path.join(os.path.join(title,'视频'), video_name)
            #下载video_url中的视频
            with open(video_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                f.close()

#download(info_url)
info = parse(get_json(info_url))
item = parse(get_json(item_url))

card_if_exist(info)

title = info['data']['act_title']

card_create_dir(title)

download_card(title,item)