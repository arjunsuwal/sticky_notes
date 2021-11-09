from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from noteapp.models import Note

# Create your views here.
def home(request):
    notes = Note.objects.all()
    return render(request, 'index.html', context={'notes':notes})
def add_notes(request):
    if request.method =='GET':
        return render(request , 'add.html')
    else:
        title = request.POST['title']
        description = request.POST['description']
        note = Note.objects.create(title=title, description=description)
        note.save()
        return redirect('home')
def delete(request,note_id):
    return HttpResponse('this is delete page')
def edit(request,note_id):
    return HttpResponse('this is edit page')
