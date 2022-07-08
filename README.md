# QR Payments System ( QR-GENERATOR )

### Follow this link to view the hosted version of this project:
https://qrps-qr-generator.herokuapp.com/

# Problem

We took this problem statement by experiencing the problem to make UPI payments in our college canteen. Lack of internet services in our college motivated us to try building a prototype to this problem.

# Our Approach

1. Our solutions begins with the belief of having a money deposit section managed by our college, where students deposit there pocket money.
2. If we place Touch Screen Monitors at every stall to take orders and deduct money from respective student account, it results in huge cost for        
   maintenance.
3. So, we thought of storing the user order in the form of a QR Code.
4. By having a QR Scanner at every stall helps in reading the QR Code and perform the transaction.
5. We want to replace this web app by a mobile application which stores data regarding food stalls and food items.
6. Thus user can login when he has internet and can use this app even when user is offline and generate QR Codes.
7. We want to replace Touch Screen Monitors with student's mobiles to make food orders.

# What's inside the QR?
This QR Code contains the details like:
   User Data:
        1. username,
        2. encrypted password.
        
   QR Meta Data:
        1. Date of QR generation,
        2. Time of QR generation.
        
   Food Data:
        1. Quantity of Food ordered,
        2. Prices from Mobile App (compared with prices in database while scanning),
        3. Food stall name.