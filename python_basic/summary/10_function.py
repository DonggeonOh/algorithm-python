# 함수의 정의
def function():
    print('function')
function()


# 매개변수는 있지만 반환 값이 없는 함수
def function_param(param1, param2):
    print(param1, param2)
function_param(10, 20)


# 매개변수와 반환 값이 있는 함수
def function_return(param1, param2):
    return param1 + param2
print(function_return(100, 200))


# 매개변수는 없지만 반환 값이 있는 함수
def function_no_param_return():
    return 'Hello World'
print(function_no_param_return())


# 함수의 매개변수에 기본 값을 넣는 방법
def function_default(name = 'Oh Donggeon', age = 26):
    return name + ' ' + str(age)
print(function_default())
print(function_default(name="Dong-geon Oh", age = 30))  # 매개변수의 키워드 활용
print(function_default(age = 30, name='Dong-geon Oh'))  # 순서를 바꿔도 가능하다.


# 함수의 가변인자
def function_variable_args(name, age, *langs):
    lang_str = ''
    for lang in langs: lang_str += lang + ' '
    return '{0} {1} {2}'.format(name, age, lang_str)
print(function_variable_args('O.D.G', 26, 'C', 'C++', 'Java', 'Swift'))


# 전역변수
global_variable = 10
def function_global_variable(int):
    global global_variable  # 내부의 변수가 아닌 외부의 전역변수를 사용한다.
    global_variable = int
function_global_variable(20)
print(global_variable)