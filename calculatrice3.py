import math

def calculatrice_3():
    print("Bienvenue dans la calculatrice avancée (4e) !")
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance (x^y)")
    print("6. Racine carrée (√x)")
    print("7. Pourcentage (x% de y)")
    print("8. Sinus (sin(x))")
    print("9. Cosinus (cos(x))")
    print("10. Tangente (tan(x))")
    
    choix = input("Entrez le numéro de l'opération (1-10) : ")
    
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
    elif choix == '7':
        pourcentage = float(input("Entrez le pourcentage (x) : "))
        valeur = float(input("Entrez la valeur (y) : "))
        print(f"Résultat : {pourcentage}% de {valeur} = {valeur * (pourcentage / 100)}")
    elif choix in ['8', '9', '10']:
        angle = float(input("Entrez un angle en degrés : "))
        radians = math.radians(angle)
        
        if choix == '8':
            print(f"Résultat : sin({angle}) = {math.sin(radians)}")
        elif choix == '9':
            print(f"Résultat : cos({angle}) = {math.cos(radians)}")
        elif choix == '10':
            print(f"Résultat : tan({angle}) = {math.tan(radians)}")
    else:
        print("Opération non valide.")

calculatrice_3()
