try:
    result = 10 + 20
    print(result)
except:
    print("it looks like something went wrongg!!!!!!")
else:
    print("successfully completed")


try:
    f = open('textfilw','w')
    f.wrirte("iam writing a line here")
except TypeError:
    print("there was a type error")
except OSError:
    print("you have an os error")
finally:
    print("i always run")


def userinput():
    while True:
        try:
            result = int(input("enter a number"))
        except:
            print("enter a valid number")
            continue
        else:
            print("input is successful")
            break
        finally:
            print("i always run")
    
userinput()
    

for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("there is a type error")


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("can't print a number with zero")
finally:
    print("I always run")
