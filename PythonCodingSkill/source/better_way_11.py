names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

print(letters)

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
        print(longest_name)
print(longest_name)

# zip 이터레이터를 병렬 순회할 때 사용
# Python3 zip은 지연 제너레이터, Python2 zip은 전체 결과를 튜플 리스트로 반환(itertools의 izip이 대안)
# 길이가 다른 이터레이터를 사용하면 zip은 그 결과를 조용히 잘라낸다.
# 내장 모듈 itertools의 zip_longest 함수를 쓰면 여러 이터레이터를 길이에 상관없이 병렬로 순회할 수 있다.(Python2에서는 izip_longest)

