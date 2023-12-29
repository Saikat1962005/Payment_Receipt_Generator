class PaymentReceiptGenerator:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, unit_price, quantity):
        try:
            unit_price = float(unit_price)
            quantity = float(quantity)
            self.products.append((product_name, unit_price, quantity))
            print("Product added successfully.")
        except ValueError:
            print("Error: Please enter valid numeric values for unit price and quantity.")

    def generate_receipt(self, customer_name):
        if not self.products:
            print("Error: Please add at least one product.")
            return

        total_amount = sum(unit_price * quantity for _, unit_price, quantity in self.products)

        # Create the payment receipt
        receipt_text = f"\n{'*' * 40}\nPayment Receipt\n{'*' * 40}\n"
        receipt_text += f"\nCustomer Name: {customer_name}\nStore Name: Squadtrion\n\nProducts Purchased:\n"

        for product in self.products:
            product_name, unit_price, quantity = product
            total_price = unit_price * quantity
            receipt_text += f"{product_name} - ${unit_price:.2f} x {quantity} = ${total_price:.2f}\n"

        receipt_text += f"\n{'-' * 40}\nTotal Amount: ${total_amount:.2f}\n{'*' * 40}"

        # Display the receipt
        print(receipt_text)


if __name__ == "__main__":
    receipt_generator = PaymentReceiptGenerator()

    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        unit_price = input("Enter unit price: ")
        quantity = input("Enter quantity: ")

        receipt_generator.add_product(product_name, unit_price, quantity)

    customer_name = input("Enter customer name: ")
    receipt_generator.generate_receipt(customer_name)
