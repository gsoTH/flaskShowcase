# Für eine detailierte Erklärung siehe:
# http://kleuker.iui.hs-osnabrueck.de/CSI/Methoden/kombiquUeberdeckung.html

def bonus(x:int, y:int):
    ergebnis = 0
    
    if(x>0 and y>0):
        ergebnis = 30
    
    if(x>10 and y <10):
        ergebnis = ergebnis + 20
    else:
        ergebnis = ergebnis + 10

    return ergebnis


def test_bonus_AnweisungsUeberdeckung_1():
    assert bonus(5,5) == 40
    
    # Arrange
    x = 5
    y = 5
    soll_ergebnis = 40

    # Act
    ist_ergebnis = bonus(x, y)

    # Assert
    assert soll_ergebnis == ist_ergebnis


""" 
> coverage run -m pytest
> coverage report 
Name                           Stmts   Miss  Cover
--------------------------------------------------
test_3_coverage.py                16      1    94%  <-- Statements der Tests zählen mit, wenn alles in einer Datei.
--------------------------------------------------
TOTAL                             16      1    94%
"""

# def test_bonus_AnweisungsUeberdeckung_2():
#     # Arrange
#     x = 11
#     y = 5
#     soll_ergebnis = 50

#     # Act
#     ist_ergebnis = bonus(x, y)

#     # Assert
#     assert soll_ergebnis == ist_ergebnis


""" 
> coverage run -m pytest
> coverage report

Name                           Stmts   Miss  Cover
--------------------------------------------------
test_3_coverage.py                20      0   100%
--------------------------------------------------
TOTAL                             20      0   100%
 """

""" 
> coverage run --branch -m pytest
> coverage report

Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
test_3_coverage.py                22      0      4      1    96%
----------------------------------------------------------------
TOTAL                             22      0      4      1    96% 
"""

# def test_bonus_ZweigUeberdeckung_3():
#     # Arrange
#     x = 15
#     y = 0
#     soll_ergebnis = 50 

#     # Act
#     ist_ergebnis = bonus(x, y)

#     # Assert
#     assert soll_ergebnis == ist_ergebnis

""" 
> coverage run --branch -m pytest
> coverage report

Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
test_3_coverage.py                27      0      4      0   100%
----------------------------------------------------------------
TOTAL                             27      0      4      0   100% 
"""