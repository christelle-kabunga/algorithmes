def vigenere_chiff(message, cle):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    cle = cle.lower()
    cle_index = 0

    for caractere in message.lower():
        if caractere in alphabet:
            shift = alphabet.index(cle[cle_index % len(cle)])
            new_index = (alphabet.index(caractere) + shift) % 26
            result += alphabet[new_index]
            cle_index += 1
        else:
            result += caractere
    return result


def vigenere_dechiff(message, cle):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    cle = cle.lower()
    cle_index = 0

    for caractere in message.lower():
        if caractere in alphabet:
            shift = alphabet.index(cle[cle_index % len(cle)])
            new_index = (alphabet.index(caractere) - shift + 26) % 26
            result += alphabet[new_index]
            cle_index += 1
        else:
            result += caractere
    return result


# Interface utilisateur
if __name__ == "__main__":
    choix = input("Voulez-vous (E)chiffrer ou (D)déchiffrer ? (E/D): ").lower()
    message = input("Entrez votre message : ")

    if choix == "e":
        cle = input("Entrez votre clé : ")
        print(f"Message chiffré : {vigenere_chiff(message, cle)}")
    elif choix == "d":
        cle = input("Entrez votre clé : ")
        print(f"Message déchiffré : {vigenere_dechiff(message, cle)}")
    else:
        print("Choix non valide.")
