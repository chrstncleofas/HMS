from app.models import Booking
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from app.serializers import BookingSerializer
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

DASHBOARDS_URL_PATH = 'app/dashboard.html'
REGISTER_URL_PATH = 'app/register.html'
HOME_URL_PATH = 'app/base.html'

# For API Frontend Side
@csrf_exempt
def reservationApi(request, id=0) -> (JsonResponse | None):
    # Fetch all Data API
    if request.method=='GET':
        bookings = Booking.objects.all()
        booking_serializer=BookingSerializer(bookings, many=True)
        return JsonResponse(booking_serializer.data, safe=False)
    # Create or Add API
    elif request.method=='POST':
        booking_data=JSONParser().parse(request)
        booking_serializer=BookingSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    # Update API
    elif request.method=='PUT':
        booking_data=JSONParser().parse(request)
        booking=Booking.objects.get(id=booking_data['id'])
        bookings_serializer=BookingSerializer(booking, data=booking_data)
        if bookings_serializer.is_valid():
            bookings_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    # Delete API
    elif request.method=='DELETE':
        booking=Booking.objects.get(id=id)
        booking.delete()
        return JsonResponse("Deleted Successfully", safe=False)

# For our Backend U.I for List of Booking
def home(request) -> HttpResponse:
    return render(request, HOME_URL_PATH)

def login_page(request) -> (HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse):
    if request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        fname = "User"

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect(dashboard)
        else:
            messages.error(
                request,
                "Incorrect username or password, please check your credentials and try again",
                extra_tags='loginError'
            )
            return redirect(login_page)
        
    return render(request, HOME_URL_PATH)

def logout_view(request) -> HttpResponseRedirect:
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect(home)

def register(request) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('signup-username')
        email = request.POST.get('signup-email')
        password = request.POST.get('signup-password')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        context = {
            'registration_successful': True,
        }

        return render(request, REGISTER_URL_PATH, context)

    return render(request, REGISTER_URL_PATH)

def dashboard(request) -> HttpResponse:
    first_name = request.user.first_name
    last_name = request.user.last_name
    total_bookings = Booking.objects.count()
    bookings = Booking.objects.all()
    total_users = User.objects.count()
    recently_logged_in_users = User.objects.filter(last_login__isnull=False).order_by('-last_login')[:5]
    return render(
        request,
        DASHBOARDS_URL_PATH, 
        {
            'first_name': first_name, 
            'last_name': last_name,
            'recently_logged_in_users': recently_logged_in_users,
            'total_bookings': total_bookings,
            'total_users': total_users,
            'booking': bookings,
            'listAllUsers': User.objects.all(),
        }
    )

def allList(request) -> HttpResponse:
    return render(request, 'app/list.html', {
        'booking' : Booking.objects.all(),
    })

def view_info(request, id) -> HttpResponseRedirect:
    if request.method == 'GET':
        Booking.objects.get(pk=id)
    return HttpResponseRedirect(reverse('allList'))

def delete_list(request, id) -> HttpResponseRedirect:
    if request.method == 'POST':
        booking = Booking.objects.get(pk=id)
        booking.delete()
    return HttpResponseRedirect(reverse('allList'))

# This functions for Users
def edit_user_details(request, id) -> (HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            return redirect(allUser)

        elif password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)
            return redirect(allUser)

    else:
        form = CustomUserChangeForm(instance=user)
        password_form = PasswordChangeForm(request.user)

    return render(
        request,
        'app/edit.html',
        {
            'form': form,
            'password_form': password_form,
            'user': user,
        }
    )

def allUser(request) -> HttpResponse:
    return render(request, 'app/users.html', {
        'listAllUsers' : User.objects.all(),
    })

def view_user_info(request, id) -> HttpResponseRedirect:
    if request.method == 'GET':
        User.objects.get(pk=id)
    return HttpResponseRedirect(reverse(allUser))

def delete_users(request, id) -> HttpResponseRedirect:
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        user.delete()
    return HttpResponseRedirect(reverse(allUser))

def createSuperUser(request) -> (HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(allUser)
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'app/createSuperUser.html', {'form': form})
