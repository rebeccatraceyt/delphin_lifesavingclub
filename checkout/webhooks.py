from django.conf import settings
from django.http import HttpResponse
from checkout.webhook_handler import StripeWH_Handler

import stripe

# reject GET methods
from django.views.decorators.http import require_POST

# So we don't require csrf token
from django.views.decorators.csrf import csrf_exempt


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from Stripe """

    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # additional error
        return HttpResponse(content=e, status=400)

    print('Success!')
    return HttpResponse(status=200)
