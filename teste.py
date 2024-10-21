class A:
     def __init__(self, x):
          self._x = x
          self.attributes_name = 1

     def __getattr__(self, attributes):
               print('calling getattr')
               return 'atributo'
     def __getattribute__(self, x):
          print('calling getatribute')
          return 3


a = A(5)

# print(vars(a))
print(a.attributes_name)