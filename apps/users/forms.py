from django import forms
from captcha.fields import CaptchaField
from users.models import *

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})
    
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    '''用户更改图像'''
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    '''个人中心信息修改'''
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender','birthday','address','mobile']