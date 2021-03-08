x=int(input("enter the Starting value of odometer: "))
y=int(input("enter the Ending value of odometer: "))
z=int(input("enter number of liters consumed during this trip: "))

Total_Distance_Travelled=y-x
Mileage=Total_Distance_Travelled/z
print("Mileage per liter:", int(Mileage))