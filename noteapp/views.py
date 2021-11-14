from django.shortcuts import redirect, render

from noteapp.models import Note

# Create your views here.
def home(request):
    notes = Note.objects.all()[0:3]
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
    note = Note.objects.get(id = note_id)
    note.delete()
    return redirect('home')
def edit(request,note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'GET':
        return render(request, 'edit.html', context={'note':note})
    else:
        title = request.POST['title']
        description = request.POST['description']
        note.title = title
        note.description = description
        note.save()
        return redirect('home')
def all_notes(request):
    notes = Note.objects.all()
    return render(request, 'all_notes.html', context={'notes': notes})
    
    
    
    
