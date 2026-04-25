from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from quiz.models import Bitik, Natija, Savol, Sinf
from .models import Carousel


def main_index(request):
    """Bosh sahifa — karusel, iqtiboslar va sinflar ro'yxati."""
    context = {
        'page_title': 'Bosh sahifa',
        'posts': Bitik.objects.all(),
        'carousels': Carousel.objects.filter(is_active=True),
    }
    return render(request, 'main/index.html', context)


def main_about(request):
    """Biz haqimizda sahifasi."""
    return render(request, 'main/about.html', {'page_title': 'Biz haqimizda'})


@login_required
def main_result(request):
    """Foydalanuvchining o'z test natijalari."""
    natija_list = Natija.objects.filter(
        user=request.user
    ).select_related('sinf').order_by('-date')

    context = {
        'page_title': 'Natijalarim',
        'natijalar': natija_list,
    }
    return render(request, 'main/result.html', context)


@login_required
def main_test(request, pk):
    """Sinf uchun test ishlash va natijani saqlash."""
    sinf = get_object_or_404(Sinf, pk=pk)
    savol_list = list(Savol.objects.filter(sinf_id=pk))

    if request.method == 'POST':
        tjavob = sum(
            1 for savol in savol_list
            if request.POST.get(str(savol.id)) == savol.tjavob
        )
        jamisavol = len(savol_list)
        njavob = jamisavol - tjavob

        Natija.objects.create(
            user=request.user,
            sinf=sinf,
            tjavob=tjavob,
            njavob=njavob,
            jamisavol=jamisavol,
        )

        foiz = round(tjavob / jamisavol * 100) if jamisavol > 0 else 0
        context = {
            'page_title': f'{sinf.nom} - Natija',
            'jamisavol': jamisavol,
            'tjavob': tjavob,
            'njavob': njavob,
            'sinf': sinf,
            'foiz': foiz,
            'date': date.today(),
        }
        return render(request, 'main/natija.html', context)

    # GET: bugun bu sinf testini allaqachon ishlagan bo'lsa to'sib qo'yamiz
    bugun_boshlangan = Natija.objects.filter(
        user=request.user,
        sinf=sinf,
        date__date=date.today(),
    ).exists()

    if bugun_boshlangan:
        return render(request, 'main/httpresponse.html', {'sinf': sinf})

    context = {
        'page_title': f'{sinf.nom} - Test',
        'savol': savol_list,
        'pk': pk,
        'sinf': sinf,
    }
    return render(request, 'main/test.html', context)