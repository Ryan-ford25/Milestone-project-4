from django.shortcuts import redirect, render
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def upgrade(request):
    return render(request, 'payment/upgrade.html')

@login_required
def create_checkout(request, plan):
    # Logic to create Stripe checkout session based on the selected plan (monthly or annual)
    # Redirect user to Stripe checkout page
    if plan == 'monthly':
        # Create Stripe checkout session for monthly plan
        amount= 999 
        plan_name = "Monthly Plan"

    elif plan == 'annual':
        # Create Stripe checkout session for annual plan
        amount = 9999 
        plan_name = "Annual Plan"
    else:
        # Invalid plan, handle error
        return redirect('home')
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'unit_amount': amount,
                'product_data': {
                    'name': plan_name,
                },
            },
            'quantity': 1
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/payment/success/') + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri('/payment/cancel/'),
    )

    return redirect(checkout_session.url)

@login_required
def payment_success(request):
    # Logic to handle successful payment, update user subscription status, etc.
    session_id = request.GET.get('session_id')
    if not session_id:
        return redirect('upgrade')
    
    # Retrieve the session from Stripe
    session = stripe.checkout.Session.retrieve(session_id)

    if session.payment_status == 'paid':
        user = request.user
        # Update user's subscription status in your database
        user.is_premium = True
        user.save()
        
    return render(request, 'payment/payment_successful.html')

@login_required
def payment_cancel(request):
    # Logic to handle payment cancellation, show message to user, etc.
    return render(request, 'payment/payment_cancelled.html')