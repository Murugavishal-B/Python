arr=[1,2,3,4,5,6,7,8,9]
target=7
n=len(arr)
for i in range(0,n):
    if arr[i]==target:
        print(f"Target Element found at Index{[i]}")
        break
else:
    print("Target Element not in the given array")
