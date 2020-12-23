# from celery import task
# from django.core.mail import send_mail
# from .models import ShopOrder
#
#
# @task
# def order_created(order_id):
#     order = ShopOrder.objects.get(id=order_id)
#     subject = f"Order nr. {order_id}"
#     message = f"Dear {order.client.first_name},\n\nYou have successfully placed an order. Your order id is {order.id}."
#     mail_sent = send_mail(subject,
#                           message,
#                           'admin@myshop.com',
#                           [order.client.email])
#     return mail_sent
