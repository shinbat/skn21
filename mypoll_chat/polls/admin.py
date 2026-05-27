from django.contrib import admin
from .models import Question, Choice
# .models -> .: 현재 모듈(admin.py)와 같은 패키지를 가리키는 것.

# Register your models here.
# 관리자 앱에서 Model의 Data를 관리할 수 있도록 등록.
## admin.site.register(모델클래스)
admin.site.register(Question)
admin.site.register(Choice)