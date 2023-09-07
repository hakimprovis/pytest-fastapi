import pytest

from main import Car


@pytest.mark.parametrize("hours, speed,expected", [(1, 20, 20), (6, 4, 24)])
def test_car_speed(car, hours, speed, expected):
    car.engine.speed = speed
    car.drive(hours)
    assert car.milage() == expected


