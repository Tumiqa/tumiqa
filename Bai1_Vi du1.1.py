a=int(input('Nhập giá trị của a: '))
b=int(input('Nhập giá trị của b: '))
c=int(input('Nhập giá trị của c: '))

max=a
if(max<b):
    max=b

if(max<c):
    max=c

print('Số lớn nhất là: ',max)
