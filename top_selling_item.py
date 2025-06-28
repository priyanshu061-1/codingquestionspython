def top_selling_item(n):
    item_sales = {}
    
    # Input loop
    for i in range(n):
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        total_price = quantity * price
        item_sales[item] = item_sales.get(item, 0) + total_price

    total = 0
    max_cost = 0
    max_cost_item = None

    # Determine max and total
    for item, cost in item_sales.items():
        total += cost
        if cost > max_cost:
            max_cost = cost
            max_cost_item = item

    avg = total / n

    print("Top Selling Item:", max_cost_item)
    print("Average Total Price:", avg)
    print("Total Revenue:", total)

# Example usage
n = 3
top_selling_item(n)
