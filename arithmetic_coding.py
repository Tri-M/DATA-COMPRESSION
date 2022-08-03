s=input("Enter string :")
dict1={}
n=len(s)
for i in s:
    dict1[i]=0
for i in s:
    dict1[i]+=1/n
print(dict1)

high=1
for i in dict1:
    low=dict1[i]
    dict1[i]=(high-low,high)
    high-=low
print(dict1)

ranges=[0,1]
for i in s:
    low,high=ranges
    ranges[0]=low+(high-low)*dict1[i][0]
    ranges[1]=low+(high-low)*dict1[i][1]
print(ranges)

x=0.71775875
word=""
for j in range(n):
    for i in dict1:
        if dict1[i][0]<x<=dict1[i][1]:
            word+=i
            x=(x-dict1[i][0])/(dict1[i][1]-dict1[i][0])
            break
print(word)

