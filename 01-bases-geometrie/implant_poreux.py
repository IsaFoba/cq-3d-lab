import cadquery as cq

# 1. param
taille_bloc = 30.0
epaisseur = 5.0
diametre_pore = 2.0
espacement = 4.0

# 2. Calcul de la grille de trou
points = []
limite = (taille_bloc /2) - espacement

# 3. On parcourt l'axe X et l'axe Y pour placer les centres des trous
x = -limite
while x <= limite:
    y = -limite
    while y <= limite: 
        points.append((x, y))
        y = y + espacement
    x = x + espacement

# 4. Création de l'objet 3D
implant = (
    cq.Workplane("XY")
    .box(taille_bloc, taille_bloc, epaisseur)
    .faces(">Z")
    .workplane()
    .pushPoints(points)
    .hole(diametre_pore)
)

# 5. Affichage et Export
show_object(implant)
cq.exporters.export(implant, "implant_poreux.stl")


