from django.shortcuts import render, redirect
from django.http import HttpResponse
# from pypaystack import Transaction, Customer, Plan
from django.conf import settings
# rave
# import unirest #unirest is an http library
import json

# Create your views here.

# checkout
def charge(request):
    return render(request, 'payment/checkout.html')

# verifying transaction
def verify(request, reference):
    # transaction = Transaction(settings.SK_KEY)
    # response = transaction.verify(reference)
    # if response[3]['status'] == 'success':
    return render(request,'pages/success.html',{'reference':reference})
    # else:
        # return HttpResponse('failed')
    # return HttpResponse(response)

# rave
def flutterwave_rave_charge(request):
	return render(request,'payment/rave_checkout.html')

#function called after your request gets a response from rave's server
def verify_rave(request,response):
    pass
	# data = {
	# 	"txref": "MC-1520443531487", #this is the reference from the payment button response after customer paid.
	# 	"SECKEY": "FLWSECK-9b4a9495dc795802ed64644c08357494-X" #this is the secret key of the pay button generated
	# 	}
 #    #confirm that the response for the transaction is successful
 #    if response.body['data']['status'] == 'success':
 #      #confirm that the amount for that transaction is the amount you wanted to charge
 #        if response.body['data']['chargecode'] == '00':
        
 #            if response.body['data']['amount'] == 2000:
 #                print("Payment successful then give value")
      

	# #this is the url of the staging server. Please make sure to change to that of production server when you are ready to go live.
	# url = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/v2/verify"

	# #make the http post request to our server with the parameters
	# thread = unirest.post(url, headers={"Content-Type":"application/json"}, params=data, callback=callback_function)








# import braintree
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