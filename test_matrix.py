"""
module for testing
"""


from Matrix import Matrix
from unittest.mock import patch
import contextlib
from io import StringIO


def test_matrix_initialization():
    A = Matrix('A', 1, 3)
    assert A.name == 'A'
    assert A.width == 1
    assert A.height == 3


def test_set_value():
    A = Matrix('A', 2, 3)
    A.set_value(10, 1, 0)
    assert A.matrix_values[1][0] == 10


def generate_input():
    yield '2'
    yield '3'
    yield '1 2'
    yield '3 4'
    yield '-1 -2'


generator = generate_input()


def fake_input_wrapper(_prompt):
    global generator
    return next(generator)


@patch('Matrix.input_wrapper', side_effect=fake_input_wrapper)
def test_get_matrix_from_user(_fake_input_function):
    A = Matrix.create_matrix('A')
    A.interactive_input()
    assert A.width == 2
    assert A.height == 3
    assert A.matrix_values == [[1, 2], [3, 4], [-1, -2]]


def test_multiplication():
    A = Matrix('A', 2, 3)
    B = Matrix('A', 1, 2)

    for i in range(A.height):
        for j in range(A.width):
            A.set_value(i+1, i, j)

    for i in range(B.height):
        for j in range(B.width):
            B.set_value(i+1, i, j)

    product = A.multiplication(B)
    assert product.matrix_values == [[3], [6], [9]]


def test_print_values():
    A = Matrix('A', 2, 3)

    for i in range(A.height):
        for j in range(A.width):
            A.set_value(i+1, i, j)

    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        A.pretty_print_values()
    output = temp_stdout.getvalue().strip()

    assert output == 'Result:\n1 1\n2 2\n3 3'
