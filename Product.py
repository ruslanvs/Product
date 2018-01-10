class Product( object ):
    def __init__( self, name, price = "-", weight = "-", brand = "-", status = "for sale", taxAmount = 0, retReason = "-", retCondition = "-" ):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = status
        self.taxAmount = taxAmount
        self.retReason = retReason
        self.retCondition = retCondition
    def sell( self ):
        self.status = "sold"
        return self
    def addTax( self, taxAmount ):
        self.taxAmount = taxAmount
        print " "
        print self.name, "Price with tax", self.price + self.taxAmount
        return self.price + self.taxAmount
    def returnItem( self, retReason, retCondition ):
        self.retReason = retReason
        self.retCondition = retCondition
        print "WE ARE HERE", self.retReason
        if self.retReason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.retCondition == "in the box, like new":
            self.status = "for sale"
        elif self.retCondition == "open box":
            self.status = "used"
            self.price *= 0.8
        return self
    def displayInfo( self ):
        print " "
        print "Name:", self.name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        print "Tax:", self.taxAmount
        print "Reason for return:", self.retReason
        print "Return condition:", self.retCondition
        return self

table1 = Product( "table1", 100, 30, "Ikea", "for sale" )
table2 = Product( "table2", 100, 30, "Ikea", "for sale" )
table3 = Product( "table3", 100, 30, "Ikea", "for sale" )
table4 = Product( "table4", 100, 30, "Ikea", "for sale" )
table5 = Product( "table5", 100, 30, "Ikea", "for sale" )

table1.sell()
table2.addTax( 3.1 )
table3.returnItem( "defective", "")
table4.returnItem( "changed mind", "in the box, like new")
table5.returnItem( "did not like", "open box")

table1.displayInfo()
table2.displayInfo()
table3.displayInfo()
table4.displayInfo()
table5.displayInfo()