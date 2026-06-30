# How do you use design patterns in your project?
"""
1. Factory Method Pattern
Notification Service
Currently: Email -> Later: Email, SMS, WhatsApp, Push Notification
Factory: NotificationFactory.get("email") -> returns: EmailNotification() or WhatsappNotification()

2. Singleton Pattern
S3 Client or Redis Client
one connection pool, reused everywhere

3. Service Layer Pattern : We followed a Service Layer architecture so our views remain thin 
and business logic stays reusable and testable.

4. Strategy Pattern :
Imagine your leave calculation.

Instead of
if leave == "Casual":
    ...
elif leave == "Medical":
    ...
elif leave == "Comp Off":
    ...
Create
LeaveStrategy

CasualLeaveStrategy, MedicalLeaveStrategy, CompOffStrategy

Now
strategy.calculate_leave(...)
No huge if-else.

In my projects I mainly prefer practical patterns rather than forcing design patterns everywhere.
Service Layer to separate business logic from API views.
Factory Method for creating different ticket generators, notification handlers, or payment gateway integrations.
Singleton for shared resources like Redis, S3, SMTP and Razorpay clients.
Dependency Injection in FastAPI using Depends() for injecting database sessions and services.
Strategy pattern for handling different business rules like leave calculations or ticket pricing.
Facade pattern by exposing a single booking service that internally coordinates payment verification, 
QR generation, ticket creation, S3 upload and email notification.
"""

# How do you use solid principles in your project?
"""
1. Single Responsibility Principle (SRP): One class should have only one reason to change.
Imagine your webhook looks like this:
def razorpay_webhook(request):
    verify_signature(), save_payment(), create_enrollment(), generate_booking_id(), generate_qr()
    create_ticket_image(), upload_s3(), send_email(), send_whatsapp()
    return Response(...)

One function is doing 8 different jobs.
If tomorrow QR generation Or S3 Or Email changes, you modify this function. Bad SRP.

✅ Better
Split responsibilities.
services/
payment_service.py, ticket_service.py, booking_service.py, qr_service.py, storage_service.py, notification_service.py

Webhook:
payment_service.verify()
booking = booking_service.create()
qr = qr_service.generate()
ticket = ticket_service.create()
storage_service.upload(ticket)
notification_service.send_ticket()
Every class has one responsibility.


2. Open Closed Principle: Open for Extension Closed for Modification
Today: Only Razorpay
Later: Stripe, Paypal, PhonePe

Don't do
if gateway=="razorpay":
    ...
elif gateway=="stripe":
    ...
elif gateway=="paypal":

Instead:
PaymentGateway
        ↑
 -----------------------
 |         |          |
Razorpay Stripe PhonePe

Every gateway implements
verify(), capture(), refund()

When Stripe comes,
Create
StripeGateway
No existing code changes.


3. Liskov Substitution Principle
Suppose: StorageService has upload(file)
Current implementation: S3Storage
Later: Azure Blob or Google Cloud Storage

Both should work.
storage.upload(ticket)

without changing calling code.
Example:
StorageService
↑
S3Storage, AzureStorage


4. Interface Segregation Principle
Suppose: NotificationService contains send_email(), send_sms(), send_whatsapp(), send_push_notification()

Your project only sends email.
Why should EmailService implement WhatsApp?

Instead: EmailNotifier, WhatsappNotifier, SMSNotifier
Each class only implements what it needs.

5. Dependency Inversion Principle
Suppose: TicketService does
s3 = boto3.client(...)
s3.upload(...)
Now TicketService is tightly coupled with AWS.

Instead: 
TicketService(storage)
storage.upload(ticket)

Pass
S3Storage or LocalStorage

SRP — Separate PaymentService, TicketService, OTPService, StorageService, NotificationService.
OCP — Design payment gateways or storage providers so you can add new implementations 
        (e.g., Stripe or Azure Storage) without modifying existing business logic.
DIP — Depend on abstractions (e.g., StorageService) rather than directly calling boto3 or Redis 
        from your business logic.
"""
