from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem


# on add,increase or delete items form shopping bag 
#run the below function(s) - is available across project.
@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when item is added or quantity
    updated in shopping bag calling update_total method
    in checkout > models.py within the Order class
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total when item is deleted from shopping bag 
    """
    instance.order.update_total()