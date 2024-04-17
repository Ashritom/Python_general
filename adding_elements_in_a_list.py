elements = []
while True:
    item = input("Enter an item (or 'exit' to quit): ")
    if item.lower() == "exit":
        break
    elements.append(item)
print("List:", elements)
