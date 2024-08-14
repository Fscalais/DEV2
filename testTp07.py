from fraction import Fraction

def test_fraction():
    tests_passed = True

    # Test de la création et de la simplification des fractions
    try:
        f1 = Fraction(4, 8)
        assert str(f1) == "1/2", "Test de simplification échoué"
        print("Test de simplification réussi pour 4/8")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        f2 = Fraction(-6, -9)
        assert str(f2) == "2/3", "Test de simplification échoué"
        print("Test de simplification réussi pour -6/-9")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        f3 = Fraction(5, -10)
        assert str(f3) == "-1/2", "Test de gestion du signe échoué"
        print("Test de gestion du signe réussi pour 5/-10")
    except AssertionError as e:
        print(e)
        tests_passed = False

    # Test de l'affichage en nombre fractionnaire
    try:
        f4 = Fraction(7, 3)
        assert f4.as_mixed_number() == "2 1/3", "Test de représentation mixte échoué"
        print("Test de représentation mixte réussi pour 7/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    # Test des opérations arithmétiques
    try:
        f5 = Fraction(1, 4)
        f6 = Fraction(1, 3)
        assert str(f5 + f6) == "7/12", "Test d'addition échoué"
        print("Test d'addition réussi pour 1/4 + 1/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert str(f5 + f6) == "8/12", "Test d'addition échoué"  # test pour echec
        print("Test d'addition réussi pour 1/4 + 1/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert str(f5 - f6) == "-1/12", "Test de soustraction échoué"
        print("Test de soustraction réussi pour 1/4 - 1/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert str(f5 * f6) == "1/12", "Test de multiplication échoué"
        print("Test de multiplication réussi pour 1/4 * 1/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert str(f5 / f6) == "3/4", "Test de division échoué"
        print("Test de division réussi pour 1/4 / 1/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    # Test de l'égalité
    try:
        f7 = Fraction(2, 4)
        f8 = Fraction(1, 2)
        assert f7 == f8, "Test d'égalité échoué"
        print("Test d'égalité réussi pour 2/4 et 1/2")
    except AssertionError as e:
        print(e)
        tests_passed = False

    # Test des propriétés
    try:
        assert f1.is_zero() == False, "Test de vérification du zéro échoué"
        print("Test de vérification du zéro réussi pour 1/2")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert f2.is_integer() == False, "Test de vérification d'entier échoué"
        print("Test de vérification d'entier réussi pour 2/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert f3.is_proper() == True, "Test de vérification propre échoué"
        print("Test de vérification propre réussi pour -1/2")
    except AssertionError as e:
        print(e)
        tests_passed = False

    try:
        assert f4.is_unit() == False, "Test de vérification de fraction unitaire échoué"
        print("Test de vérification de fraction unitaire réussi pour 7/3")
    except AssertionError as e:
        print(e)
        tests_passed = False

    # Test des fractions adjacentes
    try:
        f9 = Fraction(1, 2)
        f10 = Fraction(2, 3)
        is_adj = f9.is_adjacent_to(f10)
        assert is_adj == True, "Test de vérification d'adjacence échoué"
        print(f"Test de vérification d'adjacence réussi pour 1/2 et 2/3 (Différence: {f9 - f10})")
    except AssertionError as e:
        print(e)
        tests_passed = False

    if tests_passed:
        print("Tous les tests ont réussi !")
    else:
        print("Certains tests ont échoué.")

if __name__ == "__main__":
    test_fraction()

