# from django import forms
# from .models import ShopClient, Delivery, Payment, ClientBankAccount, ClientElectronWallet
#

# class ClientCreateForm(forms.ModelForm):
#     class Meta:
#         model = ShopClient
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'street', 'house']
#
#
# class DeliveryCreateForm(forms.Form):
#     delivery_name = forms.ChoiceField(widget=forms.Select(),
#                                       choices=((delivery.id, str(delivery.name)) for delivery in
#                                                Delivery.objects.all()))
#     delivery_cost = forms.Textarea()
#
#
# class PaymentCreateForm(forms.Form):
#     pay_name = forms.ChoiceField(widget=forms.Select(),
#                                  choices=((payment.id, str(payment.name)) for payment in
#                                           Payment.objects.all()))
#
#
# class ClientBankAccountCreateForm(forms.ModelForm):
#     class Meta:
#         model = ClientBankAccount
#         fields = ['card_number', 'card_holder', 'validity', 'cvc_code']
#     # validity = forms.DateField(
#     #     input_formats=['%d/%m/%Y'],
#     #     widget=forms.DateInput(attrs={
#     #         'class': 'form-control datetimepicker-input',
#     #         'data-target': '#datetimepicker1'
#     #     })
#     # )
#
#
# class ClientElectronWalletCreateForm(forms.ModelForm):
#     class Meta:
#         model = ClientElectronWallet
#         fields = ['account_number', 'account_holder']
