from django.forms import ModelForm
from .models import Room,tryform
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class tryform(ModelForm):
    class Meta:
        model = tryform
        fields = '__all__'
        
        