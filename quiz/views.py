from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import BitikForm, SavolForm
from .models import Bitik, Natija, Savol, Sinf


def _get_sinflar():
    """Barcha sinflarni qaytaruvchi yordamchi funksiya."""
    return Sinf.objects.all()


@staff_member_required
def quiz_index(request, pk=None):
    """Natijalar ro'yxati (admin uchun)."""
    natija_list = Natija.objects.select_related('user', 'sinf').order_by('-tjavob')
    if pk is not None:
        natija_list = natija_list.filter(sinf_id=pk)

    return render(request, 'quiz/index.html', {
        'natijalar': natija_list,
        'sinflar': _get_sinflar(),
    })


@staff_member_required
def quiz_savollar(request, pk=None):
    """Savollar ro'yxati (admin uchun)."""
    savol_list = Savol.objects.select_related('sinf')
    if pk is not None:
        savol_list = savol_list.filter(sinf_id=pk)

    return render(request, 'quiz/savollar.html', {
        'savollar': savol_list,
        'bitiklar': Bitik.objects.all(),
        'sinflar': _get_sinflar(),
    })


@staff_member_required
def quiz_savol_add(request):
    """Yangi savol qo'shish (admin uchun)."""
    form = SavolForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Savol muvaffaqqiyatli qo'shildi")
        return redirect('quiz:index')

    return render(request, 'quiz/savol_add.html', {'form': form})


@staff_member_required
def quiz_bitik_add(request):
    """Yangi iqtibos qo'shish (admin uchun)."""
    form = BitikForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Iqtibos muvaffaqqiyatli qo'shildi")
        return redirect('quiz:index')

    return render(request, 'quiz/bitik_add.html', {'form': form})


@staff_member_required
def quiz_savol_view(request, pk):
    """Savol tafsilotlari (admin uchun)."""
    savol = get_object_or_404(Savol, pk=pk)
    return render(request, 'quiz/savol_view.html', {'savol': savol})


@staff_member_required
@require_POST
def quiz_savol_delete(request, pk):
    """Savolni o'chirish — faqat POST so'rovi bilan (CSRF himoyali)."""
    get_object_or_404(Savol, pk=pk).delete()
    messages.success(request, "Savol o'chirildi")
    return redirect('quiz:savollar')


@staff_member_required
@require_POST
def quiz_bitik_delete(request, pk):
    """Iqtibosni o'chirish — faqat POST so'rovi bilan (CSRF himoyali)."""
    get_object_or_404(Bitik, pk=pk).delete()
    messages.success(request, "Iqtibos o'chirildi")
    return redirect('quiz:savollar')
