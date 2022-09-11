# zu testende Funktion
def func(x):
    return abs(x) + 1


# test_nameDerFunktion_<hinweis_zum_test>
def test_func_wert_wird_inkrementiert():
    # Arrange
    testwert = 5
    soll_ergebnis = 6

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis


def test_func_negativer_wert_wird_ignoriert():
    # Arrange
    testwert = -1
    soll_ergebnis = 2

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

    ## Als Einzeiler:
    #assert 2 == func(1)    # Für TDD nicht geeignet