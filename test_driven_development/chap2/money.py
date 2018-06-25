
class Dollar:
    def __init__(self,amount):
        self.amount=amount

    def times(self,multiplier):
        return Dollar(self.amount*multiplier)



if __name__=="__main__":
    dol=Dollar(10)
    tmp=dol.times(3)
    print(tmp.amount)