#lists
list1=[]
print(list1,type(list1))
list2=[20,30]
list2.append([40])
print(list2,type(list2))
list2.extend([50,60,70])
print(list2,type(list2))


def sentence(st):
    a=0
    n=0
    for i in st:
        if i>='a' and i<='z':
            a=a+1
        

        elif i>='0' and i<='9':
            n=n+1
            
            
        else:
            
            continue
    list=[a,n]
    print(list)
    

sentence("infosys 123")



def fpon(list1,n):
    count=0
    for i in list1:
        index=list1.index(i)+1
        for j in range(index,len(list1)):
            if i+list1[j]==n:
                count=count+1
                print((i,j))
    return count
print(fpon([1,2,7,4,5,6,0,3],6))



def index(st):
    if len(st)>2:
        s=st[0:2]+st[len(st)-2:len(st)]
        #s=st[0:2]+st[-2:]
        return s
    else:
        s=-1
print(index("w3schools"))



def fun(st):
    if len(st)<3:
        print(st)
    elif st[-3:]=='ing':
        print(st+'ly')

    elif st[-2:]=='ly':
        print(st+'ing')
    else:
        print(st+'ing')
    
    
fun("sleep")
fun("amazing")
fun("is")



 
def cd(num):
    count=0
    num1=num*2
    if len(str(num))==len(str(num1)):
        for i in str(num):
            for j in str(num1):
                if i==j:
                    
                    count+=1
        if count==len(str(num)):
            return True
        else:
            return False

print(cd(125874))



def avg(lt):
    avg1=0
    count=0
    for i in lt:
        avg1=avg1+i
    totavg=avg1/10
    for j in lt:
        if j>totavg:
            count=count+1
    return(100*count)/10
print(avg([12,18,25,24,2,5,18,20,20,21]))

def sort(lt):
    lt=list(lt)
    lt.sort()
    return lt
print(sort([12,18,25,24,2,5,18,20,20,21]))
            

def generate(lt):
    freq=[]
    for i in range(26):
        count=0
        for j in lt:
            if j==i:
                count+=1
        freq.append(count)
    return freq
print(generate([12,18,25,24,2,5,18,20,20,21]))




def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god","christmas":"jul","and":"och"}
list1=["merry","christmas"]
print(translate(dict1,list1))
    
    
        
        
            
n1=int(input(""))
n2=int(input(""))
"""res=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range()]"""
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print (result)
             
             

            
            
                

        
        
            
                   
                       


    
                    
                    
                   
        
        






