largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num1 = float(num)
        while largest is None or num1 > largest:
        	largest = num1
        while smallest is None or num1 < smallest:
            smallest = num1
       
            
        
    except:
        print ("Invalid input")
        continue

   

print ("Maximum is", int(largest))
print ("Minimum is", int(smallest))
