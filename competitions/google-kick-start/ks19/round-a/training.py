import sys

test_cases = int(input())
for t in range(test_cases):
  students_len, team_len = [int(x) for x in input().split()]
  skill_ratings = [int(x) for x in input().split()]
  skill_ratings.sort(reverse=True)

  aggs = [0]
  for i in range(students_len):
    aggs.append(aggs[i] + skill_ratings[i])

  min_time = sys.maxsize
  for i in range(students_len + 1 - team_len):
    min_time = min(min_time, team_len * skill_ratings[i] - (aggs[i+team_len] - aggs[i]))

  print("Case #", t+1, ": ", min_time, sep="")
