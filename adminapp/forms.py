import pytz
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()



from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
   class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'comments']

def clean_comments(self):
        comments = self.cleaned_data.get('comments')
        if len(comments) > 150:
            raise forms.ValidationError("Comments cannot exceed 150 characters.")
        return comments


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']
