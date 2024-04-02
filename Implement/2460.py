#2460
#내린 사람과 타는 사람의 배열을 각각 만들어 입력 받기
#공통의 변수(ex:사람)을 만들어 내린 사람 -> 타는 사람의 순서로 -+
#배열을 비교하며 큰 수 비교 알고리즘을 사용하여 큰 수 비교하기

#내리는 사람 배열
down = [0] * 10
#타는 사람 배열
up = [0] * 10

for i in range(10):
  down[i], up[i] = map(int, input().split())

people = 0
biggest = 0
#내린 사람을 적용하고 수 비교, 탄 사람을 적용하고 수 비교하면 결국 가장 많았을 때의
#사람이 biggest에 들어가있음10
for num in range(10):
  people -= down[num]
  if people > biggest:
    biggest = people
  people += up[num]
  if people > biggest:
    biggest = people

print(biggest)
