from django.utils.translation import gettext_lazy as _

from account.forms import LoginForm
from quiz.models import Sinf


def login_modal(request):
    """
    Har bir so'rovga LOGIN_FORM va sinflar context o'zgaruvchilarini qo'shadi.
    """
    form_class = LoginForm
    context = {
        'sinflar': Sinf.objects.all(),
    }

    if request.session.get('login_error'):
        username = request.session.pop('login_error')
        form = form_class(initial={'username': username})
        form.errors['__all__'] = form.error_class(
            [_("Foydalanuvchi nomi va/yoki parol noto'g'ri")]
        )
        context['LOGIN_FORM'] = form
    else:
        context['LOGIN_FORM'] = form_class()

    return context
