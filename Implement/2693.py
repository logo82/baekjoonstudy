#2693
test = int(input())

tmp = 0
for i in range(test):
  A = list(map(int, input().split()))
  for j in range(len(A) - 1):
    for k in range(len(A) - 1):
      if A[k] > A[k + 1]:
        tmp = A[k]
        A[k] = A[k + 1]
        A[k + 1] = tmp
  print(A[-3])
