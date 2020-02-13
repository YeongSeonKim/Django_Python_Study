#### 2020-02-11

#  Django Autentication(인증) - django.contrib.auth 앱을 통한 회원가입/로그인/로그아웃

참고사이트 : [Django 공식사이트](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/)

## User model

### Fields(필드)

Django에서는 **User** 객체를 이용하여 계정를 관리한다.

> superuser 도 User 객체에 포함된다

User 객체에는 아래와 같은 다양한 필드들이 있다.

- username **(required)** - 중복 X, ID로 취급
- password **(required)**
- email
- first_name
- last_name
- ....

이 외에도 다양한 속성이 존재한다. 

### Attributes(속성) 

html에서 사용.

- **is_authenticated** : 로그인여부, 사용자가 인증되었는지 알수 있는 방법이다.  읽기 전용 항상 속성 True
- **is_anonymous** : 로그아웃 여부, 항상 읽기 전용 속성 False

### Methods(방법)



-----

`from django.contrib.auth.models import User` User를 import해준다.

`from django.contrib.auth import authenticate, login, logout`  

`from django.contrib.auth`앱의 `authenticate, login, logout`를 import 해준다.

## 회원가입

회원가입은 User 모델의 `create_user()`함수를 이용하면 된다.

create_user(username=user_id, email=email, password=user_pw, first_name=name )

()안에 다른 필드들 써줄수 있음

```python
from django.contrib.auth.models import User

def RegisterAccountsView(request):
    ...

		user = User.objects.create_user(username=user_id, password=user_pw, email=email, first_name=name)
```

## 인증

authenticate

인증은 간단하다!! 

```python
from django.contrib.auth import authenticate

def LoginView(request):
    ...

		user = authenticate(username=user_id, password=user_pw)
        
        if user is not None:
    		# 인증 성공
		else:
    		# 인증 실패
```

Django 에서는 **username**을 ID로 취급한다.

## 로그인

login

로그인은 인증 후 login() 함수를 사용하면 된다.

```python
from django.contrib.auth import authenticate, login

def LoginView(request):
    ...

		user = authenticate(username=user_id, password=user_pw)
        
        if user is not None:
    		login(request, user=user)
            # 성공 : 리다이렉트
			
    	else:
  	      	# 실패 : 에러메시지 전송
```

## 로그아웃

logout

```python
from django.contrib.auth import logout

# 로그아웃
def LogoutView(request):
	logout(request)
    # Redirect 할 페이지 return.
```





----

## 데이터베이스 조회 - QuerySet

> 인스타그램 클론 프로젝트에서 사용하는 방식은 Django의 model을 사용하지 않고 MySQL을 사용하여 직접 데이터를 다루면서 개발하는 방식으로 할 것이다.
>
> 기본 프로젝트 연습을 하면서 View에서 계속 sql문을 직접 입력하여 사용하여 데이터를 불러오는 방법 사용했을 것이다. Django에서 쉽게 데이터 베이스에 저장되어있는 데이터를 불러오는 방법에 대해 설명할 것이다.

`Query`란 **데이터베이스에 정보를 요청해주는 것**을 의미하며, 파이썬으로 작성한 코드가 SQL로 매핑되어 `QuerySet`이라는 자료 형태로 값이 넘어오게 된다.  

`QuerySet`은 별도로 SQL을 작성할 필요 없이 DB로 부터 데이터를 가져오고 추가, 수정, 삭제가 가능하다.

우선, QuerySet을 생성해야되는데 위에서 말했듯이 Django model을 사용하지 않기로 했기 때문에 MySQL Workbench를 통해 필요한 인스타그램 테이블들을  생성해주었다.

#### DB 데이터 조회 (Retrieve)

- **all**

  ```python
  Post.objects.all()
  ```

  모든 데이터를 다 가져온다.

- **filter** (and, or)

  ```python
  Post.objects.filter()
  ```

  특정 데이터로 필터링해서 가져온다. 인자로는 `필드명=조건값` 이 들어가며 2개 이상 들어갈 경우, 두 조건을 and로 묶어주어야한다. or 로 묶어주기 위해서는 아래와 같이 Q 를 사용해야한다.

  ```python
  from django.db.models import Q
  
  Item.objects.filter(Q(title="제목") | Q(content="내용"))
  ```

- **exclude** (제외조건)

  ```python
  Post.objects.exclude()
  ```

  filter 와 상반되는 개념으로, `필드명=조건값` 으로 들어오는 인자를 제외한 나머지 값들을 가져온다.

- **get**

  ```python
  Post.objects.get()
  ```

  `필드명=조건값` 를 인자로 가지며, 해당 하는 데이터가 유일하게 존재해야 한다. 0개이거나 2개 이상이면 에러가 발생하게 된다.

- **first**

  ```python
  Post.objects.first()
  ```

  가장 첫번째 데이터를 가져온다.

- **last**

  ```python
  Post.objects.last()
  ```

  가장 마지막 데이터를 가져온다.

- **index**, **slice**

  ```python
  Post.objects[index]
  Post.objects[start:stop:step]
  ```

  python 의 list와 같이 인덱싱 및 슬라이싱이 가능하다. 단, 음수가 들어갈 수 없다.



### DB 데이터 추가(Create)



### DB 데이터 수정 (Update)



### DB 데이터 삭제 (Delete)




