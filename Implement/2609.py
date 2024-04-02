#2609
from sys import stdin

num1, num2 = map(int, stdin.readline().split())

# min_num = 1
# max_num = num1 * num2

# #최대공약수 구하기
# #1부터 두 수중 한 수까지 계속 나누어 둘 다 나머지가 0인경우를 공약수로 함
# #마지막으로 나누어 떨어지게 하는 수가 최대공약수
# for i in range(1, num1):
#   if (num1 % i == 0) and (num2 % i == 0):
#     min_num = i

# #만약 서로소일 경우 나올 수 있는 최소공배수인 두 수의 곱부터 1씩 내리며 최소 공배수 체크
# #두 수로 각각 나누었을 때 나머지가 둘 다 0일 경우 공배수로 봐도 됨
# for j in range(num1 * num2, 1, -1):
#   if (j % num1 == 0) and (j % num2 == 0):
#     max_num = j

#유클리드 호제법 이용하기
#a, b 두 수가 있을 때, a, b를 나눈 나머지가 r1이라 하면 여기서 r1 == 0일 경우 b가 최대공약수이다.
#여기서 r1이 0이 아닐경우 b를 r1으로 나눈 나머지가 r2라 하자. 여기서 r2 == 0일 경우 r1이 최대공약수이다.
#이렇게 반복해서 나머지가 0이 될 떄 까지 진행하면 최대공약수를 찾을 수 있다.
#최소 공배수는 (a * b) // 최대공약수를 하면 되니 더 쉽다.

#유클리드 호제법은 무조건 a가 b보다 커야한다.
if num2 > num1:
  tmp = num2
  num2 = num1
  num1 = tmp


#최대공약수
def gcd(a, b):
  while (a % b != 0) and (a != 0):
    r = a % b
    a, b = b, r

  return b


#최소공배수
def lcm(a, b):
  return (a * b) // gcd(a, b)


print(gcd(num1, num2))
print(lcm(num1, num2))

#https://jih3508.tistory.com/13