from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# use for Stripe Webhooks
class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    """ This private method handles the confirmation email """
    def _send_confirmation_email(self, order):
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order})
        
        """ sending the mail """
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )             

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

        self._send_confirmation_email(order)                                                 ######  Send Confrimation email 1/4/23
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