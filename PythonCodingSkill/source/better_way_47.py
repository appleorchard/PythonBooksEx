from decimal import Decimal, ROUND_UP

rate = Decimal('1.45')
seconds = Decimal('222')
cost = rate * seconds / Decimal('60')
print(cost)

rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)

rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate * seconds / Decimal('60')
print(cost)
print(type(cost))

assert isinstance(cost, Decimal)
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)

print(rounded)
