import json
import requests

card_list_url = 'https://api.bilibili.com/x/garb/card/subject/list?subject_id=42'


with open('card_list.json', 'w', encoding='utf-8') as f:
    json.dump(requests.get(card_list_url).json(),
              f, indent=4, ensure_ascii=False)
