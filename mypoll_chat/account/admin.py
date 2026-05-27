# account/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# 사용자 정의 UserAdmin 정의
## 관리자 앱에서 User의 어떤 항목(Field)들을 관리할지 정의.
## UserAdmin을 상속해서 구현. admin.site.register() 에 모델과 함께 등록.

# UserAdmin에서 정의할 것 (class변수로 정의)
## list_display: list - 사용자 메인 화면에서 목록에 나올 항목들 정의
## add_fieldsets : tuple - 등록 화면에 나올 항목들 지정
## fieldsets: tuple - 수정화면에 나올 항목들 지정

# field: 개별항목
# fieldset: field들을 그룹으로 묶은 것.(category)

class CustomUserAdmin(UserAdmin):
    # 목록에 나올 User의 field들 
    list_display = ["username", "name", "email"]
    # 등록화면 구성
    add_fieldsets = (
        ("인증정보", {"fields":("username", "password1", "password2")}), # 개별 fieldset
        ("개인정보", {"fields":("name", "email", "birthday")}),
        ("권한", {"fields": ("is_staff", "is_superuser")})
    )
    # 수정화면 구성
    fieldsets = (
        ("인증정보", {"fields":("username", "password")}), # 개별 fieldset
        ("개인정보", {"fields":("name", "email", "birthday")}),
        ("권한", {"fields": ("is_staff", "is_superuser")})
    )

admin.site.register(CustomUser, CustomUserAdmin)