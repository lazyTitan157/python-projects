###### list ######
r = [ 1,2,3,4,5,1,2,3 ]
print(r.index(3))
print(r.index(3,3))
print(r.count(3)) #count '3' = 2

if 5 in r:
  print('exist')
  
print(r.sort())
print(r.sort(reverse=True))
print(r.reverse())

s = 'Hello, python.'
to_split = s.split(' ')
x = ' '.join(to_split)
print(x)

print(help(list)) # print document
#append, pop, ...

i = [ 1,2,3,4,5 ]
#j = i # not good
j = i.copy() #or j = i[:]

###### tuple ######
t = ( 1,2,3,4,5,1,2 )
print(t[0:2])
print(help(tuple))
# index(), count(), t = ([],[]), t[0][0]
# tuple 내 데이터는 append나 수치 변환 불가능

a, b = (10, 20) # x=10, y=20
a, b = b, a   #swap is so easy

###### dictionary (using hashtable) ######
d = { 'var':'data', 'var2':'data2'}
d['var'] = 100
d[1] = 100

d = dict(a=10, b=20) # { 'a':10, 'b':20 }

print(help(d)) # dictionary method
d.keys()
d.values()

d2 = {'newkey':'data'}
d.update(d2)
d.get('newkey')
d.pop('x') #print and delete
print(d)

if 'newkey' in d:
  print('newkey is in d')
  
d.clear() # d = {}
del d # delete d

#d = d2 # same address
d = d2.copy() # copy dictionary contents

###### set ######
s = { 1,2,3,4,5 }
s2 = { 1,3,7 }
print(s-s2) #{2,4,5}
print(s2-s) #{7}
print(s&s2) #and
print(s|s2) #or

s.add(6)
s.remove(6)
s.clear()
print(type(dictionary))   # {}
print(type(set))  #set()

kind = set(r) #list to set = 중복제거

"""
주석 여러줄 처리
"""

s = 'aaaaaaaaaaaaaaaaaa' \
  + 'bbbbbbbbbbbb'
print(s)

###### logical calculation ######
a = 1
b = 1
print(a==b)
print(a!=b)
print(a<b)
print(a<=b)
print(a>0 and b>0)
print(a>0 or b>0)

###### in / not ######
x = 1
y = [1,2,3]

if x in y:
  print('in')
if 10 not in y:
  print('not in')  
if not x==y[0]:
  print('Not equal')

is_ok = True # 0/0.0/[]/()/{} is false
if not is_ok: #if is_ok != True
  print('False')

if is_not_ok:
  print('False')
  
###### null object ######
is_empty = None # NoneType class
if is_empty is None: #if is_empty == None # not good
  print('None!!!')
  
print(1 == True) # True
print(1 is True) # false, object도 비교
print(True is True) #True

###### condition ######
while True:
  continue # do next loop
  break # finish loop
  
while True:
  word = input('Enter: ')
  if word == 'ok':
    break;
else:
  print('done') #last do (break 대신 사용가능)

###### iterator ######
for index in y:
  print(index)
  #continue, break
else:
  print('print all!')
  
###### inner function ######
print(range(2, 10, 2)) #2, 4, 6, 8 (range(2,10) = 2~9)

for i, number in enumerate(y):  #y=list
  print(i, number)
  
# list r, y
for r_data, y_data in zip(r,y):
  print(r_data, y_data)

for content in d:
  print(content) #key
for k, v in d.items():
  print(k, ':', v)
print(d.items()) 

###### function definition ######
#say_something #undefined

#def say_something(something):
def say_something(something: string) -> string: #인수/반환값 선언형 함수정의
  s = something
  return s
result = say_something('hi')
print(result)

num: int = 10
print(num) #10
s_result = say_something('hi')
print(s_result)

# list는 default인수로 사용하면 안됨. default인수인 리스트가 프로그램 내에서 한번만 생성됨
def say_manything(one='default', two, three, four=None): #four=[] 사용금지
  print(one)
  print(two)
  print(three)
  if four is None: # 빈 리스트일때 []로 초기화
    four = []
say_manything(one='hi', two='everybody', three='!')
say_manything(one='hi', 'two is everybody', three='!') #위치 주의

# 위치인수의 튜플화
def say_somewords(word, *args):
  print(word)
  for arg in args:
    print(arg)
say_somewords('hi', 'args', 'is', 'this')
t = ('args','is','tuple')
say_somewords('hi', *t) #tuple unpacking, not usual

# 키워드인수의 사전화
def menu(**keywordargs):
  for k,v in keywordargs.items():
    print(k,v)
d = {'key':'val', 'key2':'val2'}
menu(d)
menu(key='val', key2='val2')

def many_menu(just, *args, **kwargs):
  print(just) #string
  print(args) #('', '') #tuple
  print(kwargs) #{'key':'val'} #dictionary
many_menu('string', '', '', key='val')

###### Docstrings ######

###### function in function ######

###### closure ######

###### decorator ######

###### ramda ######

###### generator ######

###### except ######

###### class ######
# 덕타이핑
# 특수메소드
