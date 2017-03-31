from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Book, Misc, Apparel, ReviewBook, ReviewApparel, ReviewMisc, Cart, BookOrder, MiscOrder, ApparelOrder
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



def add_to_cart(request, item_id, item_classifier):
    item_classifier = int(item_classifier)
    if request.user.is_authenticated():
        try:
            if item_classifier == 1:
                item = Book.objects.get(pk=item_id)
            elif item_classifier == 2:
                item = Misc.objects.get(pk=item_id)
            elif item_classifier == 3:
                item = Apparel.objects.get(pk=item_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user=request.user
                )
                cart.save()
            cart.add_to_cart(item_id, item_classifier)
        return redirect('cart')
    else:
        return redirect('index')


def remove_from_cart(request, item_id, item_classifier):
    item_classifier = int(item_classifier)
    if request.user.is_authenticated():
        try:
            if item_classifier == 1:
                item = Book.objects.get(pk=item_id)
            elif item_classifier == 2:
                item = Misc.objects.get(pk=item_id)
            elif item_classifier == 3:
                item = Apparel.objects.get(pk=item_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(item_id, item_classifier)
        return redirect('cart')
    else:
        return redirect('index')


def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user.id, active=True)
        book_orders = BookOrder.objects.filter(cart=cart)
        misc_orders = MiscOrder.objects.filter(cart=cart)
        apparel_orders = ApparelOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in book_orders:
            total += (order.item.price * order.quantity)
            count += order.quantity
        for order in misc_orders:
            total += (order.item.price * order.quantity)
            count += order.quantity
        for order in apparel_orders:
            total += (order.item.price * order.quantity)
            count += order.quantity

        context = {
            'book_cart': book_orders,
            'misc_cart': misc_orders,
            'apparel_cart': apparel_orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')
