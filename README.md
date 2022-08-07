# create_UserAgent
随机创建一个UserAgent，避免大量爬取时服务器拒绝

## 导入

    from create_UserAgent import random_UserAgent

## 使用方法
### 伪装成chrome浏览器

    response = requests.get(url=url, headers=random_UserAgent())


### 伪装成Edge浏览器

    response = requests.get(url=url, headers=random_UserAgent(edge=True))

## 返回的内容举例
直接返回一个字典

    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 Safari/537.36 Edg/103.0.1264.49'}
