import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_preconditions(self):
        # Test des préconditions
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)  # Test de création avec un dénominateur nul

    def test_normal_values(self):
        # Test de valeurs normales
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2", "Test de simplification échoué")

    def test_edge_cases(self):
        # Test de valeurs limites
        f1 = Fraction(1, 1)
        f2 = Fraction(-1, 1)
        self.assertEqual(str(f1), "1", "Test de 1/1 échoué")
        self.assertEqual(str(f2), "-1", "Test de -1/1 échoué")

    def test_boolean_methods(self):
        # Test des méthodes booléennes
        f_zero = Fraction(0, 1)
        f_integer = Fraction(8, 4)
        f_non_integer = Fraction(2, 3)
        self.assertTrue(f_zero.is_zero(), "Test de méthode is_zero échoué")
        self.assertTrue(f_integer.is_integer(), "Test de méthode is_integer échoué pour une fraction entière")
        self.assertFalse(f_non_integer.is_integer(), "Test de méthode is_integer échoué pour une fraction non entière")
        self.assertTrue(Fraction(1, 2).is_proper(), "Test de méthode is_proper échoué")
        self.assertFalse(Fraction(3, 2).is_proper(), "Test de méthode is_proper échoué pour une fraction incorrecte")

    def test_operations(self):
        # Test des opérations
        f1 = Fraction(1, 4)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 + f2), "7/12", "Test d'addition échoué")
        self.assertEqual(str(f1 - f2), "-1/12", "Test de soustraction échoué")
        self.assertEqual(str(f1 * f2), "1/12", "Test de multiplication échoué")
        self.assertEqual(str(f1 / f2), "3/4", "Test de division échoué")

    def test_power(self):
        # Test des puissances
        f = Fraction(2, 3)
        self.assertEqual(str(f ** 2), "4/9", "Test de puissance échoué")
        self.assertEqual(str(f ** 0), "1", "Test de puissance nulle échoué")

    def test_mixed_number(self):
        # Test de la conversion en nombre mixte
        f1 = Fraction(7, 4)
        self.assertEqual(f1.as_mixed_number(), "1 3/4", "Test de conversion en nombre mixte échoué")
        f2 = Fraction(1, 2)
        self.assertEqual(f2.as_mixed_number(), "1/2", "Test de conversion en nombre mixte échoué")

    def test_fraction_methods(self):
        # Test des méthodes de fraction
        f1 = Fraction(3, 4)
        self.assertTrue(f1.is_proper(), "Test de méthode is_proper échoué pour une fraction correcte")
        self.assertFalse(Fraction(5, 4).is_proper(), "Test de méthode is_proper échoué pour une fraction incorrecte")

    def test_problematic_cases(self):
        # Test des cas problématiques
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)  # Test de division par zéro

    def test_is_zero(self):
        # Test fractions zéro
        self.assertTrue(Fraction(0, 1).is_zero(), "La fraction 0/1 devrait être considérée comme zéro")
        self.assertFalse(Fraction(1, 1).is_zero(), "La fraction 1/1 ne devrait pas être considérée comme zéro")

    def test_is_integer(self):
        # Test fractions entières
        self.assertTrue(Fraction(4, 2).is_integer(), "La fraction 4/2 devrait être considérée comme un entier")
        self.assertFalse(Fraction(3, 2).is_integer(), "La fraction 3/2 ne devrait pas être considérée comme un entier")

    def test_is_proper(self):
        # Test fractions propres et incorrectes
        self.assertTrue(Fraction(3, 4).is_proper(), "La fraction 3/4 devrait être considérée comme propre")
        self.assertFalse(Fraction(5, 4).is_proper(), "La fraction 5/4 ne devrait pas être considérée comme propre")



if __name__ == '__main__':
    unittest.main()
