import pytest
import math

# pytest            <-- führt 3/4 Tests dieser Datei aus (letzter steht auf skip)
# pytest -m square  <-- führt 2/4 Tests dieser Datei aus (nur die ersten beiden)
# pytest -m others  <-- führt 1/4 Tests dieser Datei aus (nur vorletzten)

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

@pytest.mark.others
def test_equality():
   assert 10 == 11

@pytest.mark.skip
def test_wird_nie_getestet():
    assert math.pi == 3
