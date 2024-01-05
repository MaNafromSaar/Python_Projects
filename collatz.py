def collatz():
    n = 0
    try: 
        num =int(input("Please Enter a positive integer number and find it leading to 1 in some Steps. Can you guess them?"))
    
        if num <= 0:
            print ("Alas, this is not a viable input.")
            return
        while num != 1:
      
            if (num % 2) == 0:
                num = num/2
            else :
                num = 3 * num +1
            
            num = int(num)
        
            print (num)

            n += 1

        print ("It took this method", n,"steps to get this number down to 1.")
        
    except ValueError:
            print ("Are you sure, you know what an integer is?")   
            
collatz()
    
