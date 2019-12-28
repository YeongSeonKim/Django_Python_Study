### 2019-12-19

# PycharmProject

## Pycharm

- 파이썬 통합개발환경(IDE)
- Community 버전으로 설치

![image-20191228143042196](images/image-20191228143042196.png)

[https://www.jetbrains.com/ko-kr/pycharm/](https://www.jetbrains.com/ko-kr/pycharm/)

## Django 프로젝트 생성

##### 1. 작업 디렉토리 생성 및 가상환경 구성

- Django 프로젝트와 관련 파일을 담을 작업 디렉토리 생성한다.
- Pycharm 첫 화면의 Create New Project 클릭

![image-20191220220705968](images/image-20191220220705968.png)

- 원하는 프로젝트 폴더 이름으로 변경, 위치 변경 가능

파이참프로젝트 django_ex1 파일을 하나 만들어준다.

![image-20191228143446587](images/image-20191228143446587.png)

Project Interpreter: New Virtualenv environment를 클릭하여 가상환경까지 함께 구성

- 가상환경 : 자신이 원하는 환경을 구축하기 위해 필요한 모듈만 모아둔 독립된 공간

  ▶ 다양한 라이브러리들 간의 충돌을 방지하기 위해 사용

- Location에 원하는 위치에 원하는 이름으로 **가상환경** 구성

- Base interpreter에서 가장 최신 버전의 파이썬을 지정 후 Create 버튼을 클릭

![image-20191228144210444](images/image-20191228144210444-1577511765518.png)

가상환경의 위치는 프로젝트 내에 설정하지않고 따로 외부에 설정해준다...! 나중에 오류 파바바박ㄱ

##### 2. Django 패키지 설치

- 왼쪽 상단의 File - Settings - Project: 프로젝트 명 - Project Interpreter 순으로 클릭

![image-20191220222441041](images/image-20191220222441041.png)

- 아래 그림과 같은 창이 뜨면 먼저 Project Interpreter가 처음에 생성한 가상환경인지 확인

![image-20191228144617591](images/image-20191228144617591.png)

- 창 오른쪽의 + 버튼 클릭

- 'Django'를 검색한 후, 하단의 Install Package를 눌러 Django 설치

![image-20191220222712556](images/image-20191220222712556.png)

- 설치가되면 아래와 같이 성공적으로 설치되었다고 뜬다.

![image-20191220223246412](images/image-20191220223246412.png)

- 창을 닫게 되면 아래의 그림처럼 설치된 패키지들의 리스트를 볼 수 있게된다.

![image-20191228144945201](images/image-20191228144945201.png)

##### 3.  **Django 프로젝트 생성**

- 프로젝트 : 개발 대상이 되는 전체 프로그램
- 하단의 Terminal 탭 클릭

![image-20191228145019247](images/image-20191228145019247.png)

- 아래 명령어를 입력하면 최상위 디렉토리 아래로 Django 프로젝트가 생성된 것을 볼 수 있다.

```bash
django-admin startproject {project_name} .
# 반드시 {project_name} 뒤에 스페이스 한번 누르고 . 입력한다.
django-admin startproject first_prj .
```

![image-20191228145149492](images/image-20191228145149492.png)

![image-20191228150916099](images/image-20191228150916099.png)

- 아래 명령어로도 Django 프로젝트를 생성할 수 있다.

  프로젝트 파일들을 모으는 또 하나의 상위 디렉토리가 만들어지기 때문에 아래의 명령어를 사용해서 최상위 디렉토리와 Django 프로젝트를 분리시킨다.

```bash
django-admin startproject {project_name}
# {project_name}에 내가 만들 프로젝프의 이름을 지정하면된다.
django-admin startproject mybookmark
```

![image-20191228150903521](images/image-20191228150903521.png)

![image-20191228150854032](images/image-20191228150854032.png)

##### 4. **프로젝트 이름 변경 및 위치 이동**

- 현재 내가 어느 위치에 있는지 Terminal 탭에서 확인
- Django 프로젝트를 변경하고 싶은 위치까지 `cd ..` 명령으로 상위 디렉토리로 이동

![image-20191228150248054](images/image-20191228150248054.png)

- 아래 명령어를 입력하면 아래 그림과 같이 Django 프로젝트가 이동한 것을 볼 수 있다.

```bash
move django_project_location {new_name}

move C:\Pycharm\PycharmProjects\django_ex1 move_mybookmark
```

![image-20191228151250013](images/image-20191228151250013.png)

- File - Open 을 클릭해 방금 옮긴 Django 프로젝트 열기

![image-20191220225612338](images/image-20191220225612338.png)

![image-20191228151423368](images/image-20191228151423368.png)

![image-20191220225728829](images/image-20191220225728829.png)

![image-20191228151543704](images/image-20191228151543704.png)

##### 5. settings.py 설정

![image-20191228151655238](images/image-20191228151655238.png)

- 먼저 TEMPLATES의 DIRS 부분을 아래와 같이 변경

```python
'DIRS': [os.path.join(BASE_DIR, 'templates')]
```

![image-20191228151739962](images/image-20191228151739962.png)

- 나머지 부분도 다음과 같이 변경

기존

![image-20191228152341074](images/image-20191228152341074.png)

- STATIC~ : 프로젝트의 정적 파일과 관련된 사항을 지정
- MEDIA~ : 미디어 관련 사항을 지정, 파일 업로드 기능을 개발할 때 필요

변경 후

```python
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# 여기서부터는 수동으로 직접 지정
STATIC_URL = '/static/'
STATICFILES_DIR = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

![image-20191228153603805](images/image-20191228153603805.png)

##### 6. **Django 기본 테이블 생성**

- Django는 모든 웹 프로젝트 개발 시 사용자와 사용자의 권한 그룹 테이블이 반드시 필요하다는 가정 하에 설계되었기 때문에 우리가 테이블을 만들지 않았더라도 위의 테이블들을 만들어주기 위해 개발 시작 시점에 `python manage.py migrate` 이 명령을 실행
- 먼저 Terminal 탭을 클릭하여 이전에 생성한 가상환경이 활성화가 되어있는지 확인
- 비활성화 되어있다면 File - Settings - Project - Project Interpreter로 들어가 가상환경 적용
- 아래 명령어를 입력하면 Django의 기본 DB 파일, sqlite3 DB 파일이 생성된다.

```bash
python manage.py migrate
```

![image-20191228153744414](images/image-20191228153744414.png)

파이참에서는 settings.py 에서 `LANGUAGE_CODE = 'ko-kr'`이면 migrate가 안된다아아ㅏ,,, 

##### 7. superuser(관리자 계정 ) 생성

- 나중에 Admin 페이지에 접속하여 작업하기 위한 관리자 계정을 생성

```bash
python manage.py createsuperuser
```

![image-20191228154115297](images/image-20191228154115297.png)

##### 8. Django 테스트 서버 설정

아래의 명령어로 테스트 서버를 실행할 수 있다. 그러나 실행환경을 구성하면 더 쉽게 테스트 서버를 실행할 수 있기 때문에 실행환경을 구성해보도록 하자.

```bash
python manage.py runserver
```

![image-20191228154457000](images/image-20191228154457000.png)

http://127.0.0.1:8000/ 를 클릭하게 되면 아래의 우주선 모양이 나오는 사이트가 나오면 성공!!

![image-20191228154536754](images/image-20191228154536754.png)

- 상단 바에 있는 Run - Edit Configurations 클릭

![image-20191228155101415](images/image-20191228155101415.png)

- 아래 사진과 같은 창이 뜨면 왼쪽 상단의 + , Python 클릭

![image-20191228155147010](images/image-20191228155147010.png)

- Name: 원하는 이름으로 설정
- Script path: Django 프로젝트의 manage.py 를 찾아 설정
- Parameters: runserver 로 설정
- Python interpreter: 이전에 만든 가상환경으로 설정되어 있는지 확인

![image-20191228155818162](images/image-20191228155818162.png)

##### 9. 테스트 서버 실행

- 오른쪽 상단의 Run 버튼을 눌러 실행
- http://127.0.0.1:8000/ 을 클릭
- http://127.0.0.1:8000/ : 로컬 서버

![image-20191228154457000](images/image-20191228154457000-1577516667522.png)

아래의 우주선 모양이 나오는 사이트가 나오면 성공!!

![image-20191228154536754](images/image-20191228154536754-1577516915853.png)