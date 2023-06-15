# Problem 2 Open the CupcakeInvoices.csv.
open_file = open("CupcakeInvoices.csv")
# Alternative 
# open_file = open("../CupcakeInvoice.csv")

# Problem 3 Loop through all the data and print each row.
# for row in open_file:
    # print(row)

# Problem 4 Loop through all the data and print the type of cupcakes purchased.
for line in open_file:
    line = line.rstrip('\n').split(',')
    print(line[2])

# Problem 5 Loop through all the data and print out the total for each invoice 
# (Note: this data is not provided by the csv, you will need to calculate it. 
# Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

open_file.seek(0)
for line in open_file:
    # print("inside")
    line = line.rstrip('\n').split(',')
    quantity = int(line[3])
    price = float(line[4])
    # print("Quanity:", quantity, "Price:", price)
    # print("here")
    invoice_total = round(quantity*price, 2)
    print("Invoice Total:", invoice_total)

#Problem 6 Loop through all the data, and print out the total for all invoices combined.

open_file.seek(0)

all_invoices = 0

for line in open_file:
    # print("inside")
    line = line.rstrip('\n').split(',')
    quantity = int(line[3])
    price = float(line[4])
    # print("Quanity:", quantity, "Price:", price)
    # print("here")
    all_invoices = round(all_invoices, 2) + round(quantity*price, 2)
    
print(all_invoices)



# Problem 7 Close your open file.
open_file.close()
print("File Closed")