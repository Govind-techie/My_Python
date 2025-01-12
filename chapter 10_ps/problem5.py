import random

name = input("Enter the name of train : ")
location = input("Enter your route : ")
fare_range1 = int(input("Enter the range 1 : "))
fare_range2 = int(input("Enter the range 2 : "))
seat_no = random.randint(1,100)
fare = random.randint(fare_range1,fare_range2)


class Train:
    
    def bookticket(self,train , route):
        self.train = train
        self.route = route
        print(f"The ticket is booked in train {train} from {route}")

    def getstatus(self,seat_no):
        self.seat_no = seat_no
        print(f"The seat no. you booked is : {seat_no = }")

    def fare(self,fare):
        self.fare = fare
        print(f"The total fare including 'GST' is : {fare}")

    
a = Train()
a.bookticket(name,location)
a.getstatus(seat_no)
a.fare(fare)


     

        


        
