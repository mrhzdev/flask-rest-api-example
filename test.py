class A:
  def _method(self):
    print(self)
    return
  @classmethod
  def _class_method(cls):
    print(cls)
    return  
  @staticmethod
  def _static_method():
    print('Statclsic method')
    return

A()._method()
print(A())
A()._class_method()
print(A)
A()._static_method()

def test_return():
  return 'foo','bar','baz'

print(test_return())