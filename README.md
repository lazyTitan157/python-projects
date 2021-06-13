# Python Toy Project 

## 1. Text Sentiment Analysis by Python
    
### [Data source]
1. [Twitter API 발급받기-Student Type](https://blog.naver.com/2983rgt/222356513854)


### [Logic]
```
- Twitter API를 통해 특정인의 트윗들을 가져와서, 감정분석(알고리즘 미정)
 - 감정분석을 위해 자연어 처리 파이썬 패키지 NLTK 활용
 - Twitter Streaming API 사용
- 업비트 API를 통해 비트코인 시세정보 가져오기
- 비트코인과 트위터 시간 scope를 맞추고, 상관관계 분석하여 가장 관련성이 높은 변인 찾기
```


```참고```   
[Twitter Sentiment Analysis by Python -1-](https://medium.com/@whj2013123218/twitter-sentiment-analysis-by-python-1-a06b05d13465)   
[twitter api 사용하기](https://blog.naver.com/2983rgt/222356513854)


## 2. Correlation Analysis between Currency and BTC Market by Python
### [Data source]
1. 일별 환율정보 가져오기: [한국은행경제통계시스템에서 CSV로 다운로드](http://ecos.bok.or.kr/flex/EasySearch.jsp?langGubun=K&topCode=022Y013#)
2. 일별 비트코인 시세정보 가져오기   
2.1. [REST API를 이용한 업비트 시세 수신 방법](https://docs.upbit.com/docs/upbit-quotation-restful-api)   
2.2. [QUOTATION API: 시세조회-일캔들](https://docs.upbit.com/reference#%EC%9D%BCday-%EC%BA%94%EB%93%A4-1)   
2.3. 환율정보와 같은 scope로 시세정보 저장(.csv)      
*(참고) [업비트 개발자 센터](https://docs.upbit.com/)에서 API Key 발급: API를 통한 거래시 필요, 시세조회만 하는 경우는 불필요.
```
url = "https://api.upbit.com/v1/candles/days"
querystring = {"market":"KRW-BTC","count":"1000"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
# Upbit API response data parse to csv file
```
### [Logic]
```
두 개의 csv 파일을 가지고 상관분석(모델:)
```
