from empire_chain.payments import StripePaymentUI

payment_ui = StripePaymentUI(
    title="Empire Chain Subscription", 
    amount=50,  
    verbose=True   
)