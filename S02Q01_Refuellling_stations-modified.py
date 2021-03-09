Strt_Val = int(input("enter the Starting value of odometer: "))
End_Value = int(input("enter the Ending value of odometer: "))
Fuel_Con = int(input("enter number of liters consumed during this trip: "))

Distance_Travelled = End_Value - Strt_Val
Mileage = Distance_Travelled / Fuel_Con
print("Mileage per liter:", int(Mileage))

Total_Distance = 560
Tank_Capacity = int(input("enter tank capacity:"))

Required_fuel_Trip = Total_Distance / Mileage
print("print required fuel from blr to goa:",int(Required_fuel_Trip))

Refuel_Tank= Required_fuel_Trip / Tank_Capacity
print("Number of times refuel tank:", int(Refuel_Tank), "times")
