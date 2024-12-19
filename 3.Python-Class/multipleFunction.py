class cls_multipleFun():
    def Subfields_1():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
       
            
    def checkOddEven():
        num=int(input("Enter the number"))
        if(num%2)==1:
            print("odd")
            message="Odd numer"
        else:
            print("even")
            message="Even number"
            return message

    def Elegible():
            gender = input("Your Gender :").upper()
            age = int(input("Your Age:"))
            if gender == "MALE" and age < 21 :
                print("NOT ELIGIBLE")
            elif gender =="MALE" and age >21:
                print("ELIGIBLE")
            elif gender == "FEMALE" and age < 18 :
                print("NOT ELIGIBLE")
            elif gender =="FEMALE" and age >18:
                print("ELIGIBLE")

    def percentage():
        Subject1 = int(input("Subject1= "))
        Subject2 = int(input("Subject2= "))
        Subject3 = int(input("Subject3= "))
        Subject4 = int(input("Subject4= "))
        Subject5 = int(input("Subject5= "))
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage= (Total / 500) * 100
        #Percentage1 = "{:.2f}".format(Percentage) # percentage in 2 decimal
        #print(Percentage1)
        print("Total :" ,Total)
        print("Percentage :" ,Percentage)
        
    def triangleArea(Height:int, Breadth:int):
        print ("Height :" ,Height)
        print("Breadth:",Breadth)
        area = (Height*Breadth)/2
        print( "Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",area)

    def trianglePeri(Height1,Height2,Breadth): 
        print ("Height1 :",Height1)
        print ("Height2 :",Height2)
        print("Breadth:",Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1+Height2+Breadth
        print("Perimeter of Triangle: ", Perimeter)

    def BMI():
        bmi =float(input("Enter the BMI Index:"))
        if bmi < 18.5:
            print("You are underwight.")
            result="underwight"
        elif bmi < 25:
            print("You are Normalwight.")
            result="Normalwight"
        elif bmi < 33:
            print("Youare slightly overweight")
            result="overweight"
        else:
            print("Very Overweight")
            result="Very Overweight"
    
        return result

        
        
    
    