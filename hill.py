import numpy as np

def hill_encrypt(message, key_matrix):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    if len(message) % 2 != 0:
        message += "x"  # Ajouter une lettre par défaut
    result = ""
    for i in range(0, len(message), 2):
        pair = [alphabet.index(message[i]), alphabet.index(message[i + 1])]
        encrypted_pair = np.dot(key_matrix, pair) % 26
        result += alphabet[encrypted_pair[0]] + alphabet[encrypted_pair[1]]
    return result


def hill_decrypt(message, key_matrix):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    try:
        det_inv = pow(det, -1, 26)
        adjugate = np.array([[key_matrix[1, 1], -key_matrix[0, 1]],
                             [-key_matrix[1, 0], key_matrix[0, 0]]])
        inverse_key = (det_inv * adjugate) % 26
        for i in range(0, len(message), 2):
            pair = [alphabet.index(message[i]), alphabet.index(message[i + 1])]
            decrypted_pair = np.dot(inverse_key, pair) % 26
            result += alphabet[int(decrypted_pair[0])] + alphabet[int(decrypted_pair[1])]
        return result
    except ValueError:
        return "Erreur : la clé n'est pas inversible."


# Interface utilisateur
if __name__ == "__main__":
    choix = input("Voulez-vous (E)chiffrer ou (D)déchiffrer ? (E/D): ").lower()
    message = input("Entrez votre message (longueur paire) : ")

    if choix == "e":
        key_matrix = np.array([
            [int(input("Entrez K11 : ")), int(input("Entrez K12 : "))],
            [int(input("Entrez K21 : ")), int(input("Entrez K22 : "))]
        ])
        print(f"Message chiffré : {hill_encrypt(message, key_matrix)}")
    elif choix == "d":
        key_matrix = np.array([
            [int(input("Entrez K11 : ")), int(input("Entrez K12 : "))],
            [int(input("Entrez K21 : ")), int(input("Entrez K22 : "))]
        ])
        print(f"Message déchiffré : {hill_decrypt(message, key_matrix)}")
    else:
        print("Choix non valide.")
