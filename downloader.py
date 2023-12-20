import json
import requests
from os import mkdir
from os.path import join,isdir,exists


def save_json(title, url):
    name=title+'.json'
    with open(join(title,name), 'w', encoding='utf-8') as f:
        json.dump(requests.get(url).json(), f, indent=4, ensure_ascii=False)   

def get_json(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parse(text):
    json_data = json.loads(text)
    return json_data

def suit_create_dir(name):
    if not exists(name):
        mkdir(name)
    if not isdir(join(name, '表情包')):
        mkdir(join(name, '表情包'))
    if not isdir(join(name, '背景')):
        mkdir(join(name, '背景'))

def card_create_dir(name):
    if not exists(name):
        mkdir(name)
    if not isdir(join(name, '视频')):
        mkdir(join(name, '视频'))


def suit_if_exist(info):
    if info['data']['suit_items'] == None:
        print('装扮不存在')
        #终止程序
        #exit()
        return False
        

def card_if_exist(info):
    if info['message'] != '0':
        print('活动不存在')
        #终止程序
        #exit()
        return False
        


def download_card(title,item):
    

    for card in item['data']['item_list']:
        name = card['card_item']['card_name']
        img_url = card['card_item']['card_img']
        try:
            video_url = card['card_item']['video_list'][0]
        except:
            video_url = -1
        print(name, img_url, video_url)

        #img_name = name + '.png'
        image_path = title
        download_file(name,img_url,image_path)
            
        if video_url != -1:
            #video_name = name + '.mp4'
            video_path = join(title,'视频')
            #下载video_url中的视频
            download_file(name,video_url,video_path)


def download_bg(title,info):
    for i in info['data']['suit_items']['space_bg'][0]['properties']:
        if 'image' in i:
                print(i,info['data']['suit_items']['space_bg'][0]['properties'][i])
                name = i
                img_url = info['data']['suit_items']['space_bg'][0]['properties'][i]
                image_path = join(title,'背景')
                download_file(name,img_url,image_path)

        
def download_emoji(title,info):
    for image in info['data']['suit_items']['emoji_package'][0]['items']:
        print(image['name'][1:-1], image ['properties']['image'])
        name = image['name'][1:-1]
        img_url = image['properties']['image']
        image_path = join(title,'表情包')
        download_file(name,img_url,image_path)
        
def download_file(name,url,path):
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }
    response = requests.get(url,headers=headers)
    if 'mp4' in url:
        video_name = name + '.mp4'

        video_path = join(path, video_name)
        print('downloading:'+video_path)
        with open(video_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                f.close()

    else:    
        if 'jpg' in url:
            img_name = name + '.jpg'
        if 'png' in url:
            img_name = name + '.png'
        
        image_path = join(path, img_name)
        print('downloading:'+image_path)
        with open(image_path, 'wb') as f:
            f.write(response.content)