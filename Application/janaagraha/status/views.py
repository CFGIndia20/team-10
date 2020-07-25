from django.shortcuts import render

# Create your views here.

def feed(request):
    status = 0
    return render(request, 'feedback.html', {'stat': status})

def res(request):
    desc = request.POST.get('desc', False)
    loct = request.POST.get('loct', False)
    return render(request, 'result.html')