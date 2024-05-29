from FinalProjectMG.package.calculator import Calculator
def test_addition():
    calc = Calculator()
    calc.set_values(3, 2, 'add')
    result = calc.calculate()
    assert result == 5, f"Expected 5 but got {result}"

def test_subtraction():
    calc = Calculator()
    calc.set_values(5, 3, 'subtract')
    result = calc.calculate()
    assert result == 2, f"Expected 2 but got {result}"

def test_multiplication():
    calc = Calculator()
    calc.set_values(4, 3, 'multiply')
    result = calc.calculate()
    assert result == 12, f"Expected 12 but got {result}"

def test_division():
    calc = Calculator()
    calc.set_values(10, 2, 'divide')
    result = calc.calculate()
    assert result == 5, f"Expected 5 but got {result}"

def test_division_by_zero():
    calc = Calculator()
    calc.set_values(10, 0, 'divide')
    result = calc.calculate()
    assert result == 'Error! Division by zero.', f"Expected 'Error! Division by zero.' but got {result}"
