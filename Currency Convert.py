import os
import time
print('''
********WELCOME TO CURRENCY CONVERT********


''')
currency={'USD':1.0,
              'EUR': 0.85,
              'EGP': 30.9,
              'RMB': 6.5}
def convert(aCCF,CCF,CCT):
    return (aCCF*currency[CCT])/currency[CCF]

while True:
    print('\n'.join(currency))
    CCF=input('Choose a currency to convert from: ').upper()
    while CCF not in currency:
        CCF=input('invalid currency,Choose a currency to convert from: ').upper()
    amount=float(input('Enter the amount: '))
    check=input(f'You entered {amount} {CCF}. Confirm? (Y/N): ').lower()
    while check !='y':
        amount=float(input('Enter the amount: '))
        check=input(f'You entered {amount} {CCF}. Confirm? (Y/N): ').lower()
    os.system('cls')
    CCT=input('Choose a currency to convert to: ').upper()
    while CCT not in currency:
        CCT=input('invalid currency,Choose a currency to convert to: ').upper()
    print('checking ....')
    time.sleep(2)
    print('converting... please waite')
    time.sleep(2)
    total=convert(amount,CCF,CCT)
    print(f'{amount} {CCF} is equal to {total} {CCT}')
    what=input('Do you want to contanue? (Y/N): ').lower()
    if what =='n':
        break
    else:
        os.system('cls')