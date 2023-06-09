# 주석
# 파이썬에서는 #을 붙여서 나타냄(주석은 언어마다 다름)_주석이 필요한 이유(협력)
# vscode 단축키 주석(ctrl + /), 실행(ctrl + f5), 줄바꿈(alt + 방향키)

print("1 + 2 =", 1 + 2) # 1 + 2의 결과를 출력
print("1 - 2 =", 1 - 2) # 1 - 2의 결과를 출력
print("1 * 2 =", 1 * 2) # 1 * 2의 결과를 출력
print("1 / 2 =", 1 / 2) # 1 / 2의 결과를 출력
print("2 ** 3 =", 2 ** 3) # **(제곱)
print("3 / 2 =", 3 / 2) # 나누기
print("3 // 2 =", 3 // 2) # 몫(자연수만)
print("3 % 2 =", 3 % 2) # 나머지
# 프린트함수 : 터미널에 출력(아웃풋)

# python의 연산자(operator)
# + 더하기 연산자
# - 빼기 연산자
# * 곱하기 연산자
# / 나누기 연산자
# ** 제곱 연산자
# // 정수 나누기(몫) 연산자
# % 나머지 연산자
# 피연산자 : 2,3(연산되는글자)

# 문자형데이터(string 타입) : "",'' 문자로 인식, 사용
print("안녕하세요")
print('반갑습니다')
print('여러분') # "안녕' 인식불가, 앞뒤통일
print("그는 생각했다. '생각생각생각'")
print('그녀는 말했다. "말말말"')
print("쌍따옴표 사용하기 \"말말말\"")
# 이스케이프 문자(역슬래시를 더해 새로운 문자로 만듬)
# \n : 줄바꿈
# \t : 탭
# \" : 쌍따옴표
# \' : 따옴표
print('n\n\tt')
print("안녕하세요\n반갑습니다\n잘부탁드립니다\n안녕히계세요")
print("""안녕하세요
반갑습니다
잘부탁드립니다
안녕히계세요""")
print('''안녕하세요
반갑습니다
잘부탁드립니다
안녕히계세요''')

# 숫자형데이터(number 타입)
# 파이썬의 숫자형(실수형_부동소수형:float, 정수형:int, 허수형_복수형:complex)_실수형, 정수형 주로 사용