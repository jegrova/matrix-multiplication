#!/usr/bin/env python3

"""
Main function
"""

import sys
from Matrix import Matrix


if __name__ == '__main__':

    try:
        A = Matrix.create_matrix('A')
        B = Matrix.create_matrix('B')

        A.interactive_input()
        B.interactive_input()

        product = A.multiplication(B)
        A.pretty_print_values()

    except ValueError:
        sys.exit('Value has to be an integer.')
    except Exception as error:
        print(error.args[0])
        sys.exit()
