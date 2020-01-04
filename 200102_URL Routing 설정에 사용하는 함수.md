#### 2020-01-02

# URL Routing 설정에 사용하는 함수

## 1. include(), path()

### 1.1 include()

`프로젝트이름/urls.py`에서 `애플리케이션이름/urls.py`에 있는 urls.py와 연결해주기 위해서 필요한 함수이다.

사용하기 위해서는 `from django.urls import include` 코드를 입력해 줘야한다.

### 1.2 path()

사용하기 위해서는 `from django.urls import path` 코드를 입력해 줘야한다.

URL경로 상에서 `<컨버터:전달할키워드인자명>`과 같은 꺽쇠괄호가 들어 있는 URL을 인식하여 뷰 함수에 키워드 인자로 전달해준다.

- 컨버터의 종류
  - `str` : 경로 구분자를 제외한 비어 있지 않은 문자열
  - `path` : 경로 구분자를 포함한 비어 있지 않은 문자열
  - `int` : 0 또는 임의의 양의 정수와 일치
  - `slug` : 문자 또는 숫자와 하이픈 및 밑줄 문자로 구성된 슬러그 문자열과 일치. 예를 들어, I-STUDY-DJANGO

### 1.3 예제코드

```python
from django.urls import path,include

urlpatterns = [
    ...
    path('애플리케이션이름/', include('애플리케이션이름.urls')),
    path('', views.view에서 지정해준 함수명, name='지정할 이름'),
]
```

`path('애플리케이션이름/', include('애플리케이션이름.urls')),` 코드는 `애플리케이션이름/`까지 `프로젝트이름/urls.py` 파일에서 해석을하고 `include('애플리케이션이름.urls')`함수를 통해서 `애플리케이션`디렉토리 아래있는 urls.py 파일을 해석할 수 있게 해준다. 

### + 나는 위의 내용은 알고 있지만 아래의 re_path()를 사용하여 정규표현식을 쓰는 방식은 처음봐서 공부를 해볼거다!! 

## 2. re_path()

django 2.0 이전에서 사용하던 url 함수와 동일한 함수이다.

- 정규표현식을 포함한 url 패턴을 지정한다.
  - `^` : 정규표현식 시작 기호
  - `$` : 정규표현식 종료 기호

