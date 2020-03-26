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
#decorator: 여러개 데코레이터를 사용하면, func실행기준으로 하나씩 차례로 into 실행 됨.
def print_more(func):
  def wrapper(*args, **kwargs):
    print('func:', func, __name__)
    print('args:', args)
    print('kwargs:', kwargs)
    result = func(*args, **kwargs)
    print('result:', result)
    return result
  return wrapper

#decorator: 함수 전 후에 기능 추가, 다른 함수가 왔을 때에도 같은 전후처리 가능
def print_info(func):
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return wrapper

#function
@print_info #먼저 실행
@print_more
def add_num(a,b):
  return a+b

#run by raw
#f = print_info(add_num)
#r = r(10,20)

#run by @
r = add_num(10,20)
print(r) # start end 30

###### ramda ######
l = ['Mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def change_words(words, func):
  for word in words:
    print(func(word))
    
#인수로 넘어가서 실행되는 함수
##def sample_func(word):
##  return word.capitalize()

#위 sample_func 코드를 간단하게 실행하는 방법
##sample_func = lambda word: word.capitalize()
##change_words(l, sample_func)

#(더 간단하게) lambda 직접 사용 -> 함수를 많이 만들지 않아도 됨.
change_Words(l, lambda word: word.capitalize())

###### generator ######
#반복처리시 한 요소를 꺼내서 생성해나가는 역할?
l = ['good morning', 'good afternoon', 'good night']

for i in l:
  print(i)
  
def greeting():
  yield 'good morning'
  yield 'good afternoon'
  yield 'good night'
  
for g in greeting(): #greeting yield에 선언된 것들 선택
  print(g)
  
g = greeting()
print(next(g))
print('blahbla')
print(next(g)) #greeting yield로 생성된 것들 차례로 출력

###### except ######

###### class ######
# 덕타이핑
# 추상클래스
# 다중상속
# 클래스 메소드 / 스태틱 메소드
# 특수메소드


