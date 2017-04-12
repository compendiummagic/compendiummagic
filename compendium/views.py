from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils import timezone

import stripe, paypalrestsdk

from compendiummagic import settings
from .models import Book, Misc, Apparel, ReviewBook, ReviewApparel, ReviewMisc, Cart, BookOrder, MiscOrder, ApparelOrder
from .models import Trick, ReviewTrick, TrickOrder, Act, Review, Item, ShippingInfo
from .forms import ReviewForm, ContactForm, ShippingForm

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

def contact_us(request):

    context= {
        'registered':request.user.is_authenticated,
        'complete': False,
    }
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ContactForm(request.POST)

            if form.is_valid():
                subject = 'Compendium Magic Enquiry'
                from_email = settings.BOOKING_FROM_EMAIL
                to_email_customer = [request.user.email]
                to_email_compendium = [settings.BOOKING_FROM_EMAIL]

                email_context = Context ({
                    'name': request.user.username,
                    'phone':form.cleaned_data.get('phone'),
                    'email': request.user.email,
                    'date':form.cleaned_data.get('date'),
                    'time':form.cleaned_data.get('time'),
                    'venue':form.cleaned_data.get('venue'),
                    'guests':form.cleaned_data.get('guests'),
                    'extra_info':form.cleaned_data.get('extra_info'),
                    'hear':form.cleaned_data.get('hear'),
                })


                text_email = render_to_string('email/contact_request_email.txt', email_context)
                html_email = render_to_string('email/contact_request_email.html', email_context)

                msg = EmailMultiAlternatives(subject, text_email, from_email, to_email_customer)
                msg.attach_alternative(html_email, 'text/html')
                msg.content_subtype = 'html'
                msg.send()

                subject = 'Job Request: '+str(request.user.username)

                text_email = render_to_string('email/job_enquiry_email.txt', email_context)
                html_email = render_to_string('email/job_enquiry_email.html', email_context)

                msg = EmailMultiAlternatives(subject, text_email, from_email, to_email_compendium)
                msg.attach_alternative(html_email, 'text/html')
                msg.content_subtype = 'html'
                msg.send()

                context['complete'] = True
            else:
                context['form'] = form
        else:
            form = ContactForm()
            context['form'] = form

    return render(request, 'contact_us/contact_us.html', context)


def checkout(request, processor):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user.id, active=True)
        book_orders = BookOrder.objects.filter(cart=cart)
        misc_orders = MiscOrder.objects.filter(cart=cart)
        apparel_orders = ApparelOrder.objects.filter(cart=cart)
        trick_orders = TrickOrder.objects.filter(cart=cart)
        if processor == "paypal":
            redirect_url = checkout_paypal(request, cart, book_orders, misc_orders, apparel_orders, trick_orders)
            return redirect(redirect_url)
        elif processor == "stripe":
            all_requests = request.POST

            token = request.POST['stripeToken']#str(all_requests.get('stripeToken', "0"))

            f = open('store.txt', 'w')
            f.write(str(token))
            f.close()

            f = open('all_requests.txt', 'w')
            f.write(str(all_requests))
            f.close()

            status = checkout_stripe(cart, book_orders, misc_orders, apparel_orders, trick_orders, token)
            if status:
                return redirect(reverse('process_order', args=['stripe']))
            else:
                return redirect('order_error', context={"message": "There was a problem processing your payment."})
    else:
        return redirect('index')


def checkout_paypal(request, cart, book_orders, misc_orders, apparel_orders, trick_orders):
    if request.user.is_authenticated():
        items = []
        total = 0
        orders = [book_orders, misc_orders, apparel_orders, trick_orders]
        for i in orders:
            for order in i:
                total += (order.item.price * order.quantity)
                item = order.item
                current_item = {
                    'name': item.title,
                    'sku': item.id,
                    'price': str(item.price),
                    'currency': 'GBP',
                    'quantity': order.quantity
                }
                items.append(current_item)

        paypalrestsdk.configure({
            "mode": "sandbox",
            "client_id": "INSERT_ID_HERE",
            "client_secret": "INSERT_SECRET_KEY_HERE"
        })

        payment = paypalrestsdk.Payment({
            "intent": 'sale',
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:8000/store/process/paypal",
                "cancel_url": "http://localhost:8000/store"},
            "transactions": [{
                "item_list": {
                    "items": items},
                "amount": {
                    "total": str(total),
                    "currency": 'GBP'},
                "description": "Compendium Magic Order"}]})
        if payment.create():
            cart_instance = cart.get()
            cart_instance.payment_id = payment.id
            cart_instance.save()
            for link in payment.links:
                if link.method == "REDIRECT":
                    redirect_url = str(link.href)
                    return redirect_url
        else:
            return reverse('order_error')
    else:
        return redirect('index')


def checkout_stripe(cart, book_orders, misc_orders, apparel_orders, trick_orders, token):
    stripe.api_key =  settings.STRIPE_API_KEY
    total = 0
    orders_list = [book_orders, misc_orders, apparel_orders, trick_orders]
    for orders in orders_list:
        for order in orders:
            total += (order.item.price * order.quantity)
    status = True
    try:
        charge = stripe.Charge.create(
            amount=int(total * 100),
            currency="GBP",
            source=token,
        )
        cart_instance = cart.get()
        cart_instance.payment_id = charge.id
        cart_instance.save()
    except stripe.error.CardError, e:
        status = False
    return status

def order_error(request):
    if request.user.is_authenticated():
        return render(request, 'store/order_error.html')
    else:
        return redirect('index')


def process_order(request, processor):
    if request.user.is_authenticated():
        if processor == "paypal":
            payment_id = request.GET.get('paymentId')
            cart = Cart.objects.filter(payment_id=payment_id)
            book_orders = BookOrder.objects.filter(cart=cart)
            misc_orders = MiscOrder.objects.filter(cart=cart)
            apparel_orders = ApparelOrder.objects.filter(cart=cart)
            trick_orders = TrickOrder.objects.filter(cart=cart)
            total = 0
            for order in book_orders:
                total += (order.item.price * order.quantity)
            for order in misc_orders:
                total += (order.item.price * order.quantity)
            for order in apparel_orders:
                total += (order.item.price * order.quantity)
            for order in trick_orders:
                total += (order.item.price * order.quantity)
            context = {
                'book_cart': book_orders,
                'misc_cart': misc_orders,
                'trick_cart': trick_orders,
                'apparel_cart': apparel_orders,
                'total': total,
            }
            return render(request, 'store/process_order.html', context)
        elif processor == "stripe":
            return redirect('complete_order', 'stripe')
    else:
        return redirect('index')


def complete_order(request, processor):

    if request.user.is_authenticated():

        cart1 = Cart.objects.get(user=request.user.id, active=True)

        cart = Cart.objects.filter(user=request.user.id, active=True)

        book_orders = BookOrder.objects.filter(cart=cart)
        misc_orders = MiscOrder.objects.filter(cart=cart)
        apparel_orders = ApparelOrder.objects.filter(cart=cart)
        trick_orders = TrickOrder.objects.filter(cart=cart)
        total = 0

        for order in book_orders:
            total += (order.item.price * order.quantity)
        for order in misc_orders:
            total += (order.item.price * order.quantity)
        for order in apparel_orders:
            total += (order.item.price * order.quantity)
        for order in trick_orders:
            total += (order.item.price * order.quantity)

        context = {
            'book_cart': book_orders,
            'misc_cart': misc_orders,
            'trick_cart': trick_orders,
            'apparel_cart': apparel_orders,
            'total': total,
        }

        time_now = timezone.now()

        if processor == 'paypal':
            payment = paypalrestsdk.Payment.find(cart1.payment_id)
            if payment.execute({'payer_id': payment.payer.payer_info.payer_id}):
                message = "Success! Your payment has been completed, and is being processed. Payment ID: %s" % (payment.id)
                cart1.active = False
                cart1.order_date = time_now
                cart1.payment_type="Paypal"
                cart1.save()
            else:
                message = "There was a problem with the transaction. Error: %s" % (payment.error.message)

        elif processor == 'stripe':
            cart1.active = False
            cart1.order_date = time_now
            cart1.payment_type = "Stripe"
            cart1.save()
            message = "Success! Your payment has been completed, and is being processed. Payment ID: %s" % (cart1.payment_id)

        else:
            message = ""

        context["message"] = message

        subject = 'Compendium Magic Order'
        from_email = settings.SHOP_FROM_EMAIL
        to_email_customer = [request.user.email]
        to_email_compendium = [settings.SHOP_FROM_EMAIL]

        for item in ShippingInfo.objects.filter(user=request.user, active=True):
            info = item

        email_context = Context({
            'name': str(info.first_name)+" "+str(info.last_name),
            'email': request.user.email,
            'address_line_1': str(info.house_number)+" "+str(info.street_name),
            'address_line_2': str(info.postcode),
            'address_line_3': str(info.county),
            'address_line_4': str(info.country),
            'book_cart': book_orders,
            'misc_cart': misc_orders,
            'trick_cart': trick_orders,
            'apparel_cart': apparel_orders,
            'total': total,
        })

        text_email = render_to_string('email/purchase_email.txt', email_context)
        html_email = render_to_string('email/purchase_email.html', email_context)

        msg = EmailMultiAlternatives(subject, text_email, from_email, to_email_customer)
        msg.attach_alternative(html_email, 'text/html')
        msg.content_subtype = 'html'
        msg.send()

        subject = 'Shop Order: ' + str(request.user.username)

        text_email = render_to_string('email/business_purchase_email.txt', email_context)
        html_email = render_to_string('email/business_purchase_email.html', email_context)

        msg = EmailMultiAlternatives(subject, text_email, from_email, to_email_compendium)
        msg.attach_alternative(html_email, 'text/html')
        msg.content_subtype = 'html'
        msg.send()



        return render(request, 'store/order_complete.html', context)

    else:
        return redirect('index')

def shipping_info(request):

    if request.user.is_authenticated():

        cart = Cart.objects.filter(user=request.user.id, active=True)
        book_orders = BookOrder.objects.filter(cart=cart)
        misc_orders = MiscOrder.objects.filter(cart=cart)
        apparel_orders = ApparelOrder.objects.filter(cart=cart)
        trick_orders = TrickOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        f = open('order.txt','w')
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
            f.write(str(order.item.title))
        f.close()


        shipping = ShippingInfo.objects.filter(user=request.user)

        context = {
            'shipping': shipping,
            'total': total,
            'count': count,
        }

        if request.method == "POST":
            f = open('shipping.txt', 'w')
            f.write(str(request.POST))
            f.close()

            f = open('item.txt', 'w')
            for item in ShippingInfo.objects.filter(user=request.user):

                f.write("Before: "+str(item.active)+"\n")
                try:
                    if int(request.POST['active_address']) == item.id:
                        item.active = True
                    else:
                        item.active = False
                except:
                    item.active = False

                f.write("After: " + str(item.active) + "\n")
                item.save()
            f.close()

            form = ShippingForm(request.POST)
            if form.is_valid():
                new_shipping = ShippingInfo.objects.create(
                    user=request.user,
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    street_name = form.cleaned_data.get('street_name'),
                    house_number = form.cleaned_data.get('house_number'),
                    postcode = form.cleaned_data.get('postcode'),
                    country = form.cleaned_data.get('country'),
                    active = True,
                )
                new_shipping.save()
            form = ShippingForm()
            context['form'] = form
        else:
            form = ShippingForm()
            context['form'] = form
        try:
            active_address = False
            for item in ShippingInfo.objects.filter(user=request.user, active=True):
                try:
                    active_address = item.active
                except:
                    active_address = False
        except:
            active_address = False

        context['active_address'] = active_address

        return render(request, 'store/shipping_info.html', context)
    else:
        return redirect('index')