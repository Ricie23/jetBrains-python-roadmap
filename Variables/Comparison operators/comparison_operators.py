one = 1
two = 2
three = 3

# This chained comparison means that the (one < two) and (two < three)
# comparisons are performed at the same time.
print(f"one < two < three: {one < two < three}")

is_greater = three > two
print(f"three is greater than two: {is_greater}")

is_less = one < three
print(f"one is smaller than three: {is_less}")

is_true = one < three > two
print(f"one is smaller than three, which is greater than two: {is_true}")

not_equal = one != two
print(f"one does not equal two: {not_equal}")

is_equal = three == three
print(f"three equals three : {is_equal}")
