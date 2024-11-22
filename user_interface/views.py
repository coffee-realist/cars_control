from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user_interface.forms import RegistrationForm

from django.contrib.auth import logout
from django.shortcuts import redirect, reverse
from cars.models import Car
from cars.forms import CarForm, CommentForm

from django.contrib.auth import views as auth_views


class CustomLoginView(auth_views.LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)  # Разлогиниваем пользователя
        return super().get(request, *args, **kwargs)


def home(request):
    cars = Car.objects.all()
    selected_car = None
    comments = None
    comment_form = CommentForm()

    if 'pk' in request.GET:  # Заменяем car_id на pk
        selected_car = get_object_or_404(Car, id=request.GET['pk'])  # Заменяем car_id на pk
        comments = selected_car.comments.all()

    if request.method == 'POST' and selected_car and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = selected_car
            comment.author = request.user
            comment.save()
            return redirect(f'/?pk={selected_car.id}')  # Заменяем car_id на pk

    return render(request, 'pages/home.html', {
        'cars': cars,
        'selected_car': selected_car,
        'comments': comments,
        'comment_form': comment_form,
    })


def custom_logout(request):
    logout(request)
    return redirect(reverse('login'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request, pk=None):  # Используем pk вместо car_id
    user_cars = Car.objects.filter(owner=request.user)
    if pk:
        car = get_object_or_404(Car, id=pk, owner=request.user)  # Заменяем car_id на pk
        form = CarForm(instance=car)
    else:
        car = None
        form = CarForm()

    if request.method == 'POST':
        if pk:
            form = CarForm(request.POST, instance=car)
        else:
            form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('profile')

    return render(request, 'pages/profile.html', {
        'cars': user_cars,
        'form': form,
        'editing_car': car,
    })
