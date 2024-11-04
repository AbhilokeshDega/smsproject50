from django.shortcuts import render

def StudentHomePage(request):
    return render(request, 'studentapp/StudentHomePage.html')

from django.shortcuts import render
from django.contrib.auth.models import User
from facultyapp.models import Marks
from adminapp.models import StudentList

def view_marks(request):
    user = request.user

    try:
        student_user = User.objects.get(username=user.username)


        student = StudentList.objects.get(Register_Number=student_user)

        marks = Marks.objects.filter(student=student)

        return render(request, 'studentapp/view_marks.html', {'marks': marks})
    except (StudentList.DoesNotExist, User.DoesNotExist):

        return render(request, 'studentapp/no_studentlist.html',{
            'error': 'No student record found for this user.'
        })