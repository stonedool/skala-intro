# echo.py
from password import is_valid_password

while True:
    sentence = input("문장을 입력하세요 (!quit 입력 시 종료): ")

    if sentence == "!quit":
        print("프로그램을 종료합니다.")
        break

    if is_valid_password(sentence):
        print("유효한 비밀번호입니다:", sentence)
    else:
        print("비밀번호 조건을 만족하지 않습니다.")
