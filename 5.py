binary_num=[]
x=int(input("Enter the decimai number :"))
m=x
while m != 0 :
    z=m%2
    binary_num.append(z)
    m=m//2
binary_num.reverse()
s=" "
for i  in binary_num:
    s=s +str(1)
print(s)