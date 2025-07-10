import streamlit as st
import stripe
import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, Any, Optional
import re
from fpdf import FPDF
import tempfile
import uuid

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InvoicePDF(FPDF):
    """Custom PDF class for generating professional invoices."""
    
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        # Logo - You might want to replace this with your actual logo
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Empire Chain', 0, 1, 'L')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_invoice_header(self, invoice_no: str, date: str):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(0)
        self.cell(0, 10, 'INVOICE', 0, 1, 'R')
        self.set_font('Helvetica', '', 10)
        self.cell(0, 5, f'Invoice No: {invoice_no}', 0, 1, 'R')
        self.cell(0, 5, f'Date: {date}', 0, 1, 'R')
        self.ln(10)

    def add_billing_info(self, customer_name: str, customer_email: str):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Bill To:', 0, 1, 'L')
        self.set_font('Helvetica', '', 10)
        self.cell(0, 5, customer_name, 0, 1, 'L')
        self.cell(0, 5, customer_email, 0, 1, 'L')
        self.ln(10)

    def add_company_info(self):
        self.set_font('Helvetica', '', 10)
        self.cell(0, 5, 'Empire Chain Inc.', 0, 1, 'L')
        self.cell(0, 5, '123 Tech Street', 0, 1, 'L')
        self.cell(0, 5, 'Silicon Valley, CA 94025', 0, 1, 'L')
        self.cell(0, 5, 'United States', 0, 1, 'L')
        self.ln(10)

    def add_item_header(self):
        self.set_fill_color(240, 240, 240)
        self.set_font('Helvetica', 'B', 10)
        self.cell(100, 10, 'Description', 1, 0, 'L', 1)
        self.cell(30, 10, 'Quantity', 1, 0, 'C', 1)
        self.cell(30, 10, 'Unit Price', 1, 0, 'R', 1)
        self.cell(30, 10, 'Amount', 1, 1, 'R', 1)

    def add_item(self, description: str, quantity: int, unit_price: float):
        self.set_font('Helvetica', '', 10)
        amount = quantity * unit_price
        self.cell(100, 10, description, 1, 0, 'L')
        self.cell(30, 10, str(quantity), 1, 0, 'C')
        self.cell(30, 10, f'${unit_price:.2f}', 1, 0, 'R')
        self.cell(30, 10, f'${amount:.2f}', 1, 1, 'R')

    def add_total(self, total: float):
        self.set_font('Helvetica', 'B', 10)
        self.cell(160, 10, 'Total:', 1, 0, 'R')
        self.cell(30, 10, f'${total:.2f}', 1, 1, 'R')

    def add_payment_info(self, transaction_id: str):
        self.ln(10)
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 10, 'Payment Information', 0, 1, 'L')
        self.set_font('Helvetica', '', 10)
        self.cell(0, 5, f'Transaction ID: {transaction_id}', 0, 1, 'L')
        self.cell(0, 5, 'Payment Method: Credit Card', 0, 1, 'L')
        self.cell(0, 5, 'Status: Paid', 0, 1, 'L')

    def add_footer_note(self):
        self.ln(10)
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 5, 'Thank you for your business! For any questions about this invoice, please contact support@empirechain.ai')

def generate_invoice(
    customer_name: str,
    customer_email: str,
    product_name: str,
    amount: float,
    transaction_id: str
) -> str:
    """Generate a professional PDF invoice and return the file path."""
    
    # Create PDF
    pdf = InvoicePDF()
    pdf.add_page()
    
    # Add invoice details
    invoice_no = f"INV-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8]}"
    date = datetime.now().strftime("%B %d, %Y")
    
    pdf.add_invoice_header(invoice_no, date)
    pdf.add_company_info()
    pdf.add_billing_info(customer_name, customer_email)
    
    # Add items
    pdf.add_item_header()
    pdf.add_item(product_name, 1, amount)
    pdf.add_total(amount)
    
    # Add payment information
    pdf.add_payment_info(transaction_id)
    pdf.add_footer_note()
    
    # Save to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        pdf.output(tmp.name)
        return tmp.name

class _StripePayment:
    """Internal Stripe payment handler."""
    
    # Test payment method tokens for different scenarios
    TEST_PAYMENT_METHODS = {
        "4242424242424242": "pm_card_visa",  # Success
        "4000000000000002": "pm_card_chargeDeclined",  # Declined
        "4000000000009995": "pm_card_visa_chargeInsufficientFunds",  # Insufficient funds
        "4000000000000119": "pm_card_visa_chargeDeclinedProcessingError"  # Processing error
    }
    
    def __init__(self):
        """Initialize Stripe payment handler."""
        try:
            api_key = os.getenv('STRIPE_SECRET_KEY')
            if not api_key:
                logger.error("STRIPE_SECRET_KEY not found in environment variables")
                raise ValueError("STRIPE_SECRET_KEY not found in environment variables")
                
            stripe.api_key = api_key
            logger.info("Successfully initialized Stripe")
        except Exception as e:
            logger.error(f"Failed to initialize Stripe: {str(e)}")
            raise

    def create_customer(self, email: str, name: str) -> Dict[str, Any]:
        """Create a Stripe customer."""
        try:
            customer = stripe.Customer.create(
                email=email,
                name=name,
                metadata={
                    'created_at': datetime.now().isoformat(),
                    'source': 'empire_chain'
                }
            )
            logger.info(f"Created customer: {customer.id}")
            return customer
        except Exception as e:
            logger.error(f"Error creating customer: {str(e)}")
            raise

    def process_payment(
        self,
        amount: float,
        currency: str,
        customer_id: str,
        payment_method: str,
        description: str,
        metadata: Optional[Dict[str, str]] = None,
        return_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """Process a payment using Stripe."""
        try:
            amount_cents = int(amount * 100)
            
            payment_intent = stripe.PaymentIntent.create(
                amount=amount_cents,
                currency=currency,
                customer=customer_id,
                payment_method=payment_method,
                confirm=True,
                return_url=return_url,
                description=description,
                metadata=metadata or {}
            )
            
            logger.info(f"Created payment intent: {payment_intent.id}")
            return payment_intent
        except Exception as e:
            logger.error(f"Error processing payment: {str(e)}")
            raise

    def validate_test_card(self, card_number: str) -> tuple[bool, str]:
        """Validate a test card number."""
        card_number = card_number.replace(" ", "")
        if not card_number.isdigit():
            return False, "Card number should contain only digits"
        if len(card_number) != 16:
            return False, "Card number should be 16 digits"
        if card_number not in self.TEST_PAYMENT_METHODS:
            return False, "Please use one of the test card numbers provided"
        return True, ""

    def get_test_payment_method(self, card_number: str) -> str:
        """Get the test payment method token for a card number."""
        card_number = card_number.replace(" ", "")
        return self.TEST_PAYMENT_METHODS.get(card_number, "")

    @staticmethod
    def validate_email(email: str) -> tuple[bool, str]:
        """
        Enhanced email validation using regex.
        Returns (is_valid, error_message)
        """
        # Regular expression for email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not email:
            return False, "Email is required"
        if not re.match(email_pattern, email):
            return False, "Please enter a valid email address (e.g., user@example.com)"
        return True, ""

    @staticmethod
    def validate_expiry_date(month: int, year: int) -> tuple[bool, str]:
        """
        Validate if the expiry date is in the future.
        Returns (is_valid, error_message)
        """
        now = datetime.now()
        expiry_date = datetime(year=year, month=month, day=1)
        
        if expiry_date.year < now.year or (expiry_date.year == now.year and expiry_date.month < now.month):
            return False, "Card has expired. Please use a valid expiry date."
        return True, ""

    @staticmethod
    def validate_cvc(cvc: str) -> tuple[bool, str]:
        """
        Validate CVC/CVV number.
        Returns (is_valid, error_message)
        """
        if not cvc:
            return False, "CVC is required"
        if not cvc.isdigit():
            return False, "CVC must contain only digits"
        if len(cvc) not in [3, 4]:
            return False, "CVC must be 3 or 4 digits"
        return True, ""

class StripePaymentUI:
    """
    Streamlit UI for processing payments with Stripe.
    
    Example:
        ```python
        from empire_chain.payments import StripePaymentUI
        
        payment_ui = StripePaymentUI(
            title="Premium Package",
            amount=49.99,
            verbose=True  # Show test card details
        )
        ```
    """
    
    def __init__(
        self,
        title: str = "Secure Checkout",
        amount: float = 0.0,
        verbose: bool = True,
        base_url: Optional[str] = None
    ):
        """
        Initialize the payment UI.
        
        Args:
            title (str): Page title and product name
            amount (float): Price amount
            verbose (bool): Whether to show test card information
            base_url (Optional[str]): Base URL for return URLs
        """
        self.title = title
        self.amount = amount
        self.verbose = verbose
        self.base_url = base_url or os.getenv('BASE_URL', 'http://localhost:8501')
        
        # Initialize Stripe payment handler
        self._stripe = _StripePayment()
        
        # Start the UI
        self.render()

    def render(self):
        """Render the payment form UI."""
        # Page configuration
        st.set_page_config(
            page_title=self.title,
            page_icon="💳",
            layout="centered"
        )

        # Custom CSS
        st.markdown("""
            <style>
            .stButton>button {
                width: 100%;
                background-color: #635BFF;
                color: white;
                height: 48px;
            }
            .main {
                padding: 2rem;
            }
            .card-element {
                border: 1px solid #E0E0E0;
                padding: 10px;
                border-radius: 4px;
                background-color: white;
                margin: 10px 0;
            }
            .error-text {
                color: #ff0000;
                font-size: 0.8em;
                margin-top: -1em;
                margin-bottom: 1em;
            }
            </style>
        """, unsafe_allow_html=True)

        # Main payment form
        st.title(self.title)

        # Product details
        st.markdown(f"""
            ### {self.title}
            **Price:** ${self.amount:.2f} USD
            
            ---
        """)

        # Payment form
        with st.form("payment_form"):
            # Customer information
            st.subheader("Customer Information")
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            
            # Card information
            st.subheader("Card Information")
            card_number = st.text_input("Card Number", placeholder="4242 4242 4242 4242")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                exp_month = st.selectbox("Month", range(1, 13))
            with col2:
                current_year = datetime.now().year
                exp_year = st.selectbox("Year", range(current_year, current_year + 11))
            with col3:
                cvc = st.text_input("CVC", placeholder="123", max_chars=4)
            
            # Submit button
            submit = st.form_submit_button("Pay Now")
            
            if submit:
                self._handle_payment_submission(
                    name=name,
                    email=email,
                    card_number=card_number,
                    exp_month=exp_month,
                    exp_year=exp_year,
                    cvc=cvc
                )

        # Display receipt and download button outside the form
        if 'payment_success' in st.session_state:
            payment_data = st.session_state.payment_success
            
            # Generate invoice
            invoice_path = generate_invoice(
                customer_name=payment_data['name'],
                customer_email=payment_data['email'],
                product_name=payment_data['title'],
                amount=payment_data['amount'],
                transaction_id=payment_data['transaction_id']
            )
            
            # Display receipt
            st.markdown("### Receipt")
            st.markdown(f"""
                **Order Details:**
                - Product: {payment_data['title']}
                - Amount: ${payment_data['amount']:.2f}
                - Email: {payment_data['email']}
                - Transaction ID: {payment_data['transaction_id']}
            """)
            
            # Add invoice download button
            with open(invoice_path, "rb") as f:
                invoice_bytes = f.read()
            st.download_button(
                label="📥 Download Invoice",
                data=invoice_bytes,
                file_name=f"invoice_{datetime.now().strftime('%Y%m%d')}_{payment_data['transaction_id'][:8]}.pdf",
                mime="application/pdf"
            )
            
            # Clean up temporary file
            os.unlink(invoice_path)
            
            # Clear the payment success data after displaying
            if st.button("Make Another Payment"):
                del st.session_state.payment_success
                st.rerun()

        # Footer with test card information
        if self.verbose:
            self._render_footer()

    def _handle_payment_submission(
        self,
        name: str,
        email: str,
        card_number: str,
        exp_month: int,
        exp_year: int,
        cvc: str
    ):
        """Handle payment form submission and processing."""
        # Input validation
        if not name:
            st.error("Please enter your name")
            return

        # Email validation
        is_valid_email, email_error = self._stripe.validate_email(email)
        if not is_valid_email:
            st.error(email_error)
            return

        # Card validation
        is_valid_card, card_error = self._stripe.validate_test_card(card_number)
        if not is_valid_card:
            st.error(card_error)
            return

        # Expiry date validation
        is_valid_expiry, expiry_error = self._stripe.validate_expiry_date(exp_month, exp_year)
        if not is_valid_expiry:
            st.error(expiry_error)
            return

        # CVC validation
        is_valid_cvc, cvc_error = self._stripe.validate_cvc(cvc)
        if not is_valid_cvc:
            st.error(cvc_error)
            return

        with st.spinner("Processing payment..."):
            try:
                # Get test payment method
                payment_method = self._stripe.get_test_payment_method(card_number)
                
                # Create customer
                customer = self._stripe.create_customer(email=email, name=name)

                # Process payment
                intent = self._stripe.process_payment(
                    amount=self.amount,
                    currency='usd',
                    customer_id=customer.id,
                    payment_method=payment_method,
                    description=f"Payment for {self.title}",
                    metadata={
                        'customer_name': name,
                        'customer_email': email
                    },
                    return_url=f"{self.base_url}/success"
                )

                # Handle payment result
                if intent.status == "succeeded":
                    st.success("Payment successful! Thank you for your purchase.")
                    st.balloons()
                    
                    # Store successful payment data in session state for display outside form
                    st.session_state.payment_success = {
                        'name': name,
                        'email': email,
                        'title': self.title,
                        'amount': self.amount,
                        'transaction_id': intent.id
                    }
                    
                elif intent.status == "requires_action":
                    st.warning("Additional authentication required. You will be redirected to complete the payment.")
                    st.markdown(f"[Complete Payment]({intent.next_action.redirect_to_url.url})")
                else:
                    st.error(f"Payment failed. Status: {intent.status}")
                    
            except stripe.error.CardError as e:
                err = e.error
                st.error(f"Card Error: {err.message}")
                
            except stripe.error.InvalidRequestError as e:
                st.error("Invalid request. Please try again.")
                logger.error(f"Invalid request: {str(e)}")
                
            except Exception as e:
                st.error("An error occurred while processing your payment.")
                logger.error(f"Payment error: {str(e)}")

    def _render_footer(self):
        """Render the footer with test card information."""
        st.markdown("---")

        with st.expander("💳 Test Card Numbers (Click to expand)"):
            st.markdown("""
                Use these test card numbers:
                
                **Successful payment:**
                ```
                4242 4242 4242 4242
                Any future expiry date
                Any 3-digit CVC
                ```
                
                **Test error scenarios:**
                ```
                4000 0000 0000 0002 - Card declined
                4000 0000 0000 9995 - Insufficient funds
                4000 0000 0000 0119 - Processing error
                ```
                
                These are test cards and won't charge any real money.
            """)

        st.markdown("""
            <div style='text-align: center'>
                🔒 Secure payment powered by Stripe<br>
                Need help? Contact support@example.com
            </div>
        """, unsafe_allow_html=True) 