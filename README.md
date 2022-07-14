# QR Payments System

A payment system designed for fast and effective way of payments at an organization. A QR is generated for every bill the user generates and can be scanned at the vendor side. It eliminates issues at an organization where internet may be slow or transactions have to be faster.

**Deployed At:** https://qrps-qr-generator.herokuapp.com

## Working Model
- At an organization where issues like slower internet and faster transactions are needed without the help of the internet users can face problem during payments. 
- To eliminate such issues we have designed a payment system which works on the basis of QR.
- A user opens the app and selects the items he/she wants and generate a unique QR code valid for the particular items selected only.
- A user has to keep sufficent ammount in the organization deposit to generate QR for the selected items. 
- A vendor can scan the QR with the help of his phone and detect the ammount from the system. 
- At the end of the day the vendor can see his records containg the items he.she sold, ammount generated etc..
- By the help of this model it is very easy to handle transactions at an organization facing issues with the internet for eg: Especially in colleges students face a lot of problem with the internet due to many factors. it effects their daily UPI transactions at the canteen, stalls, fee payments etc.. By using the QR payments one need not worrry about the internet and can held transactions offline.

## QR Code
The generated QR contains the following:
- Username 
- Encrypted Password
- Date and Time of QR generation
- Food Stall Name
- Qunatity of each item
- Price of each item 
- **A generated QR is only valid for 15 miutes after generation for a single transaction**

## Tech Stack
      ### Front End
        - HTML
        - Bootstrap
        - CSS
        - JS
      ### Back End
         - Flask
         - Python
      ### Database
         - mySQL
      ### QR Code
      -  pyqrcode (QR Genertaion)
      - Open CV (QR Scanner)
   
## Extention of Project
The scanner part of the project can be found at **https://github.com/manchalaharikesh/QRPS-QR-GENERATOR**

## Further Scope
As of now the project works on the web. A future development would be to convert this into a mobile application using any cross platform tools like Flutter, React Native. 
 
