from django.forms import ModelForm
from .models import tryform

class tryformform(ModelForm):
    class Meta:
        model = tryform
        fields = '__all__'
