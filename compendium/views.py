from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Book, Misc, Apparel, ReviewBook, ReviewApparel, ReviewMisc, Cart, BookOrder, MiscOrder, ApparelOrder
from .models import Trick, ReviewTrick, TrickOrder, Act, Review, Item
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request, "base.html")

def hire_us(request, identifier):
    identifier = int(identifier)
    context = {
        'identifier': identifier,
    }
    if identifier == 0:
        context['acts'] = Act.objects.all().filter(stage=True)
        return render(request, "hire_us/stage.html", context)
    elif identifier == 1:
        context['acts'] = Act.objects.all().filter(restaurant=True)
        return render(request, "hire_us/restaurant.html", context)
    elif identifier == 2:
        context['acts'] = Act.objects.all().filter(close_up=True)
        return render(request, "hire_us/close_up.html", context)
    elif identifier == 3:
        return render(request, "hire_us/prices.html", context)

def reviews(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
    }

    if request.user.is_authenticated():
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = Review.objects.create(
                    user=request.user,
                    item=context['item'],
                    text=form.cleaned_data.get('text'),
                )
                new_review.save()

        else:
            if Review.objects.filter(user=request.user, item=context['item']).count() == 0:
                form = ReviewForm()
                context['form'] = form
    context['reviews'] = item.review_set.all()

    return render(request, 'hire_us/reviews.html', context)

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
        'identifier': identifier,
    }
    return render(request, "store/shop.html", context)

def trick_shop(request, sort_identifier):
    tricks = Trick.objects.order_by('publish_date')
    difficulty = []
    i = 0
    for trick in tricks:
        difficulty.append(str(trick.difficulty))
        i += 1
    context = {
        'tricks': tricks,
        'difficulty': difficulty,
    }
    return render(request, "store/tricks_shop.html", context)

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

def trick_details(request, trick_id):
    trick = get_object_or_404(Trick, id=trick_id)
    context = {
        'trick': trick,
    }
    if request.user.is_authenticated():
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = ReviewTrick.objects.create(
                    user=request.user,
                    trick=context['trick'],
                    text=form.cleaned_data.get('text'),
                )
                new_review.save()

        else:
            if ReviewTrick.objects.filter(user=request.user, trick=context['trick']).count() == 0:
                form = ReviewForm()
                context['form'] = form
    context['reviews'] = trick.reviewtrick_set.all()

    return render(request, 'store/trick_detail.html', context)



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
            elif item_classifier == 4:
                item = Trick.objects.get(pk=item_id)
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
            elif item_classifier == 4:
                item = Trick.objects.get(pk=item_id)
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
        trick_orders = TrickOrder.objects.filter(cart=cart)
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
        for order in trick_orders:
            total += (order.item.price * order.quantity)
            count += order.quantity

        context = {
            'book_cart': book_orders,
            'misc_cart': misc_orders,
            'apparel_cart': apparel_orders,
            'trick_cart': trick_orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')
