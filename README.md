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
make venv
# Actiivation du venv
make activate
# Installation des dépendences
make install
```

### Démarrer l'application
```
make start
```

### Gestion
- Les valeurs négative (-1) retournent vide comme résultat.
- Si une erreur est lancée, le champ opposé aura comme résultat un champ vide.
- Certaines devices ne peuvent pas être convertie entre elle
