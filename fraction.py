from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author: F. Scalais
    Date: Août 2024
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on a numerator and denominator.

        PRE: 
        - `den` ne doit pas être nul.
        - `num` et `den` doivent être des nombres entiers.

        POST:
        - La fraction est simplifiée (forme réduite).
        - Le dénominateur est toujours positif.
        """
        # Vérifie que le numérateur et le dénominateur sont des entiers
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Le numérateur et le dénominateur doivent être des nombres entiers.")

        # Vérifie que le dénominateur n'est pas nul
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être nul.")
        
        # Simplifie la fraction en trouvant le plus grand commun diviseur
        if den < 0:
            num = -num
            den = -den

        # simplifiez la fraction
        common_divisor = gcd(num, den)
        self._numerator = num // common_divisor
        self._denominator = den // common_divisor

    @property
    def numerator(self):
        """Renvoie le numérateur de la fraction
        PRE  : None
        POST : Retourne le dénominateur sous forme d'entier."""

        return self._numerator

    @property
    def denominator(self):
        """Renvoie le dénominateur de la fraction

        PRE  : None
        POST : Retourne le dénominateur sous forme d'entier."""

        return self._denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE: None
        POST: Renvoie une chaîne sous la forme "numérateur/dénominateur"
        """
        return f"{self._numerator}/{self._denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE: None
        POST: Renvoie une chaîne sous la forme "integer proper_fraction"
        """
        # Si la fraction est déjà propre (cad que la partie entière est 0), retourne simplement la fraction
        if abs(self._numerator) < self._denominator:
            return str(self)

        # Calculer la partie entière et le reste
        integer_part = self._numerator // self._denominator
        remainder = abs(self._numerator) % self._denominator
        if remainder == 0:
            return str(integer_part)
        # Retourne le nombre fractionnaire
        return f"{integer_part} {remainder}/{self._denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE: 
        - « autre » doit être de type « Fraction ».

        POST:
        - Renvoie une nouvelle instance « Fraction » qui est la somme de soi et des autres.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les opérandes doivent être des fractions.")

        # Additionner les fractions en trouvant le dénominateur commun
        new_num = self._numerator * other.denominator + other.numerator * self._denominator
        new_den = self._denominator * other.denominator

        #new_num += 1  (test pour echec)
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE:
        - `other` doit être de type `Fraction`.

        POST:
        - Renvoie une nouvelle instance `Fraction` qui représente la différence entre soi et les autres.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les opérandes doivent être des fractions.")

        # Soustraire les fractions en trouvant le dénominateur commun
        new_num = self._numerator * other.denominator - other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE:
        - `other` doit être de type `Fraction`.

        POST:
        - Renvoie une nouvelle instance `Fraction` qui est le produit de soi et des autres.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les opérandes doivent être des fractions.")

         # Multiplier les numérateurs et les dénominateurs
        new_num = self._numerator * other.numerator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE:
        - `other` doit être de type `Fraction`.
        - `other` ne doit pas avoir un numérateur égal à zéro.

        POST:
        - Renvoie une nouvelle instance « Fraction » qui est le quotient de soi et des autres.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les opérandes doivent être des fractions.")
        if other.numerator == 0:
            raise ZeroDivisionError("Impossible de diviser par une fraction de numérateur 0.")

        # Inverser la fraction `other` et multiplier
        new_num = self._numerator * other.denominator
        new_den = self._denominator * other.numerator
        return Fraction(new_num, new_den)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions

        PRE:
        - `power` doit être un entier.

        POST:
        - Renvoie une nouvelle instance `Fraction` qui est auto-élevée à la puissance.
        """
        if not isinstance(power, int):
            raise TypeError("La puissance doit être un entier.")

         # Élever numérateur et dénominateur à la puissance `power`
        return Fraction(self._numerator ** power, self._denominator ** power)
    
    def __eq__(self, other):
        """Overloading of the == operator for fractions
        
        PRE:
        - `other` doit être de type `Fraction`.
        
        POST:
        - Renvoie True si self et other représentent la même fraction, False sinon.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les opérandes doivent être des fractions.")

         # Comparer les fractions en fonction de leur forme réduite
        return self._numerator == other.numerator and self._denominator == other.denominator
        
    def __float__(self):
        """Returns the decimal value of the fraction

        PRE: None
        POST: Renvoie la représentation à virgule flottante de la fraction.
        """
        return self._numerator / self._denominator
    
    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE: None
        POST: Renvoie True si la fraction est 0, False sinon.
        """
        return self._numerator == 0

    def is_integer(self):
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2, ...)

        PRE: None
        POST: Renvoie True si la fraction est un entier, False sinon.
        """
        return self._numerator % self._denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE: None
        POST: Renvoie True si la fraction est correcte, False sinon.
        """
        return abs(self._numerator) < self._denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE: None
        POST: Renvoie True si la fraction est une fraction unitaire, False sinon.
        """
        return abs(self._numerator) == 1 and self._denominator != 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference between them is a unit fraction.

        PRE:
        - `other` doit être de type `Fraction`.

        POST:
        - Renvoie True si les deux fractions sont adjacentes, False sinon.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les opérandes doivent être des fractions.")

        # Calculer la différence entre les fractions
        diff_fraction = self - other
        print(f"Différence entre {self} et {other} : {diff_fraction}")
        # Vérifier si la différence est une fraction unitaire
        result = diff_fraction.is_unit()
        print(f"La différence est une fraction unitaire : {result}")

        return result
