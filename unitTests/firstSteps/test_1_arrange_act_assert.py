# zu testende Funktion
def func(x):
    return abs(x) + 1



def test_func():
    # Arrage
    testwert = 5
    soll_ergebnis = 6

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis


def test_func_negativer_wert_wird_ignoriert():
    # Arrage
    testwert = -1
    soll_ergebnis = 2

    # Act
    ist_ergebnis = func(testwert)

    # Assert
    assert ist_ergebnis == soll_ergebnis