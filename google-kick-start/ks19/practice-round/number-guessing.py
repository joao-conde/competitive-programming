def guess(lb, up):
  # binary search
  mid = lb + (up - lb)//2
  print(mid) # guess
  answer = input()
  if answer == "TOO_BIG":
    guess(lb, mid - 1)
  elif answer == "TOO_SMALL":
    guess(mid + 1, up)
  else: return

test_cases = int(input())
for _ in range(test_cases):
  lb, up = map(int, input().split())
  _ = int(input())
  guess(lb + 1, up)
