from django import forms
from .models import Task
from .models import AddCourse

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']

from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']