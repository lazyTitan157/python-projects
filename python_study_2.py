###### Docstrings ######
def example_func(param1, param2):
  """
  """
example_func.__doc__

###### function in function ######
def outer():
  def inner_func(a):
    return a;
  b = inner_func('a')
  c = inner_func('b')
  return
outer() #함수 내에서 여러번 이너 함수를 쓰는 경우 사용

###### closure ######
def outer(a,b):
  def inner(c):
    return a+b+c
  return inner
f = outer(1,2) #인수입력 후, 
#함수에 인수입력과 실행하는 시간 사이를 만들 수 있음 = 중간에 인수를 변경해서 함수 사용 가능 
result = f(3) #inner()실행 
print(result)

###### decorator ######


###### ramda ######

###### generator ######

###### except ######

###### class ######
# 덕타이핑
# 특수메소드
