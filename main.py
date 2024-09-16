"""

"""
#### Fonction secondaire


def ispalindrome(p):
    """
    retourne un bouléen

    Args:
        p: chaine de caractères

    """
    table = str.maketrans("éèêëàïùçô", "eeeeaiuco", "?.:/!', -")
    p =p.lower().translate(table)
    if p[::-1]== p:
        return True
    return False

#### Fonction principale


def main():
    """
    appel fonction palindrome
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
