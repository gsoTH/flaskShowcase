# zu testende Funktion
def func(x):
    return abs(x) + 1


# test_name_der_Funktion__hinweis_zum_test
#                        ^
#                        doppelter Unterstrich nach 
def test_func__wert_wird_inkrementiert():
    # Arrange
    testwert = 5
    soll_ergebnis = 6

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis


def test_func__negativer_wert_wird_ignoriert():
    # Arrange
    testwert = -1
    soll_ergebnis = 2

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis

    ## Als Einzeiler:
    #assert 2 == func(1)    # Für TDD nicht geeignet
