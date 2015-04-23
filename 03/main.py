def f(a,b):
    m=0
    n=False
    high = len(a)-1
    low = 0
    while (low<(high-1)):
        mid=int((high+low)/2)
        if(a[high]==b):
            m=high+1
            n=True
            break
        if(a[mid]==b):
            m=mid+1
            n=True
            break
        if(a[low]==b):
           m=low+1
           n=True
           break
        elif a[mid]>b:
            high=mid
        elif a[mid]<b:
            low=mid
    if(n):
           return(m)
    else:
           return(0)

stu=input("请输入要被查找的序列，以逗号隔开，并按照从大到小的顺序:")
stu1=eval(stu)
stu2=list(stu1)
a=stu2
b=int(input("请输入你要查找的数:"))
m=f(a,b)
if m==0:
    print('没有找到')
else:
           print("你要找的数在列表中的第{0}个位置".format(m))
            
