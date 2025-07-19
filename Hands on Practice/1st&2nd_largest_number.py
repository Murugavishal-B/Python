def using_sorted():
    num=sorted(num)
    n=len(num)
    print(num[n-1],num[n-2])
def using_loop():
    lar=num[0]
    for i in num:
        if lar<i:
            lar=i
    return lar
num=[12,56,42,36,496,64]
lar=using_loop()
print(lar)
num=num.remove(lar)
print(num)
