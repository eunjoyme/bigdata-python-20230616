# 내장함수
print(abs(-4)) # 절대값
print(chr(65)) # 숫자를 캐릭터로 변경 65 A, 97 a ascii 코드 번호
print(ord('a')) # 아스키코드값으로 바꿔줌
print(chr(44036)) # utf-8 코드번호
print(ord('각')) # 
print(chr(13)) # enter
print(min(1,4)) # 최소값
print(max(12,5)) # 최댓값
print(eval('1+4')) # eval[uate] 실행
print(hex(234)) #16 진수
a = 0
b = 1
print(id(a)) # a변수의 메모리 주소
print(id(b)) # b변수의 메모리 주소

print(int('30')) # digit number 문자열을 정수로 변환
print(pow(2,10)) # 제곱승 함수
print(2**10) # 제곱승 연산자

# map
def three_times(numberlist):
    result = []
    for n in numberlist:
        result.append(n * 3)
    return result

l1 = [3,6,9,12]
print(three_times(l1))

def threetimes(x):
    return x *3

print(list(map(threetimes, l1)))
# 함수를 첫번째 파라미터로, 두번째를 적용시킬 리스트로 
# 리스트 요소 하나씩을 함수를 통해서 처리를 해주는 방법

print(list(map(str, l1)))
print(list(map(float, l1)))
# map 결곽가 map object\이기때문에 list, tuple, set로 형변환 필요

# range list 두개를 잘 활용하면 순차적 리스트를 쉽게 만들 수 있음
print(list(range(1,101)))
print(list(range(3,100,3))) # 3의 배수 99까지

print(round(4.6))
print(round(3.141592, 4))
