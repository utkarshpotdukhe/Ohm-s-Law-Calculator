def calculate_ohms_law():
    print("Ohm's Law Calculator")
    print("Choose the value to calculate:")
    print("1. Voltage (V = I × R)")
    print("2. Current (I = V / R)")
    print("3. Resistance (R = V / I)")

    choice = input("Enter 1, 2, or 3: ")

    try:
        if choice == '1':  # Calculate Voltage (V)
            I = float(input("Enter current (I) in Amperes: "))
            R = float(input("Enter resistance (R) in Ohms: "))
            V = I * R
            print(f"Voltage (V) = {V:.2f} Volts")

        elif choice == '2':  # Calculate Current (I)
            V = float(input("Enter voltage (V) in Volts: "))
            R = float(input("Enter resistance (R) in Ohms: "))
            I = V / R
            print(f"Current (I) = {I:.2f} Amperes")

        elif choice == '3':  # Calculate Resistance (R)
            V = float(input("Enter voltage (V) in Volts: "))
            I = float(input("Enter current (I) in Amperes: "))
            R = V / I
            print(f"Resistance (R) = {R:.2f} Ohms")

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input! Please enter numerical values.")
    except ZeroDivisionError:
        print("Error! Current or Resistance cannot be zero.")

# Run the calculator
calculate_ohms_law()
