# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

print(compras)  

compras[2].append("jugo")
compras[1][1] = ("tallarines")
compras[0].remove("pan")

print(compras)