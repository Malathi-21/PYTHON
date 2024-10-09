class All_assignment():
    def age():
        age=int(input('enter your age:'))
        print('Age:',age)
        if age <18:
            print('Children')
        elif age <30:
            print('Adult')
        elif age <50:
            print('citizen')
        else:
            print('Senior citizen')
     
    def pos_neg():
        b=int(input('number:'))
        print('Enter any number:',b)
        if b >=0:
            print('No is Positive')
        else:
            print('No is Negative')
           
    def div_5():
        x=int(input('number:'))
        print('Enter a number to check:',x)
        if x%5 ==0:
            print('No is divisible by 5')
        else:
            print('No is not divisible by 5')

    def Subfields():
            i=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
            print('Sub-fields in AI are:')
            for j in i:
                print(j)

    def OddEven():
        num=int(input('number:'))
        print(f"enter the number: {num}")
        if num%2==0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")

    def Elegible():
        g=input('Your Gender:')
        a=int(input('Your Age:'))
        print('Your Gender:',g)
        print('Your Age:',a)
        if g=='Male':
            if a <21:
                print("NOT ELIGIBLE")
            else:
                print('ELIGIBLE')
        else:
            if a >=18:
                print("ELIGIBLE")
            else:
                print('NOT ELIGIBLE')

    def student():
        lis=[98,87,95,95,93]
        print(f'Subject1= {lis[0]}')
        print(f'Subject2= {lis[1]}')
        print(f'Subject3= {lis[2]}')
        print(f'Subject4= {lis[3]}')
        print(f'Subject5= {lis[4]}')
        total=0
        for i in lis:
            total +=i
        print('Total:',total)
        Percentage =(total/500)*100
        print('Percentage :',Percentage) 

    def triangle():
        H=32
        B=34
        area=(H*B)/2
        print('Height:',H)
        print('Breadth:',B)
        print('Area formula: (Height*Breadth)/2')
        print('Area of Triangle:',area)
        h1=2
        h2=4
        b=4
        perimeter=(h1+h2+b)
        print('Height1:',h1)
        print('Height2:',h2)
        print('Breadth:',b)
        print('Perimeter formula: Height1+Height2+Breadth')
        print('Perimeter of Triangle:',perimeter)    

            