for x in range (0,151):
    print(x)


for x in range(5,1001,5):
        print(x)


for x in range(0, 101):
    if (x % 10 == 0):
        print("Coding dojo")

    elif (x % 5 == 0):
        print("Coding")
    else:
        print(x)


for x in range(1,500001):
    if(x % 2 !=0):
        print(x)


for x in range(2018):
    if(x % 4==0):
        print(x)

low_num =2
high_num =9
mult =3 

for x in range(low_num, high_num + 1):
    if (x % mult == 0):
     print(x)