# site_framework_demo

## 使用說明

```
pip install -r requirements.txt
python manage.py migrate
```

## 使用 ngrok 來模擬

```
ngrok http 8000
```

在這個步驟會取得一個網址，請記住其中的 domain，後面在新增 site 時會用到。

## 新增 site

執行 `python manage.py shell`
```
from django.contrib.sites.models import Site
Site.objects.create(domain='xxxxx.ngrok.io', name='ngrok')  # 填入前個步驟取得的 domain
Site.objects.create(domain='localhost', name='localhost')
```

## 執行

```
export ALLOWED_HOSTS=xxxxx.ngrok.io
python manage.py runserver 127.0.0.1:8000
```

## 測試

打開瀏覽器，輸入 https://xxxxx.ngrok.io/blog/ ，再開啟另外一個頁籤，輸入 http://localhost:8000/blog/
你會發現一個是可以看到頁面的，另外一個則是看到 Not allowed
