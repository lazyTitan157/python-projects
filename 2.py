import requests
import json
from openpyxl import Workbook

url = "https://api.upbit.com/v1/candles/days"
headers = {"Accept": "application/json"}
to = "2021-05-25T00:00:00Z"

# 요청 횟수 제한 주의하기 (https://docs.upbit.com/docs/user-request-guide#quotation-api)
# 최신순으로 데이터 저장
for i in range(0, 6):
    querystring = {"market":"KRW-BTC","to":to, "count":"200"} # count max = 200
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == requests.codes.ok:
        print("API Response Status code: ok")
        response_native = json.loads(response.text)

        
        write_wb = Workbook()
        write_ws = write_wb.create_sheet('KRW-BTC')
        write_ws = write_wb.active
        
        for index, item in enumerate(response_native):
            if index == len(response_native)-1:
                to = item.get('candle_date_time_kst')+'Z'
                print(to)

            # data add
            write_ws.cell(1, index+1, item.get('candle_date_time_kst'))
            write_ws.cell(2, index+1, item.get('trade_price'))

            # file save
            write_wb.save("C:/projects/toyproject/kaist/KRW-BTC_",,".xlsx")            
        

print("end")
