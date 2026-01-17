import logging
from basen_multiplication import create_symbols_for_base, multiply_numbers
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def main():
    print("\n*** This app prints tables of given base ***")
    base = int(input("Enter a number for base (e.g. for base-12 enter 12): "))
    base_symbols = create_symbols_for_base(base)
    if not base_symbols:
        _logger.error(f"Base symbols could not be created for base '{base}'. Cannot continue")
        return False
    else:
        print(f"Tables for base-{base} are:")
        for i in range(base):
            number = base_symbols[i]
            for j in range(1, base):
                multiplier = base_symbols[j]
                product = multiply_numbers(base_symbols, number, multiplier)
                print(f"{number} x {multiplier} = {product}")
            print("")
        return True

if __name__ == "__main__":
    main()
