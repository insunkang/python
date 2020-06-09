import requests
from pprint import pprint
key = 'AIzaSyAotq43lwSEgjQH4JNlaVLjX0_ryzzkYMA'

#string interpolation
search = input("검색어를 입력해 주세요 : ")
q = f'q={search}'
my_type = f'type=video'
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20'
print(url)
response = requests.get(url)
datas = response.json()
#print(data)
# 채널명, 영상 제목
for data in datas['items'][:10]:
    print(data['snippet']['title'], end='  ')
    print(data['snippet']['channelTitle'])