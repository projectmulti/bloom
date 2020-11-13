from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


from .cart import Cart

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['salesreportdynarielinnovations@gmail.com', order.email]
    send_mail( subject, message, email_from, recipient_list )
    html_content = render_to_string('order_confirmation.html', {'order': order})

    pdf = render_to_pdf('order_pdf.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    if pdf:
        name = 'order_%s.pdf' % order.id
        msg.attach(name, pdf, 'application/pdf')

    msg.send()
    return redirect('redirect to a new page')

def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url, product.num_available)

        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        address = request.user.userprofile.address
        zipcode = request.user.userprofile.zipcode
        state = request.user.userprofile.state
        phone = request.user.userprofile.phone
    else:
        first_name = last_name = email = address = zipcode = state = phone = ''

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'zipcode': zipcode,
        'state': state,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'pub_key_razorpay': settings.RAZORPAY_API_KEY_PUBLISHABLE,
        'pub_key_paypal': settings.PAYPAL_API_KEY_PUBLISHABLE,
        'pub_key_paystack': settings.PAYSTACK_API_KEY_PUBLISHABLE,
        'productsstring': productsstring.rstrip(',')
    }

    return render(request, 'cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'success.html')