def compare_values(First_Number, Second_Number):
    # Check if both inputs are numbers (int or float)
    if not isinstance(First_Number, (int, float)) or not isinstance(Second_Number, (int, float)):
        print("Error: Both inputs must be numbers.")
        return "Invalid input"
    
    # Case 1: Both numbers are greater than zero
    if First_Number > 0 and Second_Number > 0:
        # If First_Number is greater, print it Second_Number times
        if First_Number > Second_Number:
            for i in range(Second_Number):
                print(First_Number)
        # If Second_Number is greater or equal, print it First_Number times
        else:
            for j in range(First_Number):
                print(Second_Number)

    #Case 2: Either number is zero
    elif First_Number == 0 or Second_Number == 0:
        print("Zero found")
        return "Zero found"

    #Case 3: At least one number is negative
    else:
        # If First_Number is less than Second_Number, subtract Second_Number from First_Number
        if First_Number < Second_Number:
            result = First_Number - Second_Number
        # Otherwise, subtract First_Number from Second_Number
        else:
            result = Second_Number - First_Number
        print(result)
        return result





      

#code tests
compare_values(-1,3)
compare_values(3,0)
compare_values(1,5)
compare_values(5,1)
compare_values(3,-5)
compare_values(d,3)
compare_values(3,d)