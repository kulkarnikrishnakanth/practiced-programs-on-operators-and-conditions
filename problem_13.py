
quantity = float(input("enter no.of units required: "))
total_price = quantity * 100
if total_price > 1000:
    discount_obtained = 0.1 * total_price
    print(discount_obtained)
else:
    print("discont obtained is 0")

final_price = total_price - discount_obtained
print("final price is: ",final_price)
