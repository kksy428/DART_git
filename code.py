#start
import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# 윈도우 생성
root = tk.Tk()
root.title("사용자 인터페이스 예제")

# 레이블과 입력 필드 생성
label = tk.Label(root, text="이름을 입력하세요:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# 버튼 생성
button = tk.Button(root, text="인사", command=on_button_click)
button.pack()

# GUI 시작
root.mainloop()
