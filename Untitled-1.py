
a=input("")
e=""
o=""
for i in a:
    if int(i)%2==0:
        e=e+i
    elif int(i)%2!=0:
        o=o+i
    else:
        print("Invalid Input")
o=''.join(sorted(o))
e=''.join(sorted(''.join(e)))
print(e+o)

