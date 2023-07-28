from django.shortcuts import render, redirect

from .models import Video
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    videos = Video.objects.all()
    return render(request, 'videos/home.html', context={'videos': videos})

def members(request):
    all_members = Member.objects.all()
    return render(request, 'videos/members.html', context={'all': all_members})

def join(request):

    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
         form.save()
        else:
            messages.success(request, ('there was an error in your form'))
            return redirect('join')

        messages.success(request, ('SUCCESS'))
        return redirect( 'members')
    else:
        return render(request, 'videos/join.html', {})