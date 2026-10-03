"""
Interactive Calculator & Unit Converter
A beginner-friendly (but complete) CLI tool for:
  - Arithmetic operations
  - Currency conversion (static rates)
  - Unit conversion (length, weight, temperature)
"""
 
# ---------------------------------------------------------------------------
# ARITHMETIC
# ---------------------------------------------------------------------------

def calculator(a,x,b):
    if x=='+':
        return a+b
    elif x=='-':
        return a-b
    elif x=='*':
        return a*b
    elif x=='/':
        if b==0:
            raise ZeroDivisionError("Cannot divisible by zero")
        return a/b
    elif x=='%':
        return a%b
    elif x=='**':
        return a**b
    else:
        raise ValueError(f"Invalid Operator {x}")

def run_cal():
    print("\n---------- ARITHMETIC OPERATOR FUNCTION-----------")
    print("Operators to Use= +,-,*,/,%,**" )
    try:
        a=float(input("Enter the First Number: "))
        x=input("Enter the Operator (in sign) : ")
        b=float(input("Enter the Second Number: "))
        result=calculator(a,x,b)
        print(f"Result= {a} {x} {b} = {result}")
    except ValueError as e:
        print(f"Invalid input {e}")
    except ZeroDivisionError as z:
        print(f"Invalid Math Error {z}")

# ---------------------------------------------------------------------------
# UNIT CONVERSiON
# ---------------------------------------------------------------------------

UNIT_CAT={
    "length":{
        "base":"m","units":{"m":1,"km":1000,"cm":0.01,"mm":0.001,"inch":0.0254,"foot":0.3048,"yard":0.9144,"miles":1609.344}
    },
    "weight":{
        "base":"kg","units":{"kg":1,"g":0.001,"mg":0.000001,"lb":0.453592,"oz":0.0283495}
    },
}

def convert_sim(value, from_unit,to_unit,category):
    units=UNIT_CAT[category]["units"]
    if from_unit not in units or to_unit not in units:
        raise ValueError(f"Unknown Unit for {category}")
    base_value=value*units[from_unit]
    return base_value/units[to_unit]

def temperature_convert(value,from_unit,to_unit):
    from_unit=from_unit.lower()
    to_unit=to_unit.lower()
    valid={"c","f","k"}
    if from_unit not in valid or to_unit not in valid:
        raise ValueError("Temperature Value must be in c,f,k")

    if from_unit=="c":
        celsius=value
    elif from_unit=="f":
        celsius=(value-32)*5/9
    else:
        celsius=value-273.15

    if to_unit=="c":
        return celsius
    elif to_unit=="f":
        return celsius*9/5+32
    else:
        return celsius+273.15

def run_unit_con():
    print("\n-----Unit Conversion-----")
    print("Categories: length, weight, temperature")
    c=input("Choose a category: ").strip().lower()
 
    try:
        if c=="temperature":
            value=float(input("Enter Value: "))
            from_unit=input("Your Value Type (c,f,k): ").strip()
            to_unit=input("Result Value Type (c,f,k): ").strip()
            result=temperature_convert(value,from_unit,to_unit)

        elif c in UNIT_CAT:
            units=UNIT_CAT[c]["units"]
            print(f"Available units:",",".join(units))
            value=float(input("Enter Value: "))
            from_unit=input("Your Value Type: ").strip()
            to_unit=input("Result Value Type: ").strip()
            result=convert_sim(value,from_unit,to_unit,c)

        else:
            print("Unknown Category.")
            return
        print(f"Result: {value} {from_unit} = {result:.4f}{to_unit}")
    except ValueError as e:
        print(f"Invalid input: {e}")


# ---------------------------------------------------------------------------
# CURRENCY CONVERSION
# ---------------------------------------------------------------------------

from currency_converter import CurrencyConverter

_currency_converter = CurrencyConverter()
 
def convert_currency(amount, from_cur, to_cur):
    from_cur = from_cur.upper()
    to_cur = to_cur.upper()
    if from_cur not in _currency_converter.currencies or to_cur not in _currency_converter.currencies:
        raise ValueError("Unsupported currency.")
    return _currency_converter.convert(amount, from_cur, to_cur)

def run_currency_conversion():
    print("\n--- Currency Conversion ---")
    try:
        amount = float(input("Enter amount: "))
        from_cur = input("From currency (e.g. INR,USD,JPY,GBP,etc): ").strip().upper()
        to_cur = input("To currency (e.g. INR,USD,JPY,GBP,etc): ").strip().upper()

        result = convert_currency(amount, from_cur, to_cur)
        print(f"{amount} {from_cur} = {result:.2f} {to_cur}")
    except ValueError as e:
        print(f"Invalid input: {e}")

# ---------------------------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------------------------
 
def print_menu():
    print("\n" + "=" * 40)
    print("  Interactive Calculator & Converter")
    print("=" * 40)
    print("1. Arithmetic")
    print("2. Currency Conversion")
    print("3. Unit Conversion")
    print("4. Exit")
 
 
def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()
 
        if choice == "1":
            run_cal()
        elif choice == "2":
            run_currency_conversion()
        elif choice == "3":
            run_unit_con()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-4.")
 
 
if __name__ == "__main__":
    main()