# UnitTests
In diesem Ordner wird gezeigt, wie man UnitTests für Flask einsetzen kann. UnitTests bilden die Grundlage für [test-driven-developement](https://de.wikipedia.org/wiki/Testgetriebene_Entwicklung).

1. [firstSteps](https://github.com/gsoTH/flaskShowcase/tree/master/unitTests/firstSteps): Einführung in UnitTests in Python mit Pytest und Coverage
2. [firstSteps_fixtures](https://github.com/gsoTH/flaskShowcase/tree/master/unitTests/firstSteps_fixtures): Einige Feinheiten von Pytest, z.B. pytest.fixture gemeinsamer Arrange-Block für alle Tests und wie man sie in eine conftest.py auslagert
3. [testFlaskSimple](https://github.com/gsoTH/flaskShowcase/tree/master/unitTests/testFlaskSimple): Erster UnitTest (HTTP-GET) für Flask, inkl. Wrapper (Factory-Pattern) um einen Test-Client zu erzeugen.
4. [testFlaskWIthPayload](https://github.com/gsoTH/flaskShowcase/tree/master/unitTests/testFlaskWIthPayload): Beispiele für UnitsTests mit HTTP-POST

Nachdem wir wissen *wie* man testet, bleibt noch die Frage, *was* wir testen sollten. Die Antwort gibt uns der Kunde (Anforderungen in UnitTests übersetzen) und die Grenzwertanalyse (gültige, ungültige Werte systematisch erarbeiten).