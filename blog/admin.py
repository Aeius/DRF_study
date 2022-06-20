from django.contrib import admin
from blog.models import *
from user.models import *

# Register your models here.


class UserProfileInline(admin.StackedInline):
    '''
    StackedInline : 세로 정렬
    TabulraInline : 가로 정렬
    '''
    model = UserProfile
    # 취미 선택 및 구분 하기 좋게 창 구분 지어줌
    filter_horizontal = ['hobby']

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'fullname', 'email') #목록에 표시할 필드
    list_display_links = ('username', 'fullname' ) # 클릭 가능하게 하는 것
    search_fields = ('username', ) # 검색 기준
    readonly_fields = ('username', 'join_date', ) # 읽기전용 필드
    # 상세 내용 목차별로 출력할 필드
    fieldsets = (
        ("info", {'fields': ('username', 'fullname','email', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', )}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return('username', 'join_date', )
        else:
            return('join_date', )

    # 다른 테이블이지만 상세 내용에 표시할 정보(역참조관계여야함!)
    inlines = (
            UserProfileInline,
        )

    def has_add_permission(self, request, obj=None): # 추가 권한
        return True

    def has_delete_permission(self, request, obj=None): # 삭제 권한
        return True

    def has_change_permission(self, request, obj=None): # 수정 권한
        return True


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Hobbies)
admin.site.register(Comment)