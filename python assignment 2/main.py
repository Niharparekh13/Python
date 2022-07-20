from files.fibonaaci import Fibonaaci
from files.prime import Prime
from files.armstrong import Armstrong
import time


def time_wrap(ni):
    start_time = time.time()
    result= ni()
    print(result)
    end_time = time.time()
    print("total execution time:",end_time- start_time)
    return " "

@time_wrap
def option():
    print("Select the Option\n1.Fibonaaci\n2.Prime Number\n3.Armstrong")
    num = 0
    a = int(input("Enter the option you want:"))
    if (a == 1):
      return Fibonaaci.run(num)
      
    elif (a == 2):
     return Prime.run(num)
      
    elif (a == 3):
     return Armstrong.run(num)
    
    else:
      print("Invalid Number")
