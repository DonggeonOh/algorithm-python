class Parent:
    def __init__(self, var1):  # 파이썬의 생성자
        self.var1 = var1

    def parent_method(self, var2):
        return self.var1 + var2

    def method_overriding(self):
        pass

class Child(Parent):
    class_variable = 10  # 클래스 변수 초기화, Child 객체에서 공유하여 사용한다. Child.class_variable 로 접근한다.

    def __init__(self, var1, var2):  # 객체의 인스턴스 변수를 초기화한다. 객체이름.var1, 객체이름.var2로 접근한다.
        super().__init__(var1)       # 인스턴스 변수는 각 객체마다 독립적이다. 파이썬은 인스턴스 변수를 클래스 내부에 작성하지 않는다.
        self.var2 = var2             # 클래스 내의 변수는 다른 언어의 static 과 같다. (class_variable은 클래스 변수)

    def child_method(self, var3):
        return self.var1 + self.var2 + var3

    def method_overriding(self):  # 메서드 오버라이딩이 간단하다. 참고로 파이썬은 오버로딩은 지원하지 않는다.
        pass

    # 메서드를 선언할 때 self가 맨 처음 매개변수로 들어가 있는 이유는 메서드를 호출한 해당 객체가 자동으로 self 매개변수로 들어간다.
    # 파이썬은 관례적으로 self 라는 키워드를 사용하고 사실 다른 키워드여도 상관 없다. (위의 first_param_changed_name(name) 확인해보자.)
    # child.param_changed_name(a, b):         def param_changed_name(name, a, b):
    #   |                                                             |  객체가 자동으로 전달된다.
    #   ---------------------------------------------------------------
    # 클래스의 메서드를 호출하는 다른방법이 있다 (자주 쓰이지 않는 방법)
    def self_param_changed_name(name, a, b):
        return name.var1 + name.var2 + a + b

# 메서드 호출 방법 중 다른 방법이다 (잘 쓰이지 않는다)
a = Child(1, 2)
Child.self_param_changed_name(a, 10, 20)  # 클래스이름.메서드 로 객체를 넘겨 메서드를 불러 올 수 있다.
# 파이썬은 외부에서 클래스의 인스턴스 변수를 만들어서 쓸 수 있다
class_ex = Child(10, 20)
class_ex.var3 = 10
print(class_ex.var3)


# 파이썬은 다중상속을 지원한다. (다른 Java, Swift 와는 달리 인터테이스, 프로토콜이 아닌 다중상속으로 다형성을 지원한다.)
class ClassA:
    def __init__(self, classa):
        self.classa = classa

    def classA_method(self):
        return self.classa

class ClassB:
    def __init__(self, classb):
        self.classb = classb

    def classB_method(self):
        return self.classb

class MultiInherit(ClassA, ClassB):
    def __init__(self, classa, classb):  # 다중상속의 경우 super()로 생성자를 초기화 하게 되는 경우 맨 앞의 상속 받은 객체만 초기화 된다.
        ClassA.__init__(self, classa)    # 따라서 명시적으로 클래스 마다 선언하여 초기화 해줌으로써 다중 상속 받은 객체를 초기화 할 수 있다.
        ClassB.__init__(self, classb)

    def multi_inherit_method(self):
        return self.classa + self.classb


# pass 키워드
class ClassC(ClassA, ClassB):
    def __init__(self, classa, classb):  # 일단 코드 내에서 완성된 것 처럼 패스한다는 의미(?)
        pass

    def pass_method(self):  # pass의 의미는 아무 것도 하지 않고 넘어간다는 의미
        pass

class ClassD:  # 아무런 기능 없이 ClassD 클래스를 작성 할 수 있다
    pass
