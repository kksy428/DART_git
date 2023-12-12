import sys

# openpyxl 모듈이 설치된 경로
openpyxl_path = '/Users/ksy/miniconda3/lib/python3.11/site-packages'

# sys 모듈을 사용하여 모듈을 불러올 수 있는 경로 추가
sys.path.append(openpyxl_path)

# 이제 openpyxl 모듈을 불러올 수 있음
import openpyxl
import openpyxl

# 주어진 역 이름 리스트
station_names = [
    "장암",
    "도봉산",
    "수락산",
    "마들",
    "노원",
    "중계",
    "하계",
    "공릉",
    "태릉입구",
    "먹골",
    "중화",
    "상봉",
    "면목",
    "사가정",
    "용마산",
    "중곡",
    "군자",
    "어린이대공원",
    "건대입구",
    "뚝섬유원지",
    "청담",
    "강남구청",
    "학동",
    "논현",
    "반포",
    "고속터미널",
    "내방",
    "이수",
    "남성",
    "숭실대입구",
    "상도",
    "장승배기",
    "신대방삼거리",
    "보라매",
    "신풍",
    "대림",
    "남구로",
    "가산디지털단지",
    "철산",
    "광명사거리",
    "천왕",
    "온수",
    "까치울",
    "부천종합운동장",
    "춘의",
    "신중동",
    "부천시청",
    "상동",
    "삼산체육관",
    "굴포천",
    "부평구청"
]

# 엑셀 파일에 역 이름 저장
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "역 이름"

# 역 이름을 엑셀에 추가
for index, station in enumerate(station_names, start=1):
    sheet.cell(row=index, column=1).value = station

# 파일로 저장
file_path = "역이름.xlsx"  # 저장할 파일 경로 및 이름
workbook.save(file_path)

print(f"'{file_path}' 파일에 역 이름이 저장되었습니다.")
