import cadquery as cq

# 1. param
taille_bloc = 30.0
epaisseur = 10.0
diametre_pore = 2.0
espacement = 5.0
rayon_arrondi = 1.5

# 2. Calcul de la grille verticale (dessus : Axe X et Y)
points_dessus = list()
limite_xy = (taille_bloc /2) - espacement

# On parcourt l'axe X et l'axe Y 
x = -limite_xy
while x <= limite_xy:
    y = -limite_xy
    while y <= limite_xy: 
        points_dessus.append((x, y))
        y = y + espacement
    x = x + espacement

# 3. Calcul de la grille laterale (côtés : Axe X et Z)
points_cote = list()
limite_z = (taille_bloc /2) - 2.5

# On parcourt l'axe X et l'axe Z
x = -limite_xy
while x <= limite_xy:
    z = -limite_z
    while z <= limite_z: 
        points_cote.append((x, z))
        z = z + 2.5
    x = x + espacement


#  Création de l'objet 3D
implant = (
    cq.Workplane("XY")
    .box(taille_bloc, taille_bloc, epaisseur)

    # Étape A : arrondir les 12 arëtes extérieures avant de percer
    .edges()
    .fillet(rayon_arrondi)

    # Étape B : Percer de haut en bas (face >Z)
    .faces(">Z")
    .workplane()
    .pushPoints(points_dessus)
    .hole(diametre_pore)

    # Étape C : Percer de l'avant vers l'arrière (face >Y)
    .faces(">Y")
    .workplane()
    .pushPoints(points_cote)
    .hole(diametre_pore)

    # Étape D : Percer de la droite vers la gauche (face >X)
    .faces(">X")
    .workplane()
    .pushPoints(points_cote)
    .hole(diametre_pore)
)

#  Affichage et Export
show_object(implant)
cq.exporters.export(implant, "../export-stl/implant_3d_interconnecte.stl")


