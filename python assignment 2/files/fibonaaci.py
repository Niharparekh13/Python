from base import assignment
# from ast import Num


class Fibonaaci(assignment):
    def run(self):
        num = int(input("enter the value:"))

        if num <= 0:
            print("Incorrect input")
        elif num == 1:
            return 0
        elif num == 2:
            return 1
        else:
            return (num-1)+(num-2)


# print(fibonaaci_number.run(num))
