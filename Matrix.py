"""
Module for working with matrices.
"""

def input_wrapper(prompt):
    return input(prompt)


class Matrix:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.matrix_values = [[0 for i in range(width)] for j in range(height)]

    @staticmethod
    def create_matrix(name):
        """
        Method for creating the Matrix object. Obtain width and height from the user.
        """
        print('Matrix ' + name)

        width = int(input_wrapper('width: '))
        if width < 1:
            raise Exception('Width has to be bigger than 0.')
        height = int(input_wrapper('heigth: '))
        if height < 1:
            raise Exception('Height has to be bigger than 0.')

        matrix = Matrix(name, width, height)

        return matrix

    def interactive_input(self):
        """
        Method obtain values of the matrix from user and calls method set_value.
        """
        print('Matrix ' + str(self.name) + ' values')

        for row in range(self.height):
            row_input = input_wrapper('')
            values = row_input.split(' ')
            if len(values) == self.width:
                for i in range(len(values)):
                    self.set_value(int(values[i]), row, i)
            else:
                raise Exception('Wrong number of values in a row.')

    def set_value(self, value, pos_x, pos_y):
        """
        Method sets provided value to the positions.
        """
        self.matrix_values[pos_x][pos_y] = value

    def multiplication(self, mat_b):
        """
        Multipilaction of two matrices
        """
        if self.width != mat_b.height:
            raise Exception('Matrices can not be multiplicated.')
        product = Matrix('product', mat_b.width, self.height)

        for row in range(self.height):
            for column in range(mat_b.width):
                sum = 0
                for i in range(self.width):
                    sum += self.matrix_values[row][i] * mat_b.matrix_values[i][column]
                product.set_value(sum, row, column)

        return product

    def pretty_print_values(self):
        """
        Prints out matrix values in a given way.
        """
        print('Result:')

        separator = ' '
        for row in self.matrix_values:
            row_print = separator.join([str(x) for x in row])
            print(row_print)
