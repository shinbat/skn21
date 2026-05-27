# 프로젝트 생성

1. 디렉토리 생성
 - mypoll (application 디렉토리)

2. mypoll 아래로 이동 -> 터미널 실행(cmd)

3. 가상환경
 - uv venv .venv --python=3.12
 - .venv\Scripts\activate  (활성화)
  
4. django 설치
 - uv pip install django

5. 장고 프로젝트 생성
 - 프로젝트 디렉토리(mypoll)안에서 다음 명령어를 실행.
 - django-admin  startproject config .

6. 개발 서버를 실행

  - python  manage.py  runserver
  - web browser
     - http://127.0.0.1:8000

7. app을 생성
  - python  manage.py  startapp  앱이름
  - python  manage.py  startapp  polls

  - config/settings.py 열기
     - 생성한 app을 등록
       - INSTALLED_APPS 에 app이름을 추가.

8. 관리자 계정 생성 (관리자페이지를 사용할 수 있는 권한을 가진 계정)
   - python manage.py migrate
   - python manage.py createsuperuser
       - username
       - email 주소
       - Password: 1111
9. 관리자 페이지 
   1. 서버 실행
	- python manage.py runserver
        - http://127.0.0.1:8000/admin

10. 한글, 타임존 설정
   - config/settings.py
	- LANGUAGE_CODE = 'ko-kr'  //언어코드-국가





# accout app 구현
- 사용자 관리 앱

- app을 생성
  - python manage.py startapp account
  - config.settings INSTALLED_APP에 추가.
  - account app용 urls.py 를 정의
    - account/urls.py urlpatterns 설정
    - config/urls.py 에 account urls.py(url-conf)를 등록

- Model
  - AbstractUser 상속
  - admin.py 에 등록 (admin app에서 관리할 수있는 데이터)
  - 사용자 관리 할 때 사용할 User 모델을 기본 모델에서 우리가 만든 것으로 변경
    - config.setting : AUTH_USER_MODEL = "account.CustomUser"

account\migrations 디렉토리 삭제
root\db.sqlite3

  - python manage.py makemigrations account
  - python manage.py migrate
  - python manage.py createsuperuser
  
  - python manage.py runserver
http://127.0.0.1:8000/admin

- Form
  - account/forms.py 파일 생성.
  - Model Form을 정의

- 템플릿 폴더 생성
  - account/templates/account

- django-bootstrap5 
  -  폼을 이용해서 등록/수정 페이지를 만들 때 bootstrap 디자인을 적용해주는 lib.
  -  uv pip install django-bootstrap5
  -  config/settings.py INSTALLED_APP으로 등록
  -  template
  ```
  {% load django_bootstrap5 %}   -> 태그들을 사용할 수있도록 로드

  {% bootstrap_form  폼변수 %} -> {{폼변수}} 대신
  ```


  # 파일 업로드
  - settings.py
    - MEDIA_URL
    - MEDIA_ROOT 
  - Model
    - ImageField 추가
  - Form
    - profile_img 를 fieldsets에 추가.
  - create/update.html 
    - <form method="post" enctype="multipart/form-data">
  - view: create/update에서 Form생성시 request.FILES 를 initializer에 넣어서 생성한다.
  - detail.html 에서 업로드된 파일이 나오도록 처리.
  - config/urls.py url 설정.