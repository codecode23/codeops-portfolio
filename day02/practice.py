# Temprature label
temperature = float(input("Enter the temperature in celsius: "))
if temperature < 15:
       print(" cold ")
elif temperature >= 15 and temperature < 25:
       print(" warm ")
else:
       print(" hot ")

#Recipt Loop
for i in range(1,11):
    print(f"Recipet #{i}")
# Even numbers
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
# Discount Function
input_price = float(input("Enter the price: "))
def apply_discount(price,percent=0.1):
    discount=price * percent
    return price - discount
print(f"Price after discount: {apply_discount(input_price)}")
# Countdown Loop
count=5
while count>0:
    print(count)
    count -= 1
print("lift off  ")