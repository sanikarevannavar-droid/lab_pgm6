from employee import employee_details

def test_employee_details():
    result = employee_details("Sanika", "101", "IT", "25000")

    expected = (
        "Name: Sanika\n"
        "Employee ID:  101\n"
        "Department: IT\n"
        "Salary: $25000.00"
    )

    assert result == expected


def test_employee_name():
    result = employee_details("Rahul", "102", "HR", "30000")
    assert "Name: Rahul" in result


def test_employee_id():
    result = employee_details("Sanika", "101", "IT", "25000")
    assert "Employee ID:  101" in result


def test_employee_department():
    result = employee_details("Sanika", "101", "IT", "25000")
    assert "Department: IT" in result


def test_employee_salary():
    result = employee_details("Sanika", "101", "IT", "25000")
    assert "Salary: $25000.00" in result