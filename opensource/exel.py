pip install openpyxl

from openpyxl import Workbook

workbook = Workbook() # 워크북(workbook) 생성

# 활성화된 워크시트(worksheet) 가져오기
worksheet = workbook.active

# 한 줄(row)씩 데이터 입력하기
worksheet.append(["이순신", 97, 3])
worksheet.append(["홍길동", 85, 2])
worksheet.append(["장보고", 100, 3])

# 워크북(workbook) 저장하기
workbook.save("output.xlsx")

"""
open(파일 이름, 모드, 인코딩) 함수를 이용해 파일 객체를 생성할 수 있습니다.
r: 읽기 모드로, 파일을 읽기만 할 때 사용합니다.
UTF8: 한글과 같은 유니코드를 처리하기 위한 인코딩 방식입니다.
"""

file = open('./students.txt', 'r', encoding='UTF8') # 파일 객체 생성

text = file.read() # 파일의 전체 내용을 문자열로 반환
print(text)

file.close() # 파일 객체 닫기

from openpyxl import Workbook

def read_files(file_names):
    text = ""
    for file_name in file_names: # 파일 이름을 하나씩 확인하며
        # 파일을 열어 text 변수에 추가
        with open(file_name, 'r', encoding='UTF8') as file:
            text += file.read()
        text += "\n" # 줄바꿈 추가
    return text

text = read_files(["students.txt", "students2.txt"])
text = text.strip() # 앞 뒤로 공백 제거

workbook = Workbook() # 워크북(workbook) 생성

# 활성화된 워크시트(worksheet) 가져오기
worksheet = workbook.active

student_list = []
# 한 줄씩 확인하며
for line in text.split('\n'):
    # [번호, 이름, 점수1, 점수2, 점수3, 학과, 학번]을 차례대로 확인
    id, name, score1, score2, score3, depart, grade = line.split(' ')
    # 수 데이터는 수 자료형으로 변환
    id = int(id)
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    grade = int(grade[0]) # 학년에 해당하는 숫자 데이터만 저장
    student = [id, name, score1, score2, score3, depart, grade]
    student_list.append(student)

for student in student_list:
    # 한 줄(row)씩 학생 정보 입력하기
    worksheet.append(student)

# 워크북(workbook) 저장하기
workbook.save("students.xlsx")

