#-*- coding:utf-8 –*-
#可以重复取，正序j
def allBag(weight,value,n):
  arr=[0]*(n+1)
  for i in range(len(weight)):
    for j in range(1,n+1):
      if j-weight[i]>=0:
        arr[j]=max(arr[j-weight[i]]+value[i],arr[j])
  return arr[-1]
#二维数组看物体重
#p[i][j]存的是哪一个物体
def allBag(weight,value,n):
  arr=[[0 for i in range(n+1)] for j in range(len(weight))]
  p=[[0 for i in range(n+1)] for j in range(len(weight))]
  for i in range(len(weight)):
    for j in range(1,n+1):
        arr[i][j]=arr[i-1][j]
        if j-weight[i]>=0 and arr[i][j-weight[i]]+value[i]>arr[i][j]:
            arr[i][j]=arr[i][j-weight[i]]+value[i]
            p[i][j]=i
        else:
            p[i][j]=0
  return arr,p
#输出时注意递归的用法
def printp(weight,p,i,j):
    if i>=0 and j>=0:
        if p[i][j]>0:
            printp(weight,p,i,j-weight[p[i][j]])
            print weight[p[i][j]],value[p[i][j]]
        if p[i][j]==0:
            printp(weight,p,i-1,j)
