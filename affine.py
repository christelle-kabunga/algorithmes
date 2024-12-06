def affine_chiff(message, clea, cleb):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for caractere in message.lower():
        if caractere in alphabet:
            index = alphabet.index(caractere)
            result += alphabet[(clea * index + cleb) % 26]
        else:
            result += caractere
    return result


def affine_dechiff_all(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print("\nToutes les possibilités de déchiffrement (Affine) :")
    for a in range(1, 26, 2):  # Seulement les nombres premiers avec 26
        try:
            inv_a = pow(a, -1, 26)
            for b in range(26):  # Essayer toutes les valeurs de b
                result = ""
                for caractere in message.lower():
                    if caractere in alphabet:
                        index = alphabet.index(caractere)
                        result += alphabet[(inv_a * (index - b)) % 26]
                    else:
                        result += caractere
                print(f"Clé (a={a}, b={b}): {result}")
        except ValueError:
            continue  # Passer si a n'est pas inversible


# Interface utilisateur
if __name__ == "__main__":
    choix = input("Voulez-vous (E)chiffrer ou (T)tester toutes les clés ? (E/T): ").lower()
    message = input("Entrez le message : ")

    if choix == 'e':
        clea = int(input("Entrez la clé a (premier avec 26) : "))
        cleb = int(input("Entrez la clé b : "))
        print(f"Message chiffré : {affine_chiff(message, clea, cleb)}")
    elif choix == 't':
        affine_dechiff_all(message)
    else:
        print("Choix non valide.")
