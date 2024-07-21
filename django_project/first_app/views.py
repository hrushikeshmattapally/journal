from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hi!")
def hel(request):
    return render(request,"hello/hello.html")

from django.shortcuts import render, redirect
from .models import JournalEntry
from .forms import JournalEntryForm

def journal_list(request):
    entries = JournalEntry.objects.all().order_by('-created_at')
    return render(request, 'journal/journal_list.html', {'entries': entries})

def journal_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal_list')
    else:
        form = JournalEntryForm()
    return render(request, 'journal/journal_create.html', {'form': form})
