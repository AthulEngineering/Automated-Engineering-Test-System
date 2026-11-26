from main import check_voltage


def test_normal_voltage():
    assert check_voltage(12.1) == "PASS"


def test_high_voltage():
    assert check_voltage(13.2) == "FAIL"


def test_low_voltage():
    assert check_voltage(11.2) == "FAIL"


def test_lower_boundary():
    assert check_voltage(11.5) == "PASS"


def test_upper_boundary():
    assert check_voltage(12.5) == "PASS"