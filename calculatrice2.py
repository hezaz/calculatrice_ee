import math

def calculatrice_2():
    print("Bienvenue dans la calculatrice scientifique (5e) !")
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance (x^y)")
    print("6. Racine carrée (√x)")
    
    choix = input("Entrez le numéro de l'opération (1/2/3/4/5/6) : ")
    
    if choix in ['1', '2', '3', '4']:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        
        if choix == '1':
            print(f"Résultat : {num1} + {num2} = {num1 + num2}")
        elif choix == '2':
            print(f"Résultat : {num1} - {num2} = {num1 - num2}")
        elif choix == '3':
            print(f"Résultat : {num1} * {num2} = {num1 * num2}")
        elif choix == '4':
            if num2 != 0:
                print(f"Résultat : {num1} / {num2} = {num1 / num2}")
            else:
                print("Erreur : division par zéro.")
    elif choix == '5':
        base = float(input("Entrez la base (x) : "))
        exposant = float(input("Entrez l'exposant (y) : "))
        print(f"Résultat : {base}^{exposant} = {base ** exposant}")
    elif choix == '6':
        num = float(input("Entrez un nombre : "))
        if num >= 0:
            print(f"Résultat : √{num} = {math.sqrt(num)}")
        else:
            print("Erreur : racine carrée d'un nombre négatif.")
    else:
        print("Opération non valide.")

calculatrice_2()
