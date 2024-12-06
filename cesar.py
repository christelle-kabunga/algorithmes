def cesar_chiff(msg, cle):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""
    for caractere in msg:
        if caractere in alphabet:
            position = (alphabet.index(caractere) + cle) % 26
            resultat += alphabet[position]
        else:
            resultat += caractere
    return resultat


def cesar_dechiff_all(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print("\nToutes les possibilités de déchiffrement (César) :")
    for cle in range(26):  # Essayer toutes les clés de 0 à 25
        resultat = ""
        for caractere in msg:
            if caractere in alphabet:
                position = (alphabet.index(caractere) - cle) % 26
                resultat += alphabet[position]
            else:
                resultat += caractere
        print(f"Clé {cle:02d}: {resultat}")


# Interface utilisateur
if __name__ == "__main__":
    choix = input("Voulez-vous (C)chiffrer ou (T)tester toutes les clés ? (C/T): ").lower()
    msg = input("Entrez le message : ")

    if choix == 'c':
        cle = int(input("Entrez la clé (0-25) : "))
        print(f"Message chiffré : {cesar_chiff(msg, cle)}")
    elif choix == 't':
        cesar_dechiff_all(msg)
    else:
        print("Choix non valide.")
