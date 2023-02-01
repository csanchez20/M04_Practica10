from A import exercici1_A as naixementA
from B import exercici1_B as naixementB

# inputs per preguntar a l'usuari les seves dades
anyNaixement = input("Posa el teu any de naixement:")
anyNaixement = int(anyNaixement)

edat = input("Posa la teva edat:")
edat = int(edat)

# cridem a les funcions
print(naixementA.naixement(anyNaixement))
print(naixementB.anyNaixement(edat))

