list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 1. Use zip() to combine multiple lists into a single iterable 
########### Write your code below ###############
zipped = zip(list1,list2) 
########### Write your code above ###############
print(list(zipped))  # Converts to list for display

# 2. Use filter() with lambda function to filter out numbers less than or equal to 2 in list1 
########### Write your code below ###############
filtered =filter(lambda e: e<=2,list1)
########### Write your code above ###############
print(list(filtered))

# 3. Using map() with lambda function to multiply each number of list1 by 2
########### Write your code below ###############
mapped = map(lambda e:e*2,list1)
########### Write your code above ###############
print(list(mapped))

