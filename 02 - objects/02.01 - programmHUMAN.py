from classHuman import Human


def export():  # print value
    print(me.get_name(), end=' ')
    print(me.get_lastname(), end=' ')
    print(me.get_age(), 'Jahre', end=' ')
    print(me.get_family())


# obect class human with name me
me = Human("Marco", "Schmidt", 28, "ledig")
# me.set_name("Marco")
# me.set_age(28)
# me.set_lastname("Schmidt")

# print pointer
# print(me)

# print object values
# export()

# me.birthday()

# export()

if me.marry('Potter')==True:
    export()
else:
    export()
    print("already married")


