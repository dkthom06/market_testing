import robin_stocks as r

login = r.login('dkthom06@gmail.com', 'J2Q6zOfq@-5!Upr')

# Now you can call build_holdings
my_stocks = r.build_holdings()
for key, value in my_stocks.items():
    print(key, value)
