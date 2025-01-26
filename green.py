corporate_values = [("Dollars", 1000), ("Profits", 2000), ("Control", 666)]
green = "yes"

def simulate_market():
    for corp, value in corporate_values:
        if corp.startswith("D"):
            value += 10  # S
        elif corp.startswith("P"):
            value += 500  # C
        elif corp.startswith("C"):
            value += 401  #O
        print(f"Monitoring {corp}: {value}")

def cannot_stop():
    global green
    if green == "yes":
        print("You cannot stop it.")

def open_dark_market():
    global green
    green = "dark"
    print("The market of evil opens for green.")

simulate_market()
cannot_stop()
open_dark_market()
