from paypalrestsdk import BillingAgreement
import logging

logging.basicConfig(level=logging.INFO)

billing_agreement = BillingAgreement({
    "name": "Fast Speed Agreement",
    "description": "Agreement for Fast Speed Plan",
    "start_date": "2015-02-19T00:37:04Z",
    "plan": {
        "id": "P-0NJ10521L3680291SOAQIVTQ"
    },
    "payer": {
        "payment_method": "paypal"
    },
    "shipping_address": {
        "line1": "StayBr111idge Suites",
        "line2": "Cro12ok Street",
        "city": "San Jose",
        "state": "CA",
        "postal_code": "95112",
        "country_code": "US"
    }
})

# Parse links and get agreement id
def get_agreement_id(links):
    for link in links:
        if link.rel == "approval_url":
            return parse.parse_qs(parse.urlparse(link.href).query)["token"][0]

if billing_agreement.create(None, None, True):
    result = {
        "id": get_agreement_id(billing_agreement.links),
        "name": billing_agreement.name,
        "description": billing_agreement.description,
        "plan_state": billing_agreement.plan.state,
        "start_date": billing_agreement.start_date,
        "links": [
            {
                "href": link.href,
                "rel": link.rel,
                "method": link.method
            } for link in billing_agreement.links
        ]
    }
    
    #print(result)
    print("Billing Agreement created successfully with id {}".format(result['id']))
else:
    print(billing_agreement.error)
