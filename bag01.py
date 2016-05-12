#-*- coding:utf-8 –*-
#那个j是倒过来求的，正序会导致重复加入背包，会影响i-1时候的状态
#状态转移函数f[i][j]=max(f[i-1][j],f[i-1][j-weight[i]]+value[i])
def bag01(weight,value,n):
    arr=[0]*(n+1)
    for i in range(len(weight)):
        for j in range(n,1,-1):
            if j>=weight[i]:
                arr[j]=max(arr[j],arr[j-weight[i]]+value[i])
    return arr[-1]
#递归
#递归就是做同样的事，但是输入不同
#递归第一件事就是想好边界
def bag001(i,weight,value,n):
    if n<=0:
      return 0
    if i==0:
      return 0 if weight[i]>n else value[i]
    #当放不进背包的时候，直接取下一个
    if n-weight[i]<0:
      return bag001(i-1,weight,value,n)
    else:
    #加入背包，输入就是n-weight,价值就+value[i],或者不加入背包，取下一个
      return max(bag001(i-1,weight,value,n-weight[i])+value[i],bag001(i-1,weight,value,n))

weight=[2,5,6,2,4]
value=[6,4,5,3,6]
n=[i for i in range(1,15)]
for i in n:
    print bag01(weight,value,i)
