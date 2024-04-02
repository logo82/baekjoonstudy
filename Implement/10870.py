#10870
#그냥 피보차니 함수 만들어서 피보나치 수를 리스트에 저장한다음 인덱싱하면 됨
n = int(input())
pibonachi = [0, 1]


def pibo(n):
  pibonachi.append(pibonachi[n - 1] + pibonachi[n - 2])


for j in range(2, n + 1):
  pibo(j)

print(pibonachi[n])
