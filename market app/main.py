import time
import webbrowser

#name login
name = input("type your name:")
time.sleep(1)
print("Welcome To Market App", name)
#Orders
print("-----------Orders---------------")
print("Apple", "oranges","mango","banana","dragon","carrote")
#Choose And Buy
chosse = input ("Type here your order:")
print("Your order is ready to show your oder type order")

user_input = input()
if user_input.lower() == "order":
    print(chosse)