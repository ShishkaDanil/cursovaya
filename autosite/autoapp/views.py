from django.shortcuts import render
from .models import RentalAgreement
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Car
from django.views.generic import FormView
from .forms import CarForm

class AddCarView(FormView):
    template_name = 'buhgalter.html'
    form_class = CarForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_required
def agreements_list(request):
    surname_filter = request.GET.get('surname_filter', '')
    if surname_filter:
        agreements = RentalAgreement.objects.filter(surname__icontains=surname_filter).select_related('car', 'car__class_type')
    else:
        agreements = RentalAgreement.objects.all().select_related('car', 'car__class_type')
        
    context = {'agreements': agreements, 'surname_filter': surname_filter}
    return render(request, 'manager.html', context)

def home(request):
    error_message = None
    form = AuthenticationForm()
    role = None # объявляем переменную и устанавливаем её значение в None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = request.POST['role']

            try:
                user = User.objects.get(username=username)
                if user.check_password(password) and user.groups.filter(name=role).exists():
                    login(request, user)
                    if role in ['Менеджер', 'manager']:
                        return redirect('manager')
                    elif role in ['Бухгалтер', 'buhgalter']:
                        return redirect('buhgalter')
                    else:
                        error_message = 'Данный пользователь не имеет доступа к системе {0}'.format(role)
                else:
                    error_message = 'Неправильный логин или пароль.'
            except User.DoesNotExist:
                error_message = 'Неправильный логин или пароль.'



    return render(request, 'base.html', {'error_message': error_message, 'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def buhgalter(request):
    agreements = RentalAgreement.objects.all().select_related('car', 'car__class_type')
    context = {'agreements': agreements}
    return render(request, 'buhgalter.html', context)
