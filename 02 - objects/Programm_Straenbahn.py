from Straenbahn import strassenbahn, fahrer

strabba = strassenbahn("Die Strabba", 100, 1, fahrer("Jonas", 17))

print(strabba)
strabba.geburtstag()
print(strabba)
strabba.stamm_aendern(5)
print(strabba)