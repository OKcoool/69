from Ampel import Ampel, Ampelmanager

#ampel1 = Ampel("rot")
#
#for i in range(10):
#    print(ampel1)
#    ampel1.schalten()
#print(ampel1)

system = Ampelmanager()
for i in range(10):
    print(system)
    system.schalten()
print(system)