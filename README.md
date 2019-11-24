# Convertisseur de devises

Cette application est un convertisseur de devices.

![enter image description here](https://raw.githubusercontent.com/musps/currency-converter/master/screenshot.png)

### Pré-requis
* Avoir `python version 3.0.0` installé sur sa machine.

### Librairie utilisées 
- CurrencyConverter
- PySide2

### Installation
```
# Création du venv
python3 -m venv venv

# Actiivation du venv
source venv/bin/activate

# Installation des dépendences
pip install -r requirements.txt
```

### Démarrer l'application
```
python3 main.py
```

### Gestion
- Les valeurs négative (-1) retournent vide comme résultat.
- Si une erreur est lancée, le champ opposé aura comme résultat un champ vide.
- Certaines devices ne peuvent pas être convertie entre elle
