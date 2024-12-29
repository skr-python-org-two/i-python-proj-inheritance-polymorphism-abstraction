
import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('foo')
    def method1(self, x, y, z):
        pass
    def method2(self):
        pass

@zope.interface.implementer(MyInterface)
class MyClass:
    foo = "24"
    def method1(self, x,y,z):
        return x** 2

    def method2(self):
        return "foo"


obj = MyClass()
print(obj.method1(5,6,7))
print(obj.method2())
print(obj.foo)

