#-*- coding:utf-8 –*-
#可以重复取，正序j
def allBag(weight,value,n):
  arr=[0]*(n+1)
  for i in range(len(weight)):
    for j in range(1,n+1):
      if j-weight[i]>=0:
        arr[j]=max(arr[j-weight[i]]+value[i],arr[j])
  return arr[-1]
