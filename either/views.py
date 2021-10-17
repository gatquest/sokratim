from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Favorite
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin




def home(request):
    return render(request, 'either/home.html', {'title' : "Сокра.тим"})


def about(request):
    return render(request, 'either/about.html', {'title' : "О нас"})



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'either/registration.html',
        {
            'title': 'Cтраница регистрации',
            'form': form
        }
    )

@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if updateUserForm.is_valid():
            updateUserForm.save()
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm,
    }
    return render(request, 'either/profile.html', data)


class ShowFavoriteView(ListView):
    model = Favorite
    template_name = 'either/favorites.html'
    context_object_name = 'favs'

    def  get_queryset(self):
        user_name = get_object_or_404(User, username=self.request.user)
        return Favorite.objects.filter(avtor=user_name).order_by('short_name')


class CreateFavoriteView(LoginRequiredMixin, CreateView):
    model = Favorite
    template_name = 'either/favorites.html'
    fields =[
        'link_name',
        'short_name'
    ]

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user_name = get_object_or_404(User, username=self.request.user)
        favs = Favorite.objects.filter(avtor=user_name).order_by('short_name')
        context['favs'] = favs
        return context
