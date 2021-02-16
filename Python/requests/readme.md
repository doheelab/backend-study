
## 0. 기본적인 사용 방법

```
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
import requests URL = 'http://www.tistory.com' 
response = requests.get(URL, headers=headers) 
```

## 1. GET 요청할 때 parameter 전달법

* dictionary 사용하기

```
params = {'param1': 'value1', 'param2': 'value2'} 
res = requests.get(URL, params=params)
```

* 직접 파라미터 넣어서 보내기

```
res = requests.get(URL+"?param1=value1&param2=value2")
```


## 2. POST 요청할 때 data 전달법

```
data = {'param1': 'value1', 'param2': 'value2'} 
res = requests.post(URL, data=json.dumps(data), auth=("id", "pass"))
``` 

그리고 전달 받기

```
json.loads(request.get_data(), encoding="utf-8")
```


## 3. 헤더 추가, 쿠키 추가
```
headers = {'Content-Type': 'application/json; charset=utf-8'} 
cookies = {'session_id': 'sorryidontcare'} 
res = requests.get(URL, headers=headers, cookies=cookies)
```


## Reference

https://dgkim5360.tistory.com/entry/python-requests