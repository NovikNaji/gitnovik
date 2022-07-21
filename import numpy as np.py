import numpy as np
import array as arr 

a=list(input().lower())
n=len(a)
k=0
b=''





for i in range(n):
    k=0
    for j in range(n):
        if(a[i]==a[j]):
            k+=1
    if(k==1):
        b+='('
    else:
        b+=')'
print(n)
print(b)
print(a)