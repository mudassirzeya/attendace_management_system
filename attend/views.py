from django.shortcuts import render, redirect
from .forms import CompanyForm, RegisterForm, InternalUserForm, AttendanceForm
from .password import PasswordSet
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import UserProfile, Attendance
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def registration(request):
    form1 = CompanyForm()
    form2 = RegisterForm()
    if request.method == 'POST':
        form2 = RegisterForm(request.POST)
        # print("form2: ", form2)
        form1 = CompanyForm(request.POST)
        # print("form1: ", form1)
        username = form2.cleaned_data.get('username')
        try:
            exist_user = User.objects.get(username=username)
        except Exception:
            exist_user = None
        if exist_user is None:
            # print("username: ", username)
            if form2.is_valid():
                # print("form2 valid")
                newuser_obj = form2.save()
                if form1.is_valid():
                    # print("form1 valid")
                    company_obj = form1.save(commit=False)
                    company_obj.super_user = newuser_obj
                    company_obj.save()
                    new_userprofile = UserProfile.objects.create(
                        user=newuser_obj,
                        company=company_obj
                    )
                    new_userprofile.user.first_name = new_userprofile.company.company_name
                    new_userprofile.user.save()
                    return redirect('login')
            else:
                print("form2 not valid")
        else:
            messages.error(request, 'Username already exists')

    context = {"form1": form1, "form2": form2}
    return render(request, 'register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            userProfile = UserProfile.objects.get(user=request.user)
            company_name = userProfile.company
            superuser = company_name.super_user

            print("request.user: ", request.user)
            print("superuser:", superuser)
            if request.user == superuser:
                print("admin page")
                return redirect('superuser')
            else:
                print("user page")
                return redirect('user')
        else:
            messages.info(request, 'Username or Password is in correct')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def adminpage(request):
    form = InternalUserForm()
    try:
        userProfile = UserProfile.objects.select_related(
            'company').get(user=request.user)
    except UserProfile.DoesNotExist:
        return JsonResponse({"msg": "You don't have access to the page"}, status=403)

    mycompany = userProfile.company
    companyAdmin = mycompany.super_user

    if companyAdmin != request.user:
        return JsonResponse({"msg": "You don't have access to the page"}, status=403)

    myuser = UserProfile.objects.filter(
        company=mycompany).exclude(user=companyAdmin)
    total = myuser.count()

    context = {"form": form, "myuser": myuser, "total": total}
    return render(request, 'admin.html', context)


@login_required(login_url='login')
def userpage(request):
    form = AttendanceForm()
    attend = Attendance.objects.filter(
        user=request.user
    )
    context = {"attend": attend, "form": form}
    return render(request, 'user.html', context)


@login_required(login_url='login')
def adduser(request):
    user = request.user
    userProfile = UserProfile.objects.get(user=user)
    company_name = userProfile.company
    form = InternalUserForm()
    if request.method == 'POST':
        form = InternalUserForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            try:
                exist_user = User.objects.get(username=email)
            except Exception:
                exist_user = None
            if exist_user is None:
                print("email: ", email)
                passcode = PasswordSet()
                print("password: ", passcode)
                newuser = form.save(commit=False)
                newuser.set_password(passcode)
                newuser.username = email
                newuser.save()
                UserProfile.objects.create(
                    user=newuser,
                    company=company_name,
                )
                subject = f'welcome to {company_name}'
                message = f'Hi {newuser.first_name}, you have successfully registered in our company. your Username is {newuser.username} & your Password is {passcode}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [newuser.email, ]
                send_mail(subject, message, email_from, recipient_list)
                messages.info(request, "User Added Successfully")
            else:
                messages.info(request, "User Already Exist")
            return redirect('superuser')

    context = {"form": form}
    return render(request, 'admin.html', context)


@login_required(login_url='login')
def userattendence(request):
    form = AttendanceForm()
    if request.method == 'POST':
        img = request.POST.get('image')
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        print("lat ", lat)
        print("lon ", lon)
        Attendance.objects.create(
            user=request.user,
            attendance='Present',
            image=img,
            latitude=lat,
            longitude=lon,
        )
        return redirect('user')
    context = {"form": form}
    return render(request, 'user.html', context)


@login_required(login_url='login')
def alluserattendence(request):
    mycompany = UserProfile.objects.get(user=request.user).company
    myuser = UserProfile.objects.filter(
        company=mycompany
    )

    all_attend = []

    for my in myuser:
        # print('all', my)
        attendance = Attendance.objects.filter(user=my.user)
        all_attend.append(attendance)

    context = {"alluser": all_attend}
    return render(request, 'users_attendance.html', context)
