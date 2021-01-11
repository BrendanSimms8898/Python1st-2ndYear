









      c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare')
      c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon')
      c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry')
      l = []
      l.append('Amount due: {-:.2f}'.format(self.owes()))
      l.append('Balance: {:.2f}'.format(self.balance))
      l.append('Discount: {:.0f}%'.format(self.discount * 100))
      l.append('{}'.format(self.a1))
      l.append('{}'.format(self.a2))
      l.append('{}'.format(self.a3))
      l.append('{}'.format(self.name))
      print(c1)
      print(c2)
      print(c3)
      return '\n'.join(l)
      return self.balance * (1 - self.discount)
      self.name, self.balance, self.a1, self.a2, self.a3 = name, balance, a1, a2, a3
    def __str__(self):
   def __init__(self, name, balance, a1, a2, a3):
   def main():
   def owes(self):
   discount = 0
   discount = 0.1
   main()
#!/usr/bin/env python
class Customer(object):
class ValuedCustomer(Customer):
if __name__ == '__main__':