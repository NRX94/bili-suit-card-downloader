## bili-suit-card-downloader

通过b站的api接口，实现装扮和收藏集的下载。

### 查找

运行`search.py`，输入关键字，可查找装扮/收藏集的商品id。

对于收藏集，也可在`card_list.json`中搜索名称，直接查找`act_id`。

运行`update_card_list.py`更新`card_list.json`列表。

### 下载装扮

下载装扮：运行`suit_download.py`并输入商品id下载。

下载装扮：运行`card_download.py`并输入商品id下载。

### API

+ 收藏集目录
https://api.bilibili.com/x/garb/card/subject/list?subject_id=42

+ 收藏集数据
https://api.bilibili.com/x/vas/dlc_act/act/item/list?act_id=161

+ 收藏集销售界面
https://api.bilibili.com/x/vas/dlc_act/act/basic?act_id=100

+ 装扮搜索
https://api.bilibili.com/x/garb/v2/mall/home/search?key_word=%E8%96%87

+ 装扮数据
https://api.bilibili.com/x/garb/v2/mall/suit/detail?from=&from_id=&item_id={装扮id}&part=suit

+ 直播间表情
https://api.live.bilibili.com/xlive/web-ucenter/v2/emoticon/GetEmoticons?platform=pc&room_id=5424

