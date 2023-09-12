money = float(input('How much money do you have? '))
convertion = money / 4.98
print(f'With R${money:.2f} you can pick up US${convertion:.2f}')
# another way to do the same thing following bellow:
# print('With R${:.2f} you can pick up US${:.2f}!'.format(money, conversion))
