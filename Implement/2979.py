#2979
'''
풀이
가장 먼저 들어온 시가ㅣㄴ과 가장 나중에 나가는 시간을 구해 이 시간동안 반복
count 변수를 하나 만들어서 차가 주차하고 있을 경우 +1, 나가면 -1
차가 3대, 2대, 1대 있을 경우를 각각 구분해서 주차요금 계산
'''

A, B, C = map(int, input().split())

#들어오는 시간과 나가는 시간의 배열
input_time = []
output_time = []

#들어오는 시간과 나가는 시간을 세 번 받아 배열에 insert
for i in range(3):
  it, ot = map(int, input().split())
  input_time.append(it)
  output_time.append(ot)

#나가는 시간 중 가장 나중에 들어오는 차 구하기
big_out = 0
for j in output_time:
  if big_out < j:
    big_out = j

switch_1 = switch_2 = switch_3 = 0
switch_tot = 0

price = 0
for car in range(big_out + 1):
  if (input_time[0] <= car):
    switch_1 = 1
  if (output_time[0] <= car):
    switch_1 = 0

  if (input_time[1] <= car):
    switch_2 = 1
  if (output_time[1] <= car):
    switch_2 = 0

  if (input_time[2] <= car):
    switch_3 = 1
  if (output_time[2] <= car):
    switch_3 = 0

  switch_tot = switch_1 + switch_2 + switch_3

  if (switch_tot == 1):
    price += A
  elif (switch_tot == 2):
    price += B * 2
  elif (switch_tot == 3):
    price += C * 3

print(price)
