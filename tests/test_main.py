from src.my_python_package.main import multiply_two_numbers

def test_multiply_two_numbers():
    # Arrange (initial condition)
    num1 = 2.5
    num2 = 2
    expected_outcome = 5

    # Act (perform the computation)
    result = multiply_two_numbers(num1,num2)

    # Assert (check that the result is what you expect)
    assert result == expected_outcome

