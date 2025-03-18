from employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee("John", "Smith")
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 15000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 20000