Table_Number=input("Enter Table number that you want to display:")
num=int(Table_Number)
print("Multiplication Table for:",num)

#Iterate 10 times from i(if you want to print table for 10 times)
for i in range(1,11):
        print(num, "X", i, "=", num*i)