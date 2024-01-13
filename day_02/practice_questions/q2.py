#Write a program to calculate the total cost of items including tax


num_items = int(input("Enter the number of items: "))
cost_per_item = float(input("Enter the cost per item: $"))

total_cost_before_tax = num_items * cost_per_item

tax_rate = 0.1
tax_amount = total_cost_before_tax * tax_rate

total_cost_after_tax = total_cost_before_tax + tax_amount

print("\nResults:")
print("Total cost before tax: ${:.2f}".format(total_cost_before_tax))
print("Tax amount (10%): ${:.2f}".format(tax_amount))
print("Total cost after tax: ${:.2f}".format(total_cost_after_tax))