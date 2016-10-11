for i in range(3):
    print('Loop %d' % i)

    if i == 1:
        break
else:
    print('Else block')

for i in []:
    print('Never runs')
else:
    print('For Else block')

while False:
    print('Never runs')
else:
    print('While Else block!')

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

# 루프 다음에 오는 else 블록은 절대로 사용하지 말아야 한다.
