# Convertisseur de devises

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
