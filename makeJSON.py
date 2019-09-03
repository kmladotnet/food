import io
import json

# 급식 뒤에 1.4.5. 같은 알레르기 나타내주는 정보를 없애주는 함수
def remove_num(msg):
    for i, ele in enumerate(msg):
        if ele.isdigit():
            msg = msg[:i]

    return msg

# java 파일을 실행한 이후 출력값을 받아 리턴해주는 함수
def get_buffer():
    texts = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        texts.append(line)

    return io.StringIO('\n'.join(texts))

if __name__ == "__main__":
    buf = get_buffer() # java 파일의 출력값은 여기 들어간다

    # 급식 달력. 예를 들어 food_dict[1][10]["breakfast"]는 1월 10일 아침 메뉴.
    food_dict = {}
    current_month = current_day = current_meal = ""

    for line in buf:
        # M 뒤에는 몇 월인지 알려준다.
        if line[0] == 'M':
            current_month = str(line[1:-1])
            food_dict[current_month] = {}

        # D 뒤에는 몇 일인지 알려준다. D4는 4일, D20은 20일!
        elif line[0] == 'D':
            current_day = str(int(line[1:-1]))
            food_dict[current_month][current_day] = {}

        # b -> 아침
        elif line[0] == 'b':
            current_meal = "breakfast"
            food_dict[current_month][current_day][current_meal] = []

        # l -> 점심
        elif line[0] == 'l':
            current_meal = "lunch"
            food_dict[current_month][current_day][current_meal] = []

        # d -> 저녁
        elif line[0] == 'd':
            current_meal = "dinner"
            food_dict[current_month][current_day][current_meal] = []

        else:
            # 가끔씩 &amp 가 끼워져 있는 경우가 있음. 이걸 &으로 바꾸자
            if '&amp;' in line:
                line = line.replace('&amp;', '&')
            
            # 마지막 character 없애준다. 왜인지는 기억 안 남...개행 문자(\n)일 듯
            line = line[:-1]

            # 알레르기 정보 숫자 없애준다
            line = remove_num(line)

            # 이 정보를 최종적으로 급식 달력에 넣어준다
            food_dict[current_month][current_day][current_meal].append(line)

    # 딕셔너리 자료형인 food_dict를 json 객체로 변환해준다.
    # https://docs.python.org/3/library/json.html
    json_obj = json.dumps(food_dict, ensure_ascii=False, indent=4, separators=(',', ': '))

    # json 객체를 .json 파일로 저장한다
    with open("./data.json", "w") as outfile:
        json.dump(food_dict, outfile, ensure_ascii=False, indent=4, separators=(',', ': '))
