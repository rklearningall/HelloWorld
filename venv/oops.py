a = 1000
b = 502
c = 501
a = b
b = c
c = a
print(a)
print(b)
print(c)
sum = a + b + c
print(sum)
if a > b or a > c:
     print(a,"is biggest ")
elif b>c:
    print(b,"is biggest")
else:
    print(c,"is biggest ")
