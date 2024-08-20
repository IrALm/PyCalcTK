import tkinter as tk
import math

# Fonction pour gérer les clics sur les boutons (nombres et opérateurs)
def cliquerBouton(valeur):
    textBouton = ecran.get()
    nouveauText = textBouton + str(valeur)
    ecran.delete(0, tk.END)
    ecran.insert(0, nouveauText)

# Fonction pour effacer l'écran
def effacer_ecran():
    ecran.delete(0, tk.END)

# Fonction pour calculer et afficher le résultat
def calculer_resultatat():
    try:
        resultat = eval(ecran.get())  # Évaluer l'expression
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer le logarithme en base 10
def calculer_logarithme():
    try:
        resultat = math.log10(float(ecran.get()))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer le logarithme naturel (ln)
def calculer_ln():
    try:
        resultat = math.log(float(ecran.get()))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer l'exponentielle
def calcculer_exponentielle():
    try:
        resultat = math.exp(float(ecran.get()))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer la racine carrée
def calculer_racineCarree():
    try:
        resultat = math.sqrt(float(ecran.get()))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer la racine cubique
def calculer_racineCubique():
    try:
        resultat = float(ecran.get()) ** (1/3)
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour élever un nombre à la puissance d'un autre
def calculer_exposant():
    try:
        base, exponent = map(float, ecran.get().split('^'))
        resultat = base ** exponent
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer le sinus
def calculer_sin():
    try:
        resultat = math.sin(math.radians(float(ecran.get())))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer le cosinus
def calculer_cosinus():
    try:
        resultat = math.cos(math.radians(float(ecran.get())))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Fonction pour calculer la tangente
def calculer_tangente():
    try:
        resultat = math.tan(math.radians(float(ecran.get())))
        ecran.delete(0, tk.END)
        ecran.insert(0, str(resultat))
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Error")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")
# Changer la couleur de fond de la fenêtre (par exemple, en bleu clair)
fenetre.configure(bg='black')
# Création de l'écran de la calculatrice
ecran = tk.Entry(fenetre, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right' , bg = 'black' , fg = 'white')
ecran.grid(row=0, column=0, columnspan=4, pady=10)

# Liste des boutons et leurs positions dans la grille
buttons = [
    'sin', 'cos','tan', 
    'x^y' ,'log', 'ln',
    'exp','√',
    '7', '8', '9','*', 
    '4', '5','6','/',
    '2', '3','1', '+',
    '.','0','%',  '-',
    '∛','=','C'
]

# Création et placement des boutons
row = 1
col = 0
for button in buttons:
    if button == 'C':
        b = tk.Button(fenetre, text=button,bg = 'blue' , fg = 'white' , padx=20, pady=20, font=('Arial', 18), command=effacer_ecran)
    elif button == '=':
        b = tk.Button(fenetre, text=button,bg = 'orange' , fg = 'white' , padx=20, pady=20, font=('Arial', 18), command=calculer_resultatat)
    elif button == 'log':
        b = tk.Button(fenetre, text=button,bg = 'darkgrey' , fg = 'black' , padx=20, pady=20, font=('Arial', 18), command=calculer_logarithme)
    elif button == 'ln':
        b = tk.Button(fenetre, text=button,bg = 'darkgrey' , fg = 'black' , padx=20, pady=20, font=('Arial', 18), command=calculer_ln)
    elif button == 'exp':
        b = tk.Button(fenetre, text=button,bg = 'darkgrey' , fg = 'black' , padx=20, pady=20, font=('Arial', 18), command=calcculer_exponentielle)
    elif button == '√':
        b = tk.Button(fenetre, text=button,bg = 'darkgrey' , fg = 'black' , padx=20, pady=20, font=('Arial', 18), command=calculer_racineCarree)
    elif button == '∛':
        b = tk.Button(fenetre, text=button,bg = 'black' , fg = 'white' , padx=20, pady=20, font=('Arial', 18), command=calculer_racineCubique)
    elif button == 'x^y':
        b = tk.Button(fenetre, text=button,bg = 'darkgrey' , fg = 'black' , padx=20, pady=20, font=('Arial', 18), command=lambda: cliquerBouton('^'))
    elif button == 'sin':
        b = tk.Button(fenetre, text=button,bg = '#4B4B4B' , fg = 'orange' , padx=20, pady=20, font=('Arial', 18), command=calculer_sin)
    elif button == 'cos':
        b = tk.Button(fenetre, text=button,bg = '#4B4B4B' , fg = 'orange' , padx=20, pady=20, font=('Arial', 18), command=calculer_cosinus)
    elif button == 'tan':
        b = tk.Button(fenetre, text=button,bg = '#4B4B4B' , fg = 'orange' , padx=20, pady=20, font=('Arial', 18), command=calculer_tangente)
    else:
        b = tk.Button(fenetre, text=button , bg = '#696969' , fg = 'white' , padx=20, pady=20, font=('Arial', 18), command=lambda b=button: cliquerBouton(b))
    
    b.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Ajuster la taille des colonnes et des lignes pour qu'ils s'étendent correctement
for i in range(4):
    fenetre.grid_columnconfigure(i, weight=1)
    fenetre.grid_rowconfigure(i + 1, weight=1)

# Démarrer l'application
fenetre.mainloop()
