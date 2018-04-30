 
num=0

while (num<=100):
    print(num)
    num+=1
    if(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
        continue
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
