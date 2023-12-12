### 웹 크롤링을 이용한 맛집 리스트 만들기
----
#### 프로젝트 목적
- 데이터 수집 및 시각화
  - 이 프로젝트의 주요 목표는 '다음' 사이트에서 'OO역 맛집'을 검색했을 때, 나오는 맛집 중 상위 6개 가게의 이름과 해당 가게의 별점을 크롤링하여 정보를 수집하는 것입니다. 이후에는 이 데이터를 활용하여 가게의 별점을 기준으로 한 막대그래프를 생성하고, 이를 담은 엑셀 파일을 만들어내어 사용자들에게 손쉽게 맛집 정보를 제공하는 것입니다.
  -  사용자들은 엑셀 파일을 통해 시각적으로 맛집들의 별점을 비교하고, 가장 인기 있는 맛집을 쉽게 확인할 수 있게 될 것입니다. 
  -  (저희는 7호선을 기준으로 코드를 구현하였습니다.)
----
#### 프로젝트 구성
- 파이썬을 이용한 웹크롤링
- 해당 웹 맛집 데이터 6가지 정리
- 엑셀 데이터를 이용한 그래프 생성
----
#### 라이브러리 설치하기
```
# 엑셀
pip install openpyxl

# 웹 크롤링
pip install requests
pip install beautifulsoup4
```
----
#### 라이브러리 가져오기
```
import openpyxl #엑셀
import requests #웹
from bs4 import BeautifulSoup #웹
from openpyxl import Workbook #그래프
```
----
#### 1. 엑셀에서 역 이름 가져와서 리스트 담기
- 역들의 이름이 담긴 엑셀파일을 만들어주세요.
- 해당 엑셀 파일의 이름을 워크북 불러올때 괄호 안에 적어야 합니다.
```
# 워크북(workbook) 불러오기
workbook = openpyxl.load_workbook("역이름.xlsx")

# 활성화된 워크시트(worksheet) 가져오기
worksheet = workbook.active

# 역이름이 담길 리스트
food = []

# 각 행(row)을 하나씩 확인하며
max_row = worksheet.max_row
for row in range(1,max_row + 1):
    value = worksheet.cell(row=row, column=1).value
    food.append(value)
```
----
#### 2-1 크롤링 함수
- 크롤링 하고자 하는 웹 페이지의 링크를 준비해주세요.
- 해당 웹 페이지에서 'F12'키를 눌러 크롤링 부분의 태그를 확인해야합니다.
```
def topfood(text):
    # 요청(Request) 객체를 생성합니다.
    re_text = 'https://search.daum.net/search?w=tot&q='+text
    # text부분은 'OO역 맛집'입니다. 입력할때마다 변경되므로 변수로 설정했습니다.
    request = requests.get(re_text)

    # 웹 사이트의 HTML 소스코드를 추출합니다.
    html = request.text.strip()

    # HTML 소스코드를 파이썬 BeautifulSoup 객체로 변환합니다.
    soup = BeautifulSoup(html, 'html.parser')

    # 특정한 클래스 이름으로 접근합니다.
    data1 = soup.find_all('a', class_ ='fn_tit')

    data2 = soup.find_all('span', class_ ='f_red')
```
----
#### 2-2 크롤링 함수
- 위 내용이 계속 이어집니다.
- 맛집의 가게 이름과 별점 두가지 항목을 가져와 리스트에 담아줍니다.
```
    # 맛집 정보가 담길 리스트
        tit = [] # 가게이름
        star = [] # 별점
    
        for i,v in enumerate(data1):
            tit.append(v.get_text())
    
        for i,v in enumerate(data2):
            Test = v.get_text()
        
            if '.' in Test :
                star.append(float(v.get_text()))
```
----
#### 2-3 제목과 별점 엑셀파일로 나타내기
- 위 함수 내용이 계속됩니다.
- 가게이름과 별점이 담긴 워크시트를 가져와 데이터를 담아내는 부분입니다.
```
    # 워크북(workbook) 생성
    workbook = Workbook() 

    # 활성화된 워크시트(worksheet) 가져오기
    worksheet = workbook.active
    worksheet.append(['가게 이름','별점'])
    for t,s in zip(tit,star):
    # 한 줄(row)씩 데이터 입력하기
        worksheet.append([t,s])
```
- 다음은 이어서 막대그래프를 생성합니다.
- 완성된 데이터를 최종 엑셀 파일로 추출합니다.
```
    bar_chart = openpyxl.chart.BarChart()

    bar_chart.width = 17
    bar_chart.height = 14

    bar_chart.title = f"{text}"
    bar_chart.x_axis.title = "가게 이름"
    bar_chart.y_axis.title = "별점"

    datas = openpyxl.chart.Reference(worksheet, min_row=2, min_col=1, max_row=7, max_col=2)
    bar_chart.add_data(datas, from_rows=True, titles_from_data=True)
    worksheet.add_chart(bar_chart, "A9")

    workbook.save("food_list.xlsx")
```
----
#### 3. 원하는 역 검색 기능 -> 크롤링 함수 실행
- 역 이름을 하나 입력 받아 사용자가 원하는 역에 대한 정보만 제공할 수 있도록 구현하였습니다.
- 만약 입력한 역이 해당 호선에 존재하지 않는다면 계속해서 다시 입력받도록 하였습니다.
```
while (1):

    name = input('7호선 중 원히는 역 이름을 검색하세요. (역 뻬고)')

    if name in food :
        print(f'7호선 {name}역 맛집 분석 시작하겠습니다.')
        topfood(f'{name}역맛집')
        break
    else:
        print(f'{name}역은 7호선에 존재하지 않습니다.')
```
----
#### Test
- exel_example.py는 7호선 역들을 엑셀파일로 자동 저장해주는 예시 코드 입니다. 코드 실행 후 foodgrapy_code.py 코드를 실행하면 정상적으로 작동이 됩니다.
- 만약 openpyxl을 설치했는데 import가 되지 않을경우 코드위에 붙이면 정상적으로 작동이 됩니다.
---- 
#### 참고 및 출처
- [엑셀](https://github.com/ndb796/Python-Robotic-Process-Automation/tree/main/6)
- [시각화](https://github.com/ndb796/Python-Robotic-Process-Automation/tree/main/8)
- [크롤링](https://github.com/ndb796/Python-Robotic-Process-Automation/tree/main/12)




