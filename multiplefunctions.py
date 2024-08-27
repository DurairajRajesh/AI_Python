class multiplefunc():
    def OddEven():
        num = int(input("Enter a number:"))
        if num%2 == 0:
            value = "It is a Even number"
        else:
            value = "It is an Odd number"
        print(value)
        return value


    def Eligible():
        gender = input("Enter your Gender")
        Age = int(input("Enter your Age"))
        print("Your Gender:",gender) 
        print("Your Age:",Age)
        if Age<18:
            print("NOT ELIGIBLE")
            msg = "NOT ELIGIBLE"
        else:
            print("ELIGIBLE FOR MARRAGE")
            msg = "ELIGIBLE FOR MARRAGE"
        return msg

    def percentage():
        Subject1= 98 
        Subject2= 87 
        Subject3= 95 
        Subject4= 95 
        Subject5= 93 
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage =  Total / 5 
        print("Total is:", Total, "and Percentage is:", Percentage)
        return (Percentage)

    def Perimeter_of_Triangle():
        Height=32 
        Breadth=34 
        Area = (Height*Breadth)/2 
        print ("Area of Triangle:", Area) 
        Height1= 2 
        Height2=4 
        Breadth=4 
        Perimeter= Height1+Height2+Breadth 
        print ("Perimeter of Triangle:",  Perimeter )
        return Perimeter

