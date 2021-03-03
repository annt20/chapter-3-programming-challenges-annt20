quantity = int(input('Enter the number of packets purchased: '))
rate = int
unit_price = 99
total = 0
if quantity >= 100:
    rate = 40
elif quantity >= 50:
    rate = 30
elif quantity >= 20:
    rate = 30
elif quantity >= 10:
    rate = 20
else:
    rate = 0
discount = (rate/100) * quantity * unit_price
total = quantity * unit_price - discount
print('The amount of discount ', rate, '%')
print('Total amount after discount: %.2f' % total)
