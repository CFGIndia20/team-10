from django.shortcuts import render
from .models import Status

# Create your views here.

def feed(request):
    stat = Status.objects.all()[:1].get()
    return render(request, 'feedback.html', {'stats': stat})

def res(request):
    #API.send_direct_message(recipient_id, text[, quick_reply_type])
    desc = request.POST.get('desc', False)
    loct = request.POST.get('loct', False)
    return render(request, 'result.html')