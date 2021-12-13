# module_sample 불러오기
print(module_sample.module_sample1(1, 2))


# module_sample 이름을 줄여서 ms로 사용 가능함
ms.module_sample2('ms')
ms.module_sample3()


# from import 모듈 가져오기
from python_basic.summary.module_sample import *
print(module_sample1(1, 2))  # 객체처럼 접근하지 않고 바로 메서드로 활용 가능하다는 점에서 import module (as alias) 와 다르다.

from python_basic.summary.module_sample import module_sample1, module_sample2   # 모듈을 , 로 필요한 것들만 가져올 수 있다.
print(module_sample1(3, 4))
module_sample2('from module_sample import module_sample1, module_sample2')

from python_basic.summary.module_sample import module_sample1 as ms1  # 불러온 메서드 또한 alias를 붙일 수 있다.
print(ms1(5, 6))

from python_basic.summary.module_sample import module_sample2 as ms2  # 다양한 응용법
ms2('from module_sample import module_sample1 as ms1, module_sample2 as ms2')


# pakage 불러오기
# import pakage_sample.pakage1.Pakage1 과 같이 모듈까지만 가능하고 내부 메서드, 클래스에는 접근불가
from python_basic import pakage_sample as p1

p = p1.Pakage1()

from python_basic.pakage_sample.pakage1 import Pakage1  # 만약 해당 클래스, 메서드를 불러와서 사용하고 싶다면 from import를 이요하면 된다.
p = Pakage1()


# __all__
# pakage 내 __init__.py 파일에 __all__ 변수에 해당모듈의 이름을 넣지 않으면 from pakage import * 에서 __all__에 있는 모듈만 불러오게 된다.
# 따라서, pakage 내의 __init__.py 에 __all__ = ['pakage'] 라고하여야 * 이 정상적으로 작동한다.


# __main__
# 모듈의 호출이 모듈 내에서 호출이 되는지, 아니면 외부에서 호출이 되는지 확인할 수 있는 방법은 __main__을 비교해주면 된다.
# 코드를 보려면 ./pakage_sample/pakage1.py 확인
