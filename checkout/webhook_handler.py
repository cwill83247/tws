from django.http import HttpResponse

# use for Stripe Webhooks
class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Dealing with unknown stripe webhook events or errors
        """
        return HttpResponse(
            content=f'Unknown Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        payment_intent.succeeded - Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        payment_intent.payment_failed - Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)        