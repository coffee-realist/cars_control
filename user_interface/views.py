from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user_interface.forms import RegistrationForm

from django.contrib.auth import logout
from django.shortcuts import redirect, reverse
from cars.models import Car
from cars.forms import CarForm, CommentForm

from django.contrib.auth import views as auth_views


class CustomLoginView(auth_views.LoginView):
    """
    Переопределяет поведение стандартного представления для входа.
    Перед входом разлогинивает пользователя, если он уже авторизован.
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)  # Разлогиниваем пользователя
        return super().get(request, *args, **kwargs)


def home(request):
    """
    Главная страница, отображающая список всех машин.
    - GET: показывает список машин.
    - POST: добавляет комментарий к выбранной машине.
    """
    cars = Car.objects.all()  # Получаем все машины
    selected_car = None  # Выбранная машина
    comments = None  # Комментарии к выбранной машине
    comment_form = CommentForm()  # Форма для добавления комментария

    if 'pk' in request.GET:  # Проверяем, есть ли выбранная машина
        selected_car = get_object_or_404(Car, id=request.GET['pk'])
        comments = selected_car.comments.all()

    if request.method == 'POST' and selected_car and request.user.is_authenticated:
        # Обработка добавления нового комментария
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = selected_car
            comment.author = request.user
            comment.save()
            return redirect(f'/?pk={selected_car.id}')  # Перенаправление на ту же страницу

    return render(request, 'pages/home.html', {
        'cars': cars,
        'selected_car': selected_car,
        'comments': comments,
        'comment_form': comment_form,
    })


def custom_logout(request):
    """
    Логаут и перенаправление на страницу входа.
    """
    logout(request)
    return redirect(reverse('login'))


def register(request):
    """
    Регистрация нового пользователя.
    - GET: отображает форму регистрации.
    - POST: сохраняет нового пользователя.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request, pk=None):
    """
    Профиль пользователя:
    - Просмотр всех машин, принадлежащих пользователю.
    - Добавление или редактирование машины.
    """
    user_cars = Car.objects.filter(owner=request.user)  # Машины текущего пользователя
    if pk:
        car = get_object_or_404(Car, id=pk, owner=request.user)
        form = CarForm(instance=car)  # Форма для редактирования машины
    else:
        car = None
        form = CarForm()  # Форма для добавления новой машины

    if request.method == 'POST':
        # Обработка добавления или редактирования машины
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
