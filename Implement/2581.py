#2581
'''
풀이
우선 소수를 구하는 함수를 만들어 소수 리스트를 만든다.
소수 리스트 중 젤 앞 원소가 최솟값이고 합은 그냥 구하면 될듯
'''

M = int(input())  #최솟값
N = int(input())  #최댓값
prime_list = []  #소수 리스트


#소수 구하는 함수(int)
def prime_num(num):
  count = 0
  #1부터 num까지 숫자로 나누었을 때 나머지가 0인 경우 count를 추가
  #소수: 1또는 자기 자신으로만 나누어 떨어지는 수

  for i in range(1, num):
    if (num % i) == 0:
      count += 1

  if (count == 1):
    prime_list.append(num)


for i in range(M, N + 1):
  prime_num(i)

tot = 0
for j in prime_list:
  tot += j

#소수 리스트에 원소가 있을 경우(소수가 있을 경우)
if (tot != 0):
  print(tot)
  print(prime_list[0])
else:
  print("-1")
