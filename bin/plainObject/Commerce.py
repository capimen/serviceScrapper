class Commerce:

    def __init__(self, id, name, priceclass, pricetag, nameclass, nametag):
        self.id = id
        self.name = name
        self.priceclass = priceclass
        self.pricetag = pricetag
        self.nameclass = nameclass
        self.nametag = nametag

    def fromJson(self,jsonCommerce):
        self.id = jsonCommerce['id']
        self.name = jsonCommerce['name']
        self.priceclass = jsonCommerce['priceclass']
        self.pricetag = jsonCommerce['pricetag']
        self.nameclass = jsonCommerce['nameclass']
        self.nametag = jsonCommerce['nametag']
        return self

    def toJson(self):
        arr = {}
        arr['id'] = self.id
        arr['name'] = self.name
        arr['priceclass'] = self.priceclass
        arr['pricetag'] = self.pricetag
        arr['nameclass'] = self.nameclass
        arr['nametag'] = self.nametag
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['id'] = self.id
        arr['name'] = self.name
        arr['priceclass'] = self.priceclass
        arr['pricetag'] = self.pricetag
        arr['nameclass'] = self.nameclass
        arr['nametag'] = self.nametag
        return arr

    def toArray(self):
        arr = []
        arr.append(self.id)
        arr.append(self.name)
        arr.append(self.priceclass)
        arr.append(self.pricetag)
        arr.append(self.nameclass)
        arr.append(self.nametag)
        return arr

    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))