#list comprehension
#for loop

res=[]
for i in range(11):
    res.append(i)
print(res)


#list com version
print([i for i in range(11)])

#for loop ---odd ele
res=[]
for i in range(11):
    if i%2!=0:
        res.append(i)
print(res)

print([i if i%2!=0 else i**2 for i in range(11)])




#if even---cube
#if odd----sqre


mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res=[]

for i in mat:
    
    for j in i:
        if j%2==0:
            res.append(j**3)
        else:
            res.append(j**2)
print(res)

#list comprehension

print([j**3 if j%2==0 else j**2 for i in mat for j in i])

#printing in 3d

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res=[]


for i in mat:
    row_data=[]
    for j in i:
        if j%2==0:
            row_data.append(j**3)
        else:
            row_data.append(j**2)
    res.append(row_data)
print(res)

#list comp

print([[j**3 if j%2==0 else j**2 for j in i]for i in mat])


mylist=list([9,3,6,1,5,0,8,2,4,7])
list_b=list([6,4,6,1,2,2])
res=[]
for i in list_b:
    res.append((i,mylist.index(i)))
print(res)

#list comp

print([(i,mylist.index(i)) for i in list_b])


#

mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
dict1={}
for i in list_b:
    dict1[i]=mylist.index(i)
print(dict1)

#list comp
print({i:mylist.index(i) for i in list_b})


sent=["a new world record was set","in the holy city of ayodhya"]
stop=['for','a','of','the','was']
res=[]
for i in sent:
    row_data=[]
    for j in i.split():
        if j not in stop:
            row_data.append(j)
    res.append(row_data)
print(res)

#list comp
print([[j for j in i.split() if j not in stop]for i in sent])



array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
    num2=num2+str(i)
print(int(num2)+num1)





s=input().split(",")#rhdt:246,ghftd:1246
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)#stt=[rhdt,ghftd]
    numm.append(n)#numm=[246,1246]
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))


n=int(input(""))
j=[]
p=[]
b=[]
for i in range(9):
    a=i+a
    j.append(a)

for x in j:
    for y in range(x+1):
        if x%y==0:
            p.append(y)
            p=p.sort()
            b=p[-1]+b
print(b)
        
        
    
        

    





            






        
        
    

