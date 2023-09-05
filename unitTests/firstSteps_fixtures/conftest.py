# Inhalte in conftest.py stehen allen Tests in diesem 
# Ordner zur Verfügung.
# Ein Import ist nicht notwendig.

import pytest

@pytest.fixture         #Wird vor jedem Testlauf ausgeführt
def input_value():
   input = 60
   return input
