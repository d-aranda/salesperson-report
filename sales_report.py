"""Generate sales report showing total melons each salesperson sold."""


# salespeople = []
# melons_sold = []

# f = open('sales-report.txt')

# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')
#     salesperson = entries[0]
#     melons = int(entries[2])
# ## splitting each line at the "|" and adding variables

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons

        
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')


### Refactored ###


def sales_by_melons(file):
   
    sales_qty = {}
    file = open(file)

    for line in file:

        line = line.rstrip()
        salespeople, price, qty = line.split("|")
        
        if salespeople in sales_qty:
            sales_qty[salespeople] += int(qty)
        else:
            sales_qty[salespeople] = int(qty)

    return sales_qty


def print_sales(sales_qty):
    for name, sold in sales_qty.items():
        print(f"{name} sold {sold}")

        


sales_qty = sales_by_melons("sales-report.txt")
    
print_sales(sales_qty)








