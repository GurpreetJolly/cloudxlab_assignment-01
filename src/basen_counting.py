import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from basen_next_number import create_symbols_for_base, find_next_number

_base_symbols = None

def is_valid_number( base_symbols, number):
    for d in number:
        logger.debug("Checking digit: %s", d)
        if d not in base_symbols:
            logger.error(f"Digit '{d}' not valid for base with symbols {base_symbols}")
            return False
    return True

def main():
    print("\n*** This app prints all numbers starting from 0 to n in given base ***")
    base = int(input("Enter a number for base (e.g. for base-12 enter 12): "))
    base_symbols = create_symbols_for_base(base)
    if not base_symbols:
        logger.error(f"Base symbols could not be created for base '{base}'. Cannot continue")
        return False

    final_number = str(input("Enter a number for counting (the number should be combination of one or more base symbols): "))
    if not is_valid_number(base_symbols, final_number):
        logger.error(f"The number '{final_number}' is not valid for base {base}")
        return None
    else:
        logger.debug(f"The number '{final_number}' is valid for base {base}")
        next_num ='0'
        all_numbers = []
        while next_num != final_number:
            next_num = find_next_number(base_symbols, next_num)
            all_numbers.append(next_num)

    print(f"All numbers from 0 to {final_number} in base {base}: {all_numbers}")
    #format_markdown(all_numbers)
    #format_markdown_table(all_numbers, base)
    
    return 0

# def format_markdown_table(numbers, base):
#     print("\n*** Markdown formatted table output ***\n")
#     markdown_table = "|"
#     for i in range(len(numbers)//base):
#         markdown_table += f"{i}|"

#     markdown_table += "\n|"
#     for i in range(len(numbers)//base):
#         markdown_table += f"---|"

#     for i in range(len(numbers)):
#         markdown_table += "\n|"
#         for j in range(len(numbers)//base):
#             if i != j:
#                 markdown_table += f" {numbers[i]} |"
#             else:
#                 markdown_table += "   |"

#     print(markdown_table)

# def format_markdown(numbers):
#     print("\n*** Markdown formatted output ***\n")
#     markdown_output = "```\n"
#     for num in numbers:
#         markdown_output += f"{num}\n"
#     markdown_output += "```"
#     print(markdown_output)

if __name__ == "__main__":
    main()
    