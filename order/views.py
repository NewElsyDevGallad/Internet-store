from django.shortcuts import render, get_object_or_404
from .models import OrderItem, ShopOrder, Payment, Delivery
from .forms import ClientCreateForm, DeliveryCreateForm, PaymentCreateForm, \
    ClientBankAccountCreateForm, ClientElectronWalletCreateForm
from cart.cart import Cart
from .task import order_created


def order_create(request):
    cart = Cart(request)
    client = None
    delivery_name = None
    payment_name = None
    pay_mtd = None
    delivery_cost = 0
    delivery_costs = []
    for delivery in Delivery.objects.all():
        delivery_costs.append(get_object_or_404(Delivery, id=delivery.id).cost)
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        delivery_form = DeliveryCreateForm(request.POST)
        payment_form = PaymentCreateForm(request.POST)
        if form.is_valid():
            client = form.save()
        if delivery_form.is_valid():
            delivery = delivery_form.cleaned_data['delivery_name']
            delivery_name = Delivery(delivery_form.cleaned_data['delivery_name'])
            delivery_cost = get_object_or_404(Delivery, id=delivery).cost
        if payment_form.is_valid():
            payment = payment_form.cleaned_data['pay_name']
            payment_name = Payment(payment_form.cleaned_data['pay_name'])
            pay_mtd = get_object_or_404(Payment, id=payment).name
        order = ShopOrder.objects.create(
            client=client,
            delivery=delivery_name,
            pay_method=payment_name
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        order_created.delay(order.id)
        total_cost = order.get_total_cost() + delivery_cost
        return render(request, 'order/created.html',
                      {'order': order, 'total_cost': total_cost, 'payment': pay_mtd})
    else:
        form = ClientCreateForm
        delivery_form = DeliveryCreateForm
        payment_form = PaymentCreateForm
    return render(request, 'order/create.html',
                  {'cart': cart, 'form': form, 'delivery_form': delivery_form, 'payment_form': payment_form,
                   'delivery_costs': delivery_costs})


def pay_method(request, order_id, pay_method):
    bank_cards = ["Visa", "Mir", "MasterCard"]
    if request.method == 'POST':
        if pay_method in bank_cards:
            form = ClientBankAccountCreateForm(request.POST)
            if form.is_valid():
                form.save()
                order = get_object_or_404(ShopOrder, id=order_id)
                order.paid = True
                order.save()
        else:
            form = ClientElectronWalletCreateForm(request.POST)
            if form.is_valid():
                form.save()
                order = get_object_or_404(ShopOrder, id=order_id)  # get once created object
                order.paid = True  # change field
                order.save()  # save object
        return render(request, 'order/payment_ok.html')
    else:
        if pay_method in bank_cards:
            form = ClientBankAccountCreateForm
        else:
            form = ClientElectronWalletCreateForm
    return render(request, 'order/payment.html', {'form': form})
