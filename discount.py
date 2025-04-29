def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        after_discount_percent = 100 - discount_percent
        discounted_price = price * (after_discount_percent / 100)
        return discounted_price
    else:
        return price
        
try:
    original_price = float(input("Enter original price: "))
    discount = float(input("Enter discount percentage: "))
    discounted_price = calculate_discount(original_price, discount)
    
    if discount >= 20:
        print("Discount applied, final price: $", discounted_price)
    else:
        print("final price: $" , original_price)
except:
    ValueError
    