import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    print("Finding next number in given base")
    base = int(input("Enter a number for base e.g. for base-12 enter 12: "))
    base_symbols = create_symbols_for_base(base)
    if base_symbols is None:
        logger.error(f"Base symbols could not be created for base '{base}'.")
        return None

    number = str(input("Enter a number that you want to increment (the number should be combination of one or more base symbols): "))

    if not is_valid_number(base_symbols, number):
        logger.error(f"The number '{number}' is not valid for base {base}")
        return -1
    else:
        print (find_next_number(base_symbols, number))
        return 0


def is_valid_number(base_symbols, number):
    for d in number:
        logger.debug("Checking digit: %s", d)
        if d not in base_symbols:
            logger.error(f"Digit '{d}' not valid for base with symbols {base_symbols}")
            return False
    return True


def create_symbols_for_base(base):
    if base <= 10:
        logger.debug("Using digits 0-9 for base %d", base)
        base_symbols = [str(i) for i in range(base)]
        #base_symbols = list(range(base))
    elif base > 10 and base <= 36:
        logger.debug("Using digits 0-9 and letters A-Z for base %d", base)
        base_symbols = [str(i) for i in range(10)]
        base_symbols += [chr(i) for i in range(ord('A'), ord('A') + (base-10))]
    elif base > 36 and base <= 62:
        logger.debug("Using digits 0-9, letters A-Z and a-z for base %d", base)
        base_symbols = [str(i) for i in range(10)]
        base_symbols += [chr(i) for i in range(ord('A'), ord('A') + 26 if base > 36 else (base - 10))]
        base_symbols += [chr(i) for i in range(ord('a'), ord('a') + (base-36))]
    else:
        base_symbols = None
        logger.error(f"Base greater than '62' is not supported.")
    if base_symbols is not None:
        print(f"Assumed base symbols: {base_symbols}")
    return base_symbols


def find_next_number(base_symbols, number):
    number_list = list(number)

    # Find next number
    d = number_list[-1]
    logger.debug("Processing digit: %s", d)
    bi = base_symbols.index(d)
    logger.debug("Digit %s found at index %s in base symbols", d, bi)
    if bi < len(base_symbols) - 1:
        number_list[-1] = base_symbols[bi + 1]
        logger.debug("Incrementing '%s' to next number '%s'", d, number_list[-1])
    else:
        number_list[-1] = base_symbols[0]
        logger.debug("Incrementing '%s' to next number '%s'", d, number_list[-1])
        logger.debug("Carrying over, setting digit to: %s", base_symbols[0])
        if len(number_list) == 1:
            number_list.insert(0, base_symbols[1])
            logger.debug("Extending number, new digit added at front (leftmost position): %s", base_symbols[1])
        else:
            prefix = find_next_number(base_symbols, ''.join(number_list[:-1]))
            number_list = list(prefix) + [number_list[-1]]

    return ''.join(number_list)


if __name__ == "__main__":
    main()
