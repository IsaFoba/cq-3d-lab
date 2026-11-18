import cadquery as cq
"""
result = cq.Workplane("XY" ).box(3, 3, 1.5).edges("|Z").fillet(0.925)
show_object(result)
"""
#Création d'un bloc de 20 mm x 30 mm x 10 mm avec un trou de 7mm
piece = cq.Workplane("XY").box(20,30,10).hole(7)

#Affichage de l'objet à l'écran
show_object(piece)

#Crée un fichier prët pour impression 3D
cq.exporters.export(piece, "ma_prems_piece.stl")