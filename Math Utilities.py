#CALCULATOR WHICH CALCULATES AGGREGATES OF DIFFERENT UNIVERSITIES, BASIC ARITHMETIC OPERATIONS AND SOME UNIT CONVERSIONS.




f = open("Start.txt", "r")
print(f.read())

def operator(c):
    while c != "+" and c != "-" and c != "*" and c != "/" and c != "P" and c != "p" and c != "Avg" and c != "avg" \
            and c != "UET S" and c != "uet s" and c != "Uet S" and c != "UET" and c != "uet" and c != "Uet" \
            and c != "Pucit" and c != "PUCIT" and c != "pucit" \
            and c != "Umt" and c != "UMT" and c != "umt" \
            and c != "cm" and c != "CM" and c != "Cm" and c != "Foot" and c != "foot" and c != "FOOT" \
            and c != "c" and c != "C" and c != "F" and c != "f" \
            and c != "KPH" and c != "kph" and c != "Kph" and c != "MPH" and c != "Mph" and c != "mph"\
            and c != "1" and c != "2" and c != "3" and c != "4" and c != "5" and c != "6" and c != "7"\
            and c != "8" and c != "9" and c != "10" and c != "11" and c != "12" and c != "13" and c != "14"\
            and c != "15" and c != "16" :

        print("You have entered wrong word or operation ")

        c = input("Enter what you want to perform. Please Choose the relevant number :\n1. Addition +     2. Subtraction -    3. Multiplication * "
                         "  4. Division /   5. Power P    6. Average Avg\n"
                         "7. UET Aggregate   " 
                         "8. PUCIT Aggregate  "
                         "9. UMT Aggregate  \n"
                         "10. cm To Foot  "
                         "11. Foot To cm  "
                         "12. Celsius To Fahrenheit  "
                         "13. Fahrenheit To Celsius  "
                         "14. Kph To Mph  "
                         "15. Mph To Kph\n")
    return c


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


def Compute_speed_in_MPH(x):
    return x * 0.621371


def Compute_speed_in_KPH(x):
    return x * 1.60934


def Compute_height_in_foot(x):
    return x * 0.0328084


def Compute_height_in_cm(x):
    return x * 30.48


def Compute_temperature_in_Fahrenheit(x):
    return (x * 9 / 5) + 32


def Compute_temperature_in_Celsius(x):
    return (x - 32) * 5 / 9


def question_option():
    inp_Operator = input("Do you want to perform another task? If yes, then press Y else press anyother key.")
    if (inp_Operator == "y" or inp_Operator == "Y"):
        question_again()
    else:
        print("Thanks for using my program!!")


def question_again():
    inp_Operator = input("Enter what you want to perform. Please Choose the relevant number :\n1. Addition +     2. Subtraction -    3. Multiplication * "
                         "  4. Division /   5. Power P    6. Average Avg\n"
                         "7. UET Aggregate   " 
                         "8. PUCIT Aggregate  "
                         "9. UMT Aggregate  \n"
                         "10. cm To Foot  "
                         "11. Foot To cm  "
                         "12. Celsius To Fahrenheit  "
                         "13. Fahrenheit To Celsius  "
                         "14. Kph To Mph  "
                         "15. Mph To Kph\n")
    Operation = operator(inp_Operator)
    Operations(Operation)
    print(inp_Operator)



def Operations(operator):
    if operator == "+" or operator == "1" :
        Num1 = int(input("Enter the first number:"))
        Num2 = int(input("Enter the second number:"))
        sum = add(Num1, Num2)
        print(sum)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "-" or operator == "2" :
        Num1 = int(input("Enter the first number:"))
        Num2 = int(input("Enter the second number:"))
        subtraction = subtract(Num1, Num2)
        print(subtraction)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "*" or operator == "3":
        Num1 = int(input("Enter the first number:"))
        Num2 = int(input("Enter the second number:"))
        multiplication = multiply(Num1, Num2)
        print(multiplication)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "/" or operator == "4":
        Num1 = int(input("Enter the first number:"))
        Num2 = int(input("Enter the second number:"))
        division = divide(Num1, Num2)
        print(division)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "P" or operator == "p" or operator == "5":
        Num1 = int(input("Enter the first number:"))
        Num2 = int(input("Enter the second number:"))
        Exponent = power(Num1, Num2)
        print(Exponent)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "Avg" or operator == "avg" or operator == "6":
        Num1 = int(input("Enter the first number:"))
        Num2 = int(input("Enter the second number:"))
        sum = add(Num1, Num2)
        Avg = divide(sum, 2)
        print(Avg)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()



    if operator == "UET" or operator == "Uet" or operator == "UET" or operator == "uet s" or operator == "7":

        Num_1 = int(input("FSc Marks Obtained:"))
        Num_2 = int(input("FSc Total Marks:"))



        #f=open("Talha.txt","r+")
        #a=f.readlines()
        #for x in a:
        #    print(x)


        FSC_Percent = Num_1 / Num_2 * 70
        print("FSc Percentage (70 Percent):", FSC_Percent)

        Num_3 = int(input("ECAT Marks Obtained:"))
        Num_4 = int(input("ECAT Total Marks:"))

        ECAT_Percent = Num_3 / Num_4 * 30
        print("ECAT Percentage (30 Percent):", ECAT_Percent)

        Total_aggregate = FSC_Percent + ECAT_Percent
        print("AGGREGATE:", Total_aggregate)

        data=str(Total_aggregate)
        f=open("Uet_RESULTS.txt", "a")
        f.write(data + "\n")
        f.close()

        if Total_aggregate > 70:
           print("CONGRATULATIONS!\n"
                    "You are eligible to get the Admission in UET.")
        else:
          print("SORRY!\n"
                 "You are not eligible to get Admission.")

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "PUCIT" or operator == "pucit" or operator == "Pucit" or operator == "8":

        Num_1 = int(input("FSc Marks Obtained:"))
        Num_2 = int(input("FSc Total Marks:"))

        FSC_Percent = Num_1 / Num_2 * 70

        print("FSc Percentage (70 Percent will be count):", FSC_Percent)

        Num_3 = int(input("Matric Marks Obtained:"))
        Num_4 = int(input("Matric Total Marks:"))

        Matric_Percent = Num_3 / Num_4 * 30
        print("Matric Percentage (30 Percent will be count):", Matric_Percent)

        Total_aggregate = FSC_Percent + Matric_Percent
        print("AGGREGATE:", Total_aggregate)

        data = str(Total_aggregate)
        f = open("Pucit_RESULTS.txt", "a")
        f.write(data + "\n")
        f.close()

        if Total_aggregate > 95 and Total_aggregate <= 96:
             print("You will be eligible to get admission in Data Science")
        else:
             print("SORRY! You will not be eligible for admission")

        if Total_aggregate > 96 and Total_aggregate <= 100:
            print("You will be eligible to get admission in IT, Software Engineering, and in Computer Science")

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()





    if operator == "UMT" or operator == "Umt" or operator == "umt" or operator == "9":
          Num_1 = int(input("FSc Marks Obtained:"))
          Num_2 = int(input("FSc Total Marks:"))

          FSC_Percent = Num_1 / Num_2 * 50
          print("FSc Percentage (50 Percent will be count):", FSC_Percent)

          Num_3 = int(input("Matric Marks Obtained:"))
          Num_4 = int(input("Matric Total Marks:"))

          Matric_Percent = Num_3 / Num_4 * 20
          print("Matric Percentage (20 Percent will be count):", Matric_Percent )

          Num_5 = int(input("Entry Test Marks Obtained:"))
          Num_6 = int(input("Entry Test Total Marks:"))

          Entry_Test_Percent = Num_5 / Num_6 * 30
          print("Entry Test Percentage (30 Percent will be count):", Entry_Test_Percent)

          Total_aggregate = FSC_Percent + Matric_Percent + Entry_Test_Percent
          print("AGGREGATE:", Total_aggregate)

          data = str(Total_aggregate)
          f = open("Umt_RESULTS.txt", "a")
          f.write(data + "\n")
          f.close()

          if Total_aggregate > 70 and Total_aggregate <= 100:
                print("You will be eligible to get admission in UMT")
          else:
             print("SORRY! You will not be eligible for admission")

          g = open("After Result Text.txt", "r")
          print(g.read())

          question_option()




    if operator == "cm" or operator == "CM" or operator == "Cm" or operator == "10":
        Num_1 = float(input("Enter Height in Centimeters:"))
        Height_in_foot = Compute_height_in_foot(Num_1)
        print("Height in Foot:", Height_in_foot)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "Foot" or operator == "FOOT" or operator == "foot" or operator == "11":
        Num_1 = float(input("Enter Height in Foot:"))
        Height_in_cm = Compute_height_in_cm(Num_1)
        print("Height in cm:", Height_in_cm)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "c" or operator == "C" or operator == "12":
        Num_1 = float(input("Enter temperature in Celsius:"))
        Temp_in_fah = Compute_temperature_in_Fahrenheit(Num_1)
        print("Temperature in Fahrenheit:", Temp_in_fah)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "f" or operator == "F" or operator == "13":
        Num_1 = float(input("Enter temperature in Fahrenheit:"))
        Temp_in_celsius = Compute_temperature_in_Celsius(Num_1)
        print("Temperature in Celsius:", Temp_in_celsius)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "KPH" or operator == "Kph" or operator == "kph" or operator == "14":
        Num_1 = float(input("Enter Speed in KPH:"))
        speed_mph = Compute_speed_in_MPH(Num_1)
        print("Speed in MPH:", speed_mph)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


    if operator == "mph" or operator == "MPH" or operator == "Mph" or operator == "15":
        Num_1 = float(input("Enter Speed in MPH:"))
        speed_kph = Compute_speed_in_KPH(Num_1)
        print("Speed in KPH:", speed_kph)

        g = open("After Result Text.txt", "r")
        print(g.read())

        question_option()


question_again()


