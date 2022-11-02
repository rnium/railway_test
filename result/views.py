from django.shortcuts import render, get_object_or_404
from .models import Result

def homepage(request):
    return render(request, 'result/index.html')

def result_indiv(request):
    pk = request.GET.get('roll')
    if not pk:
        return render(request, 'result/result.html', context={'error': 'please enter roll'})
    if len(str(pk)) != 7 or not str(pk).isdigit():
        return render(request, 'result/result.html', context={'error': 'invalid roll'})
    try:
        result = Result.objects.get(roll=pk)
    except Result.DoesNotExist:
        return render(request, 'result/result.html', context={'error': 'result not found'})
    return render(request, 'result/result.html', context={'result': result})
