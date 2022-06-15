# DRF_study
DRF_study

과제
## 1. args, kwargs를 사용하는 예제 코드 짜보기
 ```python
class People:
    def __init__(self, **kwargs):
        self.info = kwargs
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.is_worked = kwargs.get('is_worked')


john = People(name='john', age=25, is_worked=True)
print(john.info)
print(john.name, john.age, john.is_worked)


class Human:
    def __init__(self, *args):
        self.info = args
        self.name = args[0]
        self.age = args[1]
        self.is_worked = args[2]


peter = Human('peter', 23, True)
print(peter.info)
print(f'name : {peter.name}, age: {peter.age}, is_worked : {peter.is_worked}')

 ```
## 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
기본형 데이터 타입들이 immutable, 파이썬에선 list, dict 와 같은 참조형 타입들이 mutable
Immutable 객체	int, float, str, tuple
Mutable 객체	list, dict

수정불가능한 객체 즉 immutable 객체는 기존 객체는 그대로 있고 항상 새로 생성되고 기존 객체는 가비지컬렉터에 의해 자동으로 삭제가 되나
이러한 동작들이 순식간에 이루어지기 때문에 우리는 그냥 덮어씌워 지는구나 착각하는 것 실제로 덮어 씌워지는 경우는 참조형 데이터들을 사용할 때 인데
list, dict 같이 수정 가능한 객체 mutable 객체의 경우는 해당 주소값을 직접 가지고 있는게 아닌 가리키고 있는 것이기 때문에 안의 원소를 변경할 경우
다른 인스턴스에도 영향을 미치게 된다.
```python
a = ["python2", "python3"]
print(a)
b = a
print(b)
a.append("python4")
print(f'a : {a}')
print(f'b : {b}')

>>> ['python2', 'python3']
>>> ['python2', 'python3']
>>> a : ['python2', 'python3', 'python4']
>>> b : ['python2', 'python3', 'python4']
```
append로 데이터를 추가 했을 때 b에도 영향이 가는 것을 볼 수 있다. append 아니고 그냥 등호로 사용하게 되면 다시 새로운 선언을 하는 거기 때문에   
immutable 처럼 새로 생성되고 이전 객체는 가비지컬렉터에 자동으로 삭제가 되간한다.   
<br>
## 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
Primary Key - 하나의 필드에서 다른 필드와 구분을 위한 고유한 key, 중복 X, null값을 가질 수 없음, 무조건 하나는 있어야하며 없어서도 여러개 있어서도 안되는 key    
Foreign Key - 다른 테이블과의 관계성을 연결하기 위한 key 다른 테이블의 primary key와 연결되어 데이터의 참조관계를 만들기 위해서 사용하는 key    
Unique Key - 해당 컬럼의 레코드값이 다른 필드와 중복을 피하기 위해 지정하는 key 대신에 null은 입력 가능함   
Not Null이나 Check 로 제약조건도 걸어줄 수 있다.   

## 4. django에서 queryset과 object는 어떻게 다른지 서술하기
queryset의 형태는 DB 에서 전달 받은 objec들의 list 이다. 전달받은 object의 형태는 dict 이다.    
그래서 queryset 으로 받아온 데이터를 빼내서 사용하려면 for문을 이용해서 각각 데이터에 접근을 하고    
각각의 object 들은 dict 형태 이므로 그에 맞는 key 에 접근해서 value를 얻어 낼 수 있다.    
```python
ex)     
User.objects.all()    
<QuerySet [<user: 1>, <user: 2>]>    
User.objects.all().values()    
<QuerySet [{id: 1, name: 홍길동}, {id:2, name:이순신}]>    
```
