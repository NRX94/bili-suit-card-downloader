import json
import requests

card_list_url = 'https://api.bilibili.com/x/garb/card/subject/list?subject_id=42'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}

with open('card_list.json', 'w', encoding='utf-8') as f:
    json.dump(requests.get(card_list_url, headers=headers).json(),
              f, indent=4, ensure_ascii=False)
