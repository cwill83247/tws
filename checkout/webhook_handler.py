from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class StripeWH_Handler:
    """used for Stripe Webhooks"""

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
        if intent.mode == 'payment' and intent.payment_status == 'succeeded':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            order.paid = True
            order.save()

        self._send_confirmation_email(order)
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
