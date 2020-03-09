import math

def max_subarray_sum(array, subarray_length):
  aggs = [0]
  for i in range(len(array)): aggs.append(aggs[i] + array[i]) # sum aggregated list of array to the left
  max_sum = -1 # sum >= 0 for array of positive values
  for i in range(len(aggs) - subarray_length): max_sum = max(max_sum, aggs[i+subarray_length] - aggs[i])
  return max_sum

test_cases = int(input())
for i in range(test_cases):
  sections_to_paint = math.ceil(int(input())/2) # paint half, other half is destroyed, we get to paint the last section
  mural_beauty_scores = [int(x) for x in input()]
  max_beauty = max_subarray_sum(mural_beauty_scores, sections_to_paint)
  print("Case #", i+1, ": ", max_beauty, sep="")
