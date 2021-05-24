from django import forms
from Backend.models import Pic


class PicForm(forms.ModelForm):

    class Meta():
        model = Pic
        fields = ('pic',)
        labels = {
            'pic': 'Add photo'
        }