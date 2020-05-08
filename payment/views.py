from django.shortcuts import render, redirect
from django.http import HttpResponse
# from pypaystack import Transaction, Customer, Plan
from django.conf import settings
# import braintree

# Create your views here.

# paypal
# gateway = braintree.BraintreeGateway(access_token='access_token$sandbox$cf2szyscwgfnhpj6$9bead1b8aecff6549481c2e7b7f31356')
# def client_token(request):
# 	client_token = gateway.client_token.generate()
# 	return render(request,'payment/ppmethod.html',{'client_token':client_token})

# def transact(request,nonce):
# 	nonce = str(nonce)
# 	result = gateway.transaction.sale({
#     "amount" : 10.00,
#     "merchant_account_id": "USD",
#     "payment_method_nonce" : nonce,
#     "order_id" : "Mapped to PayPal Invoice Number",
#     "descriptor": {
#       "name": "Descriptor displayed in customer CC statements. 22 char max"
#     },
#     "shipping": {
#       "first_name": "Jen",
#       "last_name": "Smith",
#       "company": "Braintree",
#       "street_address": "1 E 1st St",
#       "extended_address": "Suite 403",
#       "locality": "Bartlett",
#       "region": "IL",
#       "postal_code": "60103",
#       "country_code_alpha2": "US"
#     },
#     "options" : {
#       "paypal" : {
#         "custom_field" : "PayPal custom field",
#         "description" : "Description for PayPal email receipt"
#     	},
#     }
# 	})
# 	if result.is_success:
# 	    return HttpResponse(f'{result.transaction.id} succesful')
# 	else:
# 		return HttpResponse('failed')

# paystack
def charge(request):
    return render(request, 'payment/checkout.html')

def verify(request, reference):
    # transaction = Transaction(settings.SK_KEY)
    # response = transaction.verify(reference)
    # if response[3]['status'] == 'success':
    return render(request,'pages/success.html',{'reference':reference})
    # else:
        # return HttpResponse('failed')
    # return HttpResponse(response)