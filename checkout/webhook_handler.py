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
        intent = event.data.object
        if intent.mode == 'payment' and intent.payment_status == 'succeeded':              # strip 31/3/23
            try:                                                                            # strip 31/3/23
                order = Order.objects.get(id=session.client_reference_id)               # strip 31/3/23
            except Order.DoesNotExist:                                                      # strip 31/3/23
                return HttpResponse(status=404)                                         # strip 31/3/23
            order.paid = True                                                       # strip 31/3/23
            order.save()                                                            # strip 31/3/23   

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