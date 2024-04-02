#1292
#1 22 333 4444 55555 666666
'''
풀이
1. 수열을 직접 만들어 슬라이싱 한다
  a. 구간의 끝자리까지 반복하며 수열 생성
  b. 생성된 수열을 바탕으로 구간 합 구하기
'''

#1번 풀이
start, end = map(int, input().split())
sequence_list = []

#1223334444...등으로 수열을 생성
for i in range(end):
  sequence_list += [i + 1] * (i + 1)

#start ~ end 구간을 정해 이 구간의 합 구하기
tot = 0
for j in sequence_list[start - 1:end]:
  tot += j

print(tot)
