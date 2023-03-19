"""def pd(n):
    n=str(n)
    if n==n[::-1]:
        return True
a=int(input())
while(a!=0):
    a+=1
    if pd(a)==True:
        print(a)
        break



dict1={"p":"pediatrics","o":"orthopedics","e":'ent'}
def med(a):
    res=0
    for i in a:
        p=a.count(i)
        if res<p:
            res=p
            o=i
    return dict1[o]
print(med([101,"o",102,"p",103,"p"]))


def med(p,s):
    P=p.count("p")
    E=p.count("e")
    O=p.count("o")
    if P>E and P>O:
        spec=s['p']
    elif E>O:
        spec=s['e']
    else:
        spec=s['o']
    return spec
p=[101,"o",102,"p",103,"p"]
s={"p":"pediatrics","o":"orthopedics","e":'ent'}
print(spec)




def sent(s1,s2):
    s3=[i for i in s1]
    s4=[i for i in s2]
    for i in s3:
        if i in s4 and i!=" ":
            
            print(i,end="")
    return 
            
print(sent("I like Python","Java is a popular language"))


x="I like Python"
y="Java is a popular language"
x=[i for i in x]
y=[i for i in y]

for i in x:
    if (i in y) and i!=" ":
        print(i,end="")

w1=input()
w2=input()
w1=[i for i in w1] 
w2=[i for i in w2]
d=[]
for i in w2:
    if i in w1:
        d.append(i)
    else:
        d=[]
print(d)

"""

k=int(input())
a=[int(i) for i in input()]
n=int(input())
a=a[::2]

if k%2==0 and len(a)!=0:
    for i in a:
        for j in range(n):
            print(i,end=" ")
            i=i+1
        print()
else:
    print("Invalid input")
  









    
    
            
