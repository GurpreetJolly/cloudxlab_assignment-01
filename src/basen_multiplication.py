import logging
from basen_addition import add_numbers
from basen_next_number import create_symbols_for_base, find_next_number, is_valid_number

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def main():
    print("\n*** This app multiply 2 numbers of given base ***")
    base = int(input("Enter a number for base (e.g. for base-12 enter 12): "))
    base_symbols = create_symbols_for_base(base)
    if not base_symbols:
        _logger.error(f"Base symbols could not be created for base '{base}'. Cannot continue")
        return False

    number_1 = str(input("Enter first number for multiplication (the number should be combination of one or more base symbols): "))
    if not is_valid_number(base_symbols, number_1):
        print(f"Error: The number '{number_1}' is not valid for base {base}")
    else:
        number_2 = str(input("Enter second number for multiplication (the number should be combination of one or more base symbols): "))
        if not is_valid_number(base_symbols, number_2):
            print(f"Error: The number '{number_2}' is not valid for base {base}")
        else:
            result = multiply_numbers(base_symbols, number_1, number_2)
            print(f"The result of multiplication of '{number_1}' and '{number_2}' in base-{base} is: {result}")
            return True
    return False


def multiply_numbers(base_symbols:list, number_1:str, number_2:str) -> str:
    """Multiply two numbers in a given base using repeated addition."""

    result = '0'
    for _ in range(int(number_2, len(base_symbols))):
        result = add_numbers(base_symbols, result, number_1)
    return result

if __name__ == "__main__":
    main()
