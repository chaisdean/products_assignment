class products(object):
    def __init__(self, price, name, weight, brand, cost, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sold(self):
        self.sold = 'sold-out'
        return self

    def add_tax(self):

        self.add_tax = (0.089 + self.price) + self.price
        self.results = self.add_tax
        return self

    def returns(self, reason):
        if products == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'returned':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price = self.price - (.20*self.price) 
        return self

    def displayinfo(self):
        print self.price
        print self.name
        print self.weight
        print self.brand
        print self.cost
        print self.status

example1 = products(19.99,'swiffer',3,'swiffer corp',14.99,'opened')
example1.returns('opened')

example1.displayinfo()
