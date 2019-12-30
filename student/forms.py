from django import forms

from .models import Student



"""class StudentForm(forms.Form):
    name=forms.CharFiled(lable='姓名',max_length=128)
    sex=forms.ChoiseField(lable='性别',choices=Student.Sex_ITEMS)
    profession=forms.CharFiled(lable='职业',max_length=128)
    qq=forms.CharFiled(lable='QQ',max_length=128)
    phone=forms.CharFiled(lable='手机',max_length=128)
"""
class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data=self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

        return int(cleaned_data)
    class Meta:
        model=Student
        fields={
            'name','sex','profession',
            'email','qq','phone'
        }