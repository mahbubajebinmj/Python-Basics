#Task 1: Variable Manipulation

def task1():
    name = " Jebin "
    age = "30"
    print("My name is " + name + " and " + " My age is " +  str(age))
task1()    

#Task 2: Data Types and Type Conversion

def task2():
    num1 = int(5)
    #print(type(num1))
    #print (num1)
    print(" num1: ", num1, " is " , type(num1) )


    num2 = float(5.03)
    #print(type(num2))
    #print (num2)
    print(" num2: ", num2, " is " , type(num2) )



    num1_float = float ( num1 )
    #print (type(num1_float))
    #print( num1_float )
    print("num1_float: ", num1_float, "is", type(num1_float) )
    
    num2_int = int ( num2)
    #print (type(num2_int))
    #print ( num2_int)
    print("num2_int: ", num2_int, "is", type(num2_int) )


task2()


#Task 3: String Manipulation



def task3():
    
    x = "Python programming is fun! "
    print( x )
    print ("length is:  " + str(len(x))) 
    print ("8th character of " + x + " is: " + str(x[8]))
    substring = x [0:5]
    print(" substring is:  " + substring)
    print ( " I enjoy it! " + substring )
task3()   




#Task 4: Lists and List Manipulation

def task4():
    list = [ "apple", "banana", "cherry", "date" ]
    print(list)
    list.append ("grape")
    print( " Add grape " + str(list))
    list.remove("banana")
    print(" after removing banana the list is:  " + str(list))
    print (" the length of the list: " + str(len(list)))
    sliced_fruits = (list[1:3])
    print("sliced fruits: " + str(sliced_fruits))
    extra_fruits = [ "kiwi" , " lemon "]
    combined_fruits = str(sliced_fruits)  +  str(extra_fruits)
    print ("combined list: " + str( combined_fruits) )
    

task4()



#Task 5: Conditional Statements

def task5():

    num = int (input("enter any number : "))
    if num % 2 == 0: 
        print (num, " is even ")
    else:
        print(num,  " is odd") 


task5()




#Task 6: Loops

def task6():

    
    for x in range (1,11):
    
        print((x))


        sum = 0
        firstnumber = 1
        secondnumber = 100

    for i in range(firstnumber,secondnumber+1):
        sum += i
    
    print("sum of 1 to 100 is =  " + str(sum)) 



        
task6()    



#Task 7: Functions
def task7():

    def calculate_square():
        calculate_square = int (input("enter any number : "))
        x = pow (calculate_square , 2 )
        print("square value is:  " + str (x))
    calculate_square()

    def is_prime(num):
        num = int ( input("enter a number: "))
        if num <= 1:
            return False
        for i in range (2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        print(num)
    number = 7 
    number2 = 29
    if is_prime(number2):
            print(number2,"is prime")
    else:
         print(number2,"is not")
    
    
     

task7()




# Task 8: Dictionaries

student = {
    "name": "Mahbuba Jebin",
    "age" : 30,
    "grade" : "A"
}
student["course"] = "Web Application"
print("Keys in the dictionary:", student.keys())
print("Key-value pairs in the dictionary:")
for key, value in student.items():
    print(key, ":", value)

