from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from apps.users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
from users.views import LogoutView
from django.views.static import serve
from bwOnline.settings import MEDIA_ROOT
from bwOnline.settings import STATIC_ROOT
from django.views import static
import xadmin
from apps.users.views import pag_not_found,page_error

urlpatterns = [
    path('captcha/',include('captcha.urls')),
    path('xadmin/',xadmin.site.urls),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name='register'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path("org/", include('organization.urls', namespace="org")),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    path("course/", include('course.urls', namespace="course")),
    #个人信息
    path("users/", include('users.urls', namespace="users")),
    #静态文件
    re_path(r'^static/(?P<path>.*)', static.serve, {"document_root": STATIC_ROOT },name='static'),
    # 富文本编辑器url
    path('ueditor/',include('DjangoUeditor.urls' )),
]


# 全局404页面配置
handler404 = 'users.views.pag_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'