# Jeu de la Vie de Conway - Implémentation Python/Tkinter

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

Implémentation interactive du célèbre automate cellulaire conçu par John Horton Conway en 1970. Cet outil pédagogique permet d'explorer les motifs émergents et les comportements complexes issus de règles simples.

## 🌟 Fonctionnalités Principales

Le projet intègre une interface graphique intuitive permettant de visualiser l'évolution des cellules selon les règles classiques du jeu. Les utilisateurs peuvent interagir avec la grille en temps réel, sélectionner des motifs prédéfinis et contrôler la vitesse de simulation. Une fonction de redémarrage automatique prévient les états stagnants.

## 📋 Prérequis Système

L'application nécessite Python 3.8 ou supérieur avec la bibliothèque Tkinter incluse par défaut. Aucune installation supplémentaire n'est requise pour la version de base. Les distributions Linux peuvent nécessiter les paquets `python3-tk`.

## 🚀 Installation Rapide

Clonez le dépôt et exécutez le script principal :

```
git clone https://github.com/votreutilisateur/jeu-de-la-vie.git
cd jeu-de-la-vie
python jeu_de_la_vie.py
```

## 🎮 Utilisation de Base

L'interface se compose d'une grille interactive et d'un panneau de contrôle. Utilisez le clic gauche pour activer/désactiver les cellules, la barre d'espace pour réinitialiser la grille, et les flèches directionnelles pour ajuster la vitesse de simulation.

### Commandes Clavier

| Touche       | Action                          |
|--------------|---------------------------------|
| Espace       | Redémarrer la simulation        |
| Flèche Haut  | Augmenter la vitesse            |
| Flèche Bas   | Réduire la vitesse              |
| Entrée       | Mode pas à pas                  |
| Clic Gauche  | Modifier l'état d'une cellule   |

## 🧠 Structure du Code

Le projet suit une architecture modulaire avec séparation claire entre la logique métier et l'interface utilisateur. Le module `Cellule` gère les états individuels tandis que `Grille` orchestre les interactions entre cellules. Le contrôleur principal intègre les entrées utilisateur et met à jour l'affichage via Tkinter.

