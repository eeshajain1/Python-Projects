# Python-Projects
#This repository includes projects done in the language python

#Eesha Jain


def main() : 
    print("This program calculates the future balance of a 10-year investment. ")
    principal = eval(input("Enter the initial investment (> $1000): "))
    pay_period = eval(input("Enter the number of compounding periods each year(1,2,3,4,6): "))
    apr = eval(input("Enter the annual interest rate ( < 1): " ))
    interest_adjustment = eval(input("Enter the interest adjustment for each period ( <1): ")) #Question number 2
    
    period = 0
    interest = 0
    temp = interest_adjustment #sets a varaible called temp equal to the original intrest adjustment
    total_periods = pay_period * 10
    
    for i in range(10): #10 years
        
        for j in range(pay_period): #for each year, there are this many pay periods 
            
            principal = (principal + (principal * (apr/(pay_period))))
           
            period = period + 1 #prints out the period number by setting a counter
            
            if (period <= (total_periods/2 - 1) and period != 1): #adds intrest adjustment for the first five years
                 interest_adjustment = interest_adjustment + temp
                 
            elif(period >= (total_periods/2)): #subtracts the intrest adjustment after the first five years
                 interest_adjustment = interest_adjustment - temp
        
            principal = principal + interest #final principal amount after interest and apr
            
            print("The balance after period", period, "is $", principal)
            
            interest = principal * interest_adjustment #calculates total intrest
    print()        
    print("The final balance after 10 years is $", principal)  #Question number 3
         
main()
