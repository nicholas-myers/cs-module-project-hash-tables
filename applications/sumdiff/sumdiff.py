"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# create a list of possible combinations
# check each possible list of combinations in the formula
combos = {}
count = 0
for x in q:
    for y in q:
        count+=1
        combos[count] = (x, y)
# print(combos)

for add in combos:
    for sub in combos:
        if f(combos[add][0]) + f(combos[add][1]) == f(combos[sub][0]) - f(combos[sub][1]):
            x_add = f(combos[add][0])
            y_add = f(combos[add][1])
            x_sub = f(combos[sub][0])
            y_sub = f(combos[sub][1])
            print(f"f({combos[add][0]}) + f({combos[add][1]}) = f({combos[sub][0]}) - f({combos[sub][1]})  {x_add} + {y_add} = {x_sub} - {y_sub}")
        
        
