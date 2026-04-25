from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from .forms import LoginForm, RegistForm


def account_regist(request):
    """Yangi foydalanuvchi ro'yxatdan o'tishi."""
    if request.user.is_authenticated:
        return redirect('main:index')

    form = RegistForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        messages.success(request, _("Ro'yhatdan muvaffaqiyatli o'tdingiz"))
        return redirect('main:index')

    return render(request, 'account/regist.html', {'form': form})


def account_login(request):
    """Tizimga kirish."""
    if request.user.is_authenticated:
        return redirect('main:index')

    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, _(f"Xush kelibsiz, {user.username}!"))
                return redirect('quiz:index' if user.is_staff else 'main:index')

            # Login xatosi — modal ochish uchun sessiyaga yozamiz
            request.session['login_error'] = form.cleaned_data.get('username', '')
            return redirect('main:index')

    return render(request, 'account/login.html', {'form': form})


@require_POST
def account_logout(request):
    """Tizimdan chiqish — faqat POST so'rovi bilan (CSRF himoyali)."""
    logout(request)
    messages.success(request, _("Xayr! Yana kelib turing."))
    return redirect('main:index')