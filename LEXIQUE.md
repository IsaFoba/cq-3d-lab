Lexique technique avec synonymes courants en **CAO** (Conception Assistée par Ordinateur) et analogies

**1. Finitions et Arêtes**

• **fillet** (Prononcer « filette ») : Congé ou arrondi. C'est une opération qui remplace une arête vive par une surface courbe et douce.  

&emsp; • Synonymes en CAO : *Congé*, rayon de raccordement, **arrondi**.  
 
 &emsp; • À ne pas confondre avec : chamfer (le *chanfrein*), qui coupe l'arête en biais avec un angle plat (souvent à 45°) au lieu de l'arrondir.  
 
 &emsp; • Utilité en MedTech : Évite que les bords d'un implant n'irritent les tissus biologiques.  
 &nbsp;
 
• **edge** (Prononcer « èdje ») : Arête. C'est la ligne où deux faces d'un objet se rejoignent. Un cube possède 12 arêtes.  

&emsp; • Synonymes : Bord, segment, ligne de jonction.
 &nbsp;
 

**2. Positionnement et Perçage**

• **pushPoints** (De « pousser des points ») : Placer des repères. Cette commande prend une liste de coordonnées (x, y) et pose un point d'ancrage virtuel sur chacun de ces emplacements.  

&emsp; • Analogie : C'est l'équivalent du coup de pointeau d'un artisan avant de percer. On marque tous les endroits où la perceuse devra passer.  

&emsp; • Synonymes : Répartir des coordonnées, placer des cibles, marquer des emplacements.  

 &nbsp;
 
• **hole** (Prononcer « hôle ») : Perçage ou trou cylindrique. Cette commande perce directement un trou circulaire à l'emplacement du repère actif.  

&emsp; • Différence clé : .hole(diametre) demande le diamètre complet du trou et traverse toute la pièce par défaut. 
 
 À l'inverse, 
 **.circle**(rayon).**cutThruAll()** demande le rayon (la moitié du diamètre).  
 
&emsp; • Synonymes : Alésage, perforation, forage.  

 &nbsp;
 
• **Workplane** (Plan de travail) : Feuille de dessin virtuelle. C'est une surface plane et invisible posée dans l'espace 3D sur laquelle vous tracez vos formes avant de leur donner du volume.  

&emsp; • Synonymes : Plan d'esquisse, surface de référence, repère 2D.  
 
 &nbsp;

**3. Découpe et Limites Géométriques**

• **cutThruAll** (Cut Through All) : Découpe traversante. Cette action prend le dessin 2D que vous venez de tracer et creuse la matière de part en part, sur toute l'épaisseur de la pièce.  

&emsp; • Synonymes : Extrusion négative totale, perçage débouchant, évidement complet.  

 &nbsp;
 
• **bound / Bounding Box** : Boîte englobante. C'est un cube virtuel invisible qui entoure au plus près un objet 3D pour mesurer sa hauteur, sa largeur et sa profondeur maximales.  

&emsp; • Synonymes : Encombrement, volume limite, cadre extérieur.  
 &nbsp;

 
• **CenterOfBoundBox** : Centre géométrique. C'est le point situé exactement au milieu de la boîte englobante. Il permet de remettre le compteur (0, 0) pile au centre de votre pièce.
 &nbsp;


**4. Python & Mathématiques**

• **append** (Ajouter à la fin) : Empiler dans une liste. Permet d'ajouter une nouvelle coordonnée à la suite des autres dans votre variable points.  

&emsp; • Synonymes : Insérer, compléter, ajouter à la suite.  

 &nbsp;
 
• **sqrt** (Square Root) : Racine carrée. Fonction mathématique utilisée avec le théorème de Pythagore pour calculer la distance en ligne droite entre deux points.  



