# 클래스 예제
class Calculator:
    def __init__(self) -> None:
        self.result = 0

    def __init__(self, num):
        self.result += num
        return self.result

    def __init__(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        pass

mycalc = Calculator() # javaj와 달리 new 없음
print(mycalc.add(40))
print(mycalc.add(50))
print(mycalc.sub(15))

val = 10
if val != 10:
    pass

