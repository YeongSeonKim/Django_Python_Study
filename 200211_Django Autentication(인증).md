#### 2020-02-11

#  Django Autentication(인증)

웹 사이트에서 현재 접속한 사용자가 로그인이 되어있는지 로그인이 되어있다면 어떤 사용자이고 어떤 권한을 가지고 있는지그에 따라 사용할 수 있는 기능이나 페이지에 제한을 두고 있다. 이와 같은 로직을 구현하기 위해서는 먼저 사용자를 인증하는 과정을 거쳐줘야 한다. Django에서는 사용자 인증 및 권한 승인 시스템을 다양한 기능들과 함께 제공해준다.

참고사이트 : [Django 공식사이트](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/)

## User 

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



## 1. User 생성 - 회원가입

회원가입은 User 모델의 `create_user()`함수를 이용하면 된다.

`create_user(username, email=None, password=None, **extra_fields)`

()안에 다른 필드들 써줄수 있음

```python
from django.contrib.auth.models import User

def RegisterAccountsView(request):
    ...
	# 방법1
    	user = User.objects.create_user('test', 'test@test.com', 'password')
    # 방법2
		user = User.objects.create_user(username=user_id, password=user_pw, email=email, first_name=name)
```

- superuser

앱을 생성하고 admin 페이지를 관리하기 위해 `python manage.py createsuperuser` 명령문을 날리는데 이렇게 슈퍼유저를 생성한 것처럼 함수를 사용하여 슈퍼유저를 생성할 수 있다.

`create_superuser(username, email, password, **extra_fields)`

```python
from django.contrib.auth.models import User

def createSuperUser(request):
    superUser = create_superuser('test', 'test@test.com', 'password')
```

## 2. User 정보수정

비밀번호가 변경되면 모든 세션에서 로그아웃 된다.

```python
from django.contrib.auth.models import User
user = User.objects.get(username='test')
user.email='test@test.com'
# 비밀번호 변경
user.set_password('new password')     

# 수정 후 save()를 해줘야 영구적으로 반영된다.
user.save()        
```

## 3. User 인증

`authenticate(request=None, **credentials)`

User 인증 함수이다. 인증은 간단하다!! 

자격증명이 유효한 경우 User 객체를 반환, 그렇지 않은 경우에는 None을 반환

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

## 4. 로그인

로그인은 인증 후 login() 함수를 사용하면 된다.

`login(request, user, backend=None)`

Django의 세션 프레임 워크를 사용하여 세션에 인증된 사용자의 ID를 저장한다.

```python
from django.contrib.auth import authenticate, login

def LoginView(request):
    ...

		user = authenticate(username=user_id, password=user_pw)
        
        if user is not None:
    		login(request, user)
            # 성공 : 리다이렉트
			
    	else:
  	      	# 실패 : 에러메시지 전송
```

## 5. 인증 확인

인증이 되어야 들어갈 수 있는 페이지와 기능 등을 위해서 로그인한 사용자의 계정이 인증이 되었는지 확인을 할 필요가 있다.

먼저, 인증확인 실패 시 리다이렉트할 경로를 설정해 준다.

```python
# settings.py
...
LOGIN_URL = '/login/'
```

### 5.1 Views.py에서 인증 확인

`is_authenticated` : 대상 User 객체의 로그인 여부를 확인한다.

```python
# views.py
def LoginView(request):
    if request.user.is_authenticated:
        # 로그인한 유저인 경우
        ...
    else:
        # 로그인 하지 않은 유저인 경우
        ...
```

`login_required()` : auth의 데코레이터(decorators)를 사용하면 로그인하지 않은 유저에 대한 처리를 위의 방법보다 더 간단하게 구현할 수 있다.

- `login_required(redirect_field_name='next', login_url=None)`

  : 지정된 인자값이 없을 경우, settings.py에 설정한 `LOGIN_URL` 로 리다이렉트

```python
from django.contrib.auth.decorators import login_required

@login_required
def example1(request):
    ...
    
# redirect_field_name
@login_required(redirect_field_name='login')
def example2(request):
    ...
    
# login_url
@login_required(login_url='/accounts/login/')
def example3(request):
    ...    
```

### 5.2 Templates에서 인증 확인

```django
...
{% if user.is_authenticated %}
    <a href="{% url 'login:logout' %}">로그아웃</a>
{% else %}
    <a href="{% url 'login:login' %}">로그인</a>
{% endif %}
...
```

## 6. 로그아웃

`logout(request)` : 현재 request에 대한 세션 데이터를 모두 삭제해준다.

```python
from django.contrib.auth import logout

# 로그아웃
def LogoutView(request):
	logout(request)
    # Redirect 할 페이지 return.
```


