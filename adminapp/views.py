from django.shortcuts import render, redirect, get_object_or_404

from . import models
from .models import Task
from .forms import TaskForm
# Create your views here.
def projecthomepage(request):
    return render(request,'ProjectHomePage.html')

def printpagecall(request):
    return render(request,'adminapp/printer.html')


def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1= {'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')

def randompagecall(request):
    return render(request,'adminapp/randomexample.html')
import random
import string
def randomlogic(request):
    if request.method =="POST":
        number1=int(request.POST['number1'])
        ran="".join(random.sample(string.ascii_uppercase+string.digits,k=number1))
        a1={'ran':ran}
        return render(request,'adminapp/randomexample.html',a1)

def calculatorpagecall(request):
    return render(request,'adminapp/calculator.html')

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def UserLoginPageCall(request):
    return render(request, 'adminapp/loginpage.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                #return render(request, 'studentapp/StudentHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                #return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

def datetimepagecall(request):
    return render(request,'adminapp/datetimepage.html')

import datetime
import calendar
from datetime import timedelta
def datetimepagelogic(request):
    if request.method == 'POST':
        number1= int(request.POST['date1'])
        x = datetime.datetime.now()
        ran=x + timedelta(days=number1)
        ran1 = ran.year
        ran2 = calendar.isleap(ran1)
        if ran2 == False:
            ran3 = "Not leap year"
        else:
            ran3 = "Leap year"
    a1 = {'ran': ran, 'ran3':ran3, 'ran1':ran1, 'number1':number1}
    return render(request,'adminapp/datetimepage.html',a1)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html',
                  {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegisterPage.html')

from .forms import StudentForm
from .models import StudentList

#def add_student(request):
 #       if request.method == 'POST':
  #          form = StudentForm(request.POST)
   #         if form.is_valid():
    #            form.save()
     #           return redirect('student_list')
      #  else:
       #     form = StudentForm()
        #return render(request, 'adminapp/add_student.html', {'form': form})


from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
def add_studentcall(request):
        return render(request, 'adminapp/add_student.html')

def student_list(request):
        students = StudentList.objects.all()
        return render(request, 'adminapp/student_list.html', {'students': students})

def student_listcall(request):
        return render(request, 'adminapp/student_list.html')

from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x-1])

        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per Month')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'adminapp/chart.html', {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })
    return render(request, 'adminapp/chart.html', {'form': UploadFileForm()})




from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'adminapp/confirmation.html')
    else:
        form = FeedbackForm()
    return render(request, 'adminapp/feedback_form.html', {'form': form})





from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Add a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send contact details via email
            recipient_email = request.POST.get('recipient_email')
            if recipient_email:
                send_mail(
                    subject='New Contact Created',
                    message=f'Contact Details:\nName: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\nAddress: {contact.address}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient_email]
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})

# List all contacts with search functionality
from django.shortcuts import render
from .models import Contact

def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(models.Q(name__icontains=query) | models.Q(email__icontains=query))
    else:
        contacts = Contact.objects.all()
    return render(request, 'adminapp/contact_list.html', {'contacts': contacts})


# Delete a contact
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_list')
