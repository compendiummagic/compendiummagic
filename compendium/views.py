from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Book, Misc, Apparel, ReviewBook, ReviewApparel, ReviewMisc
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request, "base.html")

def shop(request, identifier):
    books = Book.objects.order_by('author')
    miscs = Misc.objects.order_by('title')
    clothes = Apparel.objects.order_by('title')

    identifier = int(identifier)

    if identifier == 1:
        miscs = []
        clothes = []
    elif identifier == 2:
        books = []
        clothes = []
    elif identifier == 3:
        miscs = []
        books =[]
    else:
        pass
    context = {
        'books': books,
        'miscs': miscs,
        'clothes': clothes,
    }
    return render(request, "store/shop.html", context)

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book,
    }

    if request.user.is_authenticated():
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = ReviewBook.objects.create(
                    user=request.user,
                    book=context['book'],
                    text=form.cleaned_data.get('text'),
                )
                new_review.save()

        else:
            if ReviewBook.objects.filter(user=request.user, book=context['book']).count() == 0:
                form = ReviewForm()
                context['form'] = form
    context['reviews'] = book.reviewbook_set.all()

    return render(request, 'store/detail.html', context)

def misc_details(request, misc_id):
    misc = get_object_or_404(Misc, id=misc_id)
    context = {
        'misc': misc,
    }
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = ReviewMisc.objects.create(
                    user=request.user,
                    misc=context['misc'],
                    text=form.cleaned_data.get('text'),
                )
                new_review.save()

        else:
            if ReviewMisc.objects.filter(user=request.user, misc=context['misc']).count() == 0:
                form = ReviewForm()
                context['form'] = form
    context['reviews'] = misc.reviewmisc_set.all()

    return render(request, 'store/misc_detail.html', context)

def apparel_details(request, apparel_id):
    cloth = get_object_or_404(Apparel, id=apparel_id)
    context = {
        'cloth': cloth,
    }
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = ReviewApparel.objects.create(
                    user=request.user,
                    apparel=context['cloth'],
                    text=form.cleaned_data.get('text'),
                )
                new_review.save()

        else:
            if ReviewApparel.objects.filter(user=request.user, apparel=context['cloth']).count() == 0:
                form = ReviewForm()
                context['form'] = form
    context['reviews'] = cloth.reviewapparel_set.all()

    return render(request, 'store/apparel_detail.html', context)