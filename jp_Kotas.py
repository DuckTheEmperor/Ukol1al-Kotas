#1
nebe = ["slunce", "mesic", "nebe", "mrak", "strom"]
#2
nebe.append("vitr")
#3
nebe.remove("mesic")
#4
zeme = [a.replace("vitr", "slunce") for a in nebe]
#5
pridat = ["list", "zem"]
zeme.extend (pridat)
#6

