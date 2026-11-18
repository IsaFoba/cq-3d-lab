# 🧪 CQ-3D-Lab : Modélisation Paramétrique & Fabrication Additive en Python

Bienvenue dans mon laboratoire de recherche et de développement dédié à la **CAO paramétrique par le code** et à la **fabrication additive** (impression 3D). 

Ce dépôt rassemble mes scripts Python développés avec **CadQuery** pour générer automatiquement des géométries complexes, des structures poreuses (type *scaffolds* médicaux) et préparer des maillages `.stl` prêts à être imprimés.

---

## 🎯 Objectifs du projet
* **Automatisation géométrique :** Remplacer la modélisation manuelle par des algorithmes paramétriques reproductibles.
* **Ingénierie biomédicale & MedTech :** Concevoir des structures poreuses interconnectées favorisant la circulation des fluides et la colonisation cellulaire.
* **Chaîne numérique complète :** Maîtriser le flux de travail du script Python jusqu'à l'exportation et la validation du maillage `.stl` (slicing).

---

## 🛠️ Technologies utilisées
* **Langage :** Python 3
* **Moteur CAO :** [CadQuery](https://github.com) (basé sur OpenCascade)
* **Environnement :** CQ-editor
* **Validation & Slicing :** ONLINE 3D VIEWER (option : PrusaSlicer / Visualiseur STL)

---

## 📂 Structure du dépôt

```text
cq-3d-lab/
├── implant_poreux/ # Scripts de modélisation paramétrique
│ ├── implant_poreux.py # Grille de pores 2D générée par boucles
│ ├── implant_poreux.stl # Fichiers de maillages générés prêts pour l'impression 3D
│ ├── implant_poreux_face.png et implant_poreux_biais.png # Captures d'écran des rendus 3D
└── README.md
```

---

## 🚀 Réalisations & Aperçus 3D

---

### 1. Grille poreuse paramétrique (`implant_poreux.py`)
Création d'une matrice de perforations calibrées sur une plaque de base. L'espacement et le diamètre des pores s'ajustent dynamiquement via les variables en tête de script.

* **Concepts clés :** Listes de coordonnées, `.pushPoints()`, exportation automatisée au format `.stl`.

![Rendu de la grille poreuse](implant_poreux/implant_poreux_face.png)
![Rendu de la grille poreuse](implant_poreux/implant_poreux_biais.png)

---

