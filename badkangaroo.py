class Kangaroo():
    """ note this __init__ is a workaround for a default value of an empty
    list, but mutable objects as defaults should be avoided.

    see Downey's BadKangaroo.py and GoodKangaroo.py for illustrations.
    """
    def __init__(self, name, contents=None):
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        return str(self.name) + ': ' + str(self.pouch_contents)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

kanga = Kangaroo('kanga')
kanga.put_in_pouch('a')
kanga.put_in_pouch((1,2))
print(kanga)
roo = Kangaroo('roo')
roo.put_in_pouch('car keys')
print(roo)
print("putting roo into kanga...")
kanga.put_in_pouch(roo)
print(kanga)
