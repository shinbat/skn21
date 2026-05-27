# polls/urls.py
# polls app에 대한 url-view 매핑파일 (URL Conf)

# URLConf  - urlpatterns =[ 매핑 설정 ]
# 매핑 설정 - path("url경로", View, name="설정식별이름") 함수를 이용

from django.urls import path
from . import views   # 상대 경로로 import. `.` 현재 모듈이 있는 패키지.

app_name = "polls" # 전체 설정에 대한 prefix(namespace). 
                   # 설정 name에 공통적으로 앞에 붙일 이름 ("app_name:name")

urlpatterns = [
    path("welcome", views.welcome, name="welcome"),
    path("vote_list", views.list, name="list"), # polls/list -> polls/vote_list
    path("vote_form/<int:question_id>", views.vote_form, name="vote_form"),
    path("vote", views.vote, name="vote"),
    path("vote_result/<int:question_id>", views.vote_result, name="vote_result"),
    path("vote_create", views.vote_create, name="vote_create"),
    path("vote_delete/<int:question_id>", views.vote_delete, name="vote_delete"),
]


# polls/vote_form/<path파라미터값 타입:view의 파라미터변수명>
# <int:   #path parameter값을 int로 전달해라.
# <   :question_id> # view의 question_id 변수로 전달해라.
# type: int, str