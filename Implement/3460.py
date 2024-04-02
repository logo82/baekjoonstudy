#3460
#양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.
'''
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)
출력
각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.
'''

#10진수 -> 2진수 변환하는 알고리즘을 참고하여 하면 될듯

#10진수를 넣으면 2진수로 바꾸고 2진수가 1인 자리를 출력하는 함수
#인수: int, return: 없음, 단순 출력 함수


def binaryTodecimal(decimal):
  binary = []
  #나눈 몫이 0이 아닐때까지 반복하며 2진수로 변형
  while (decimal > 0):
    binary.append(decimal % 2)
    decimal = decimal // 2

  counter = 0
  for j in binary:
    counter += 1

  for j in range(counter):
    if binary[j] == 1:
      print(j, end=' ')

  return 0


num = int(input())

for dec in range(num):
  decimal = int(input())
  binaryTodecimal(decimal)
