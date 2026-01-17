import logging
from basen_next_number import create_symbols_for_base, find_next_number, is_valid_number

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    print("\n*** This app adds 2 numbers of given base ***")
    base = int(input("Enter a number for base (e.g. for base-12 enter 12): "))
    base_symbols = create_symbols_for_base(base)
    if not base_symbols:
        logger.error(f"Base symbols could not be created for base '{base}'. Cannot continue")
        return False

    number_1 = str(input("Enter first number for addition (the number should be combination of one or more base symbols): "))
    if not is_valid_number(base_symbols, number_1):
        logger.error(f"The number '{number_1}' is not valid for base {base}")
    else:
        number_2 = str(input("Enter second number for addition (the number should be combination of one or more base symbols): "))
        if not is_valid_number(base_symbols, number_2):
            logger.error(f"The number '{number_2}' is not valid for base {base}")
        else:
            result = add_numbers(base_symbols, number_1, number_2)
            print(f"The result of addition of '{number_1}' and '{number_2}' in base-{base} is: {result}")    


def add_numbers(base_symbols:list, number_1:str, number_2:str) -> str:
    sum = number_1
    for i in range(int(number_2, len(base_symbols))):
        sum = find_next_number(base_symbols, sum)
    return sum


if __name__ == "__main__":
    main()
