def currency_converter():
    print("------This program convert Tunisian Dinars to Euro:------")
    exchange_rate = 0.3
    amount_in_euro = float(input("Please enter the amount in Tunisian Dinars: "))
    amount_in_dinars = amount_in_euro * exchange_rate
    print(f"The amount in Euro: {amount_in_dinars:.2f}")
    
currency_converter()
