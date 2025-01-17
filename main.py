import time
my_time=int(input("Enter the time in seconds:"))

hours=int(my_time/3600)
minute=int((my_time%3600)/60)
seconds=int(my_time % 60)

while(hours>=0):
    
    
    while(minute>=0):
        
        while (seconds>=0):
            print(f"{hours}:{minute}:{seconds}", end="\r")
            seconds-=1
            time.sleep(1)
            
            

        seconds=59

        minute-=1
        
    minute=59

    hours-=1
