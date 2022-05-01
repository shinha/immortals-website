from django.shortcuts import redirect, render
from .forms import ApplicationForm, MemberEntryForm
from .models import Application

# Create your views here.
def index(request):
    return render(request, 'website/index.html', context={})

def apply(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        print('posted')
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('thankyou')
    context = {'form': form}
    return render(request, 'website/apply.html', context)

def memberentry(request):
    form = MemberEntryForm()
    if request.method == "POST":
        form = MemberEntryForm(request.POST)
        print('posted')
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('thankyou')
    context = {'form': form}
    return render(request, 'website/member-entry.html', context)
    
def thankyou(request):
    return render(request, 'website/thank-you.html', context={})
