#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE  

import qrcode

name = input("Recipient Name: ")
upi_id = input("UPI ID: ")

#Different URL based on UPI ID and Payment Application

#f strings are used to embed the variable values into the strings
# mc is the merchant code, which is optional and can be left blank if not needed

phonepe_url = f"upi://pay?pa={upi_id}&pn={name}&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn={name}&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn={name}&mc=1234"

phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url) 
paytm_qr = qrcode.make(paytm_url)

# Save the QR codes as images
phonepe_qr.save("phonepe_qr.png")
google_pay_qr.save("google_pay_qr.png")
paytm_qr.save("paytm_qr.png")  

# Display the QR codes
phonepe_qr.show()   
google_pay_qr.show()
paytm_qr.show()


