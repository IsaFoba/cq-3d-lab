import cadquery as cq
import math

"""
On cherche à reproduire la structure d'un os naturel 
(très dense sur l'extérieur pour la solidité mécanique, 
et très poreux au coeur pour laisser circuler les cellules
"""
# 1. param
taille_bloc = 40.0
epaisseur = 5.0
espacement = 5.0

rayon_min = 0.4
rayon_max = 1.6

# 2. Création de bloc de base
piece = cq.Workplane("XY").box(taille_bloc, taille_bloc, epaisseur)

# Distance maximale du centre jusqu'au bord du bloc
limite = (taille_bloc / 2) - espacement

# 3. Boucle de percage à diamètre variable

x = -limite
while x <= limite:
    y = -limite
    while y <= limite: 
        # Calcul de la distance du trou par rapport au centre (0, 0)
        distance = math.sqrt(x**2 + y**2)
        # Calcul du ratio (0.0 au centre, proche de 1.0 sur les bords)
        ratio = distance / limite
        if ratio > 1.0:
            ratio = 1.0

        # Plus on est proche du centre, plus le rayon est grand
        rayon_actuel = rayon_max - (ratio * (rayon_max - rayon_min))

        # On perce ce trou précis avec son rayon calculé, ne repartant toujours du centre
        piece = (
            piece.faces(">Z")
            .workplane(centerOption="CenterOfBoundBox")
            .center(x, y)
            .circle(rayon_actuel)
            .cutThruAll()
        )
        y = y + espacement
    x = x + espacement




#  Affichage et Export
show_object(piece)
cq.exporters.export(piece, "../export-stl/gradiant_porosite.stl")


