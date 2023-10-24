capital = float(input("ingrese un capital a invertir "))
year = int(input("ingrese una cantidad de años a invertir "))
annual_interest = float(input("ingrese el interes anual "))
annual_investment = (capital*annual_interest*(365*year))/36500
print(annual_investment*1000)