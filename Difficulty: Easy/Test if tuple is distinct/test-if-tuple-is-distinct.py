arr = tuple(map(int, input().split()))

# code here
if len(arr) == len(set(arr)):
    print("True")
else:
    print("False")