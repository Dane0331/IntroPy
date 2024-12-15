#Dynamic_protocol.py version 1 by JDE
def main():
    try:
        # Calculation variables, similar to our previous lab's inputs but adapted to the provided code
        final_vol = float(input("Please enter the final volume of the solution (ml): "))
        nacl_stock = float(input("Please enter the NaCl stock (mM): "))
        nacl_final = float(input("Please enter the NaCl final (mM): "))
        mg_stock = float(input("Please enter the MgCl2 stock (mM): "))
        mg_final = float(input("Please enter the MgCl2 final (mM): "))

        # Calculating the volumes needed with the given formulas (concatenation portion of the provided protocol.py), used 3 decimal points
        try:
            step1 = f"Add {final_vol * (nacl_final / nacl_stock):.3f} ml NaCl\n"
            step2 = f"Add {final_vol * (mg_final / mg_stock):.3f} mg MgCl2\n"
            step3 = f"Add water to a final volume of {final_vol:.3f} ml and mix"

            print(step1 + step2 + step3)

        except ZeroDivisionError: #added ZeroDivisionError in case of zero value inputs for the stock conc.
            print("Your input included a stock concentration of zero, try again with a non-zero value for stock concentration.")

    except ValueError: #added ValueError in case of non-numeric value inputs
        print("Your input may have included invalid characters. Please enter numeric values only")

if __name__ == "__main__":
    main()