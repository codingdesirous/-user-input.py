def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def main():
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price != original_price:
        print(f"The final price after applying {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print("No discount applied. Final price remains: ${:.2f}".format(final_price))

if __name__ == "__main__":
    main()

