from django import forms
from django.core import validators

from front.models import Article


# 留言帮表单

class MessageBoardForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=8, label='标题',
                            error_messages={
                                "min_length": '标题最小长度不能小于2',
                                "max_length": '最大长度不能超过10'
                            })
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')


class RegisterForm(forms.Form):
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message="手机号码格式不符合")])
    pwd1 = forms.CharField(max_length=8, min_length=3)
    pwd2 = forms.CharField(max_length=8, min_length=3)

    # 自定义验证  clean)字段
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # 从数据库中查找telephone是否存在，如果存在抛出异常
        if telephone == '1888888888':
            raise forms.ValidationError('手机号码已存在')
        else:
            return telephone

    def clean(self):
        # 验证以后数据
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码闭一眼")
        else:
            return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
