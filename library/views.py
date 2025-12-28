import datetime
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from library.models import Book,Author
from django.db.models import ForeignKey
from django.contrib import messages


def index(request):
    return render(request,"home.html")


def getBooks(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'book_list': books,
        'authors_list': authors
    }
    return render(request, "book_list.html", context)


def getAuthors(request):
    authors = Author.objects.all()
    return render(request,"authors_list.html",{'authors_list':authors})

def addAuthors(request):
    name= request.POST["nombre"]
    date= request.POST["fecha"]
    errors=[]

    if not name:
        errors.append("El nombre es obligatorio.")

    try:
        birthdate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        errors.append("El formato de la fecha de nacimiento es inválido. Por favor, usa el formato AAAA-MM-DD.")
        birthdate = None

    if errors:
        for e in errors:
            messages.error(request, e)
        return redirect("getAuthors") 


    newAuthor = Author(name=name,birthdate=date)
    newAuthor.save()
    messages.success(request,'Autor Agregado')
    return redirect('getAuthors')


def addBooks(request):
    if request.method == 'POST':
        title = request.POST["title"]
        published = request.POST["date"]
        author_id = request.POST["author"]

        #Validacion de los campos
        errors = []
        if not title:
            errors.append("El nombre es obligatorio.")

        try:
            date = datetime.datetime.strptime(published, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            errors.append("El formato de la fecha de Publicacion es inválido. Por favor, usa el formato AAAA-MM-DD.")
            date = None

    if errors:
        for e in errors:
            messages.error(request, e)
        return redirect("getBooks") 
        
        
        #Convertimos las páginas a un número entero de forma segura
    try:
        page_numbers = int(request.POST["pages"])
    except (ValueError, KeyError):
        page_numbers = None
    try:
        author_obj = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return redirect('some_error_page') 
    
    newBook = Book(
        title=title,
        author=author_obj, 
        published=published,
        page_numbers=page_numbers
        )
    newBook.save()
    messages.success(request,'Libro Agregado')
    return redirect('getBooks')
   

def deleteBook(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        messages.success(request,'Libro Eliminado')
    return redirect('getBooks')

def deleteAuthors(request, authors_id):
    if request.method == 'POST':
        author = get_object_or_404(Author, pk=authors_id)
        author.delete()
        messages.success(request,'Autor Eliminado')
    return redirect('getAuthors')

def detailsAuthors(request, authors_id):
    author = get_object_or_404(Author, pk=authors_id)
    return render(request,"authors_update.html",{'author':author})


def detailsBooks(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    authors = Author.objects.all()
    context = {
        'book': book,
        'author': authors
    }
    return render(request,"books_updates.html",context)

def updateAuthors(request):
    author_id = request.POST.get("id")
    name= request.POST["name"]
    date= request.POST["date"]
    errors = []
    
    if not name:
        errors.append("El nombre es obligatorio.")

    try:
        birthdate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        errors.append("El formato de la fecha de nacimiento es inválido. Por favor, usa el formato AAAA-MM-DD.")
        birthdate = None

    if errors:
        for e in errors:
            messages.error(request, e)
        return redirect("getAuthors")

    Author.objects.filter(pk=author_id).update(birthdate=date,name=name)
    messages.success(request,'Autor Actualizado')
    return redirect('getAuthors')

def updateBooks(request):
    Book_id = request.POST.get("id")
    title = request.POST["title"]
    published = request.POST["published"]
    author_id = int(request.POST["author"])
    pages = request.POST["pages"]
    errors = []
        # Validar campos
    if not title:
        errors.append("El título es obligatorio.")

    try:
        birthdate = datetime.datetime.strptime(published, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        errors.append("El formato de la fecha de Publicacioin es inválido. Por favor, usa el formato AAAA-MM-DD.")
        birthdate = None

    if pages:
        try:
            pages = int(pages)
            if pages <= 0:
                errors.append("El número de páginas debe ser mayor a 0.")
        except ValueError:
            errors.append("Número de páginas inválido.")
    else:
            pages = None  # opcional
    if errors:
        for e in errors:
            messages.error(request, e)
        return redirect("getBooks")  
    

    Book.objects.filter(pk=Book_id).update(title=title,published=published,author_id=author_id,page_numbers=pages)
    messages.success(request,'Libro Actualizado')
    return redirect('getBooks')