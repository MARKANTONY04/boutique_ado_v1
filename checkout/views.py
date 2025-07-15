from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Rl6ZMD0OAI0fPSIL1CO8jsnohneT06tMj7TSnEQ0fmMNc8Fe112NUUIV5bQNKfUHoaWSJ0YKN1ShqvBhfVdcEZn000Cp5tQoM',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)