from django.shortcuts import render
from .models import KnittingPattern, YarnType, Tutorial


def home(request):
    """Главная страница"""
    patterns = KnittingPattern.objects.all()[:3]  # Последние 3 схемы
    yarns = YarnType.objects.filter(in_stock=True)[:3]  # 3 типа пряжи в наличии
    context = {
        'patterns': patterns,
        'yarns': yarns,
    }
    return render(request, 'knitting/home.html', context)


def patterns(request):
    """Страница со схемами вязания"""
    all_patterns = KnittingPattern.objects.all()
    context = {
        'patterns': all_patterns,
    }
    return render(request, 'knitting/patterns.html', context)


def tutorials(request):
    """Страница с уроками вязания"""
    all_tutorials = Tutorial.objects.all()
    context = {
        'tutorials': all_tutorials,
    }
    return render(request, 'knitting/tutorials.html', context)
