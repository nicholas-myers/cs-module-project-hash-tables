# Add up and print the sum of the all of the minimum elements of each inner array:
num_arrays = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# print lowest values in arrays
# produce the sum of those values
# iterate throgh each index array
# create lowest variable
# create a sum variable
# have the lowest get added to sum

min_sum = 0
for arr in num_arrays:
    # print(arr)
    lowest = arr[0]
    for num in arr:
        # print(lowest)
        if int(num) < lowest:
            lowest = num
            # print(lowest)
    
    min_sum += lowest

print(min_sum)