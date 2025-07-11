def sum_odd_even(st,end):
    sum_odd=0
    sum_even=0
    for i in range(st,end+1):
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
    print(f"Sum of Odd numbers = {sum_odd}")
    print(f"Sum of Even numbers = {sum_even}")
st=int(input("Enter the Start Value:"))
end=int(input("Enter the End Value:"))
sum_odd_even(st,end)
