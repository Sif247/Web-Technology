#try:  -> inside we have the code that can have errors
#except:  -> if we have errors, we have to do the instrutions inside here

try:
    i = 5 / 0
except:
    print("Error, you can't divide by 0")

#if we want just a one error to handle, we can specify like this


try:
    # IndexError
    a = [1, 2, 3]
    a[10] = 9
    #ZeroDivisionError
    i = 5 / 0

except ZeroDivisionError:
    print("Error, you can't divide by 0")
except IndexError:
    print("In this list there aren't so many elements")


#If I want to create my personal error, I can create the class/function error and with "raise" I can call it
def IfSameType(num, typeValue):
    if isinstance(num, typeValue):
        return f"the variable {num} is {typeValue}"
    else:
        raise TypeError(f"the variable {num} is not {typeValue}")

try:
    print(IfSameType(7, str))
except TypeError as e:
    print(f"Error {e}")
