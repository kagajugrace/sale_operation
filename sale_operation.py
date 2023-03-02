#read initial_stock and num_months from the user
initial_stock = int(input("Please enter an initial stock level: "))
num_months = int(input("Please enter the number of months to plan: "))

#declare a list to store number of months quantity
sales_quantity = []
for index in range(num_months):
    qty = int(input("Please enter the planned sales quantity: "))
    sales_quantity.append(qty)

#declare list which store result
production_quantity = []

#iterate quantities and calculate the production_quantity
for ind in sales_quantity:
    if initial_stock > ind:
        production_quantity.append(0)
        initial_stock = initial_stock - ind
    elif initial_stock < 0:
        production_quantity.append(ind)
    else:
        initial_stock = initial_stock - ind
        production_quantity.append(abs(initial_stock))
            
print()        
#print the result
i = 1
for x in production_quantity:
    print("Production quantity month", i, " - ", x)
    i = i+1