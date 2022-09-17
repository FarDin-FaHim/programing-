
print("-------- Midea Markt Shoping ---------------")
amount = int(input("Enter amount:  "))

if amount >= 3000:
    discount = amount * 0.09
    print(" this is your Discount (0,09%)=", discount)
elif amount >= 1500 and amount < 3000:
    discount = amount * 0.05
    print("This is your Discount (0.05%)= ", discount)

elif amount < 1500:
    discount = amount * 0.02
    print("This is your Discout (0.02%)=", discount)

print ( " ------------ End----------------------------")