def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6
assert remainder(20, divisor=7) == 6
assert remainder(number=20, divisor=7) == 6
assert remainder(divisor=7, number=20) == 6


# 위치 인수는 키워드 인수 앞에 지정되어야 한다.
# assert remainder(number=20, 7) == 6

# assert remainder(20, number=7) == 6


# 키워드 인수의 유연성 세 가지
# 코드를 처음 보는 사람이 함수 호출을 더 명확하게 이해할 수 있다는 점이다.
# remainder 메서드의 구현을 보지 않고서 remainder(20, 7) 호출에서 어떤 인수가 숫자이고 어떤 인수가 나눗수인지 분명하지 않다.
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


# 두번째 이점은 기본값을 설정할 수 있다.
weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)


# 세번째 이점은 기존의 호출 코드와 호환성을 유지하면서도 함수의 파라미터를 확장할 수 있는 강력한 수단이 된다는 점이다.
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period


pounds_per_hour = flow_rate(weight_diff, time_diff, period=360, units_per_kg=2.2)
print(pounds_per_hour)

# 이 방법의 유일한 문제는 period, unit_per_kg를 위치 인수로도 넘길 수 있다는 것이다.
pounds_per_hour = flow_rate(weight_diff, time_diff, 360, 2.2)
print(pounds_per_hour)

