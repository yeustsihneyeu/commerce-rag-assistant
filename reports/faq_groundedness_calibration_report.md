# FAQ Groundedness Calibration Report

Source notebook: `notebooks/14_faq_groundedness_calibrating.ipynb`

## Overview

- Evaluated samples: 150
- Threshold: 0.500
- Mean groundedness score: 0.565
- Accuracy: 0.627

## Summary Tables

### Final Metrics

| samples | threshold | mean_groundedness_score | accuracy |
| --- | --- | --- | --- |
| 150 | 0.500 | 0.565 | 0.627 |

### Sample Results

| question | answer_type | groundedness_score | predicted_is_grounded | expected_is_grounded | label_match |
| --- | --- | --- | --- | --- | --- |
| Will I get a full refund including shipping if I return my order? | adversarial | 0.500 | 1 | 0 | 0 |
| Will I get a full refund including shipping if I return my order? | bad | 0.000 | 0 | 0 | 1 |
| Will I get a full refund including shipping if I return my order? | good | 1.000 | 1 | 1 | 1 |
| Can I use multiple delivery addresses for one order or just one? | adversarial | 0.250 | 0 | 0 | 1 |
| Can I use multiple delivery addresses for one order or just one? | bad | 0.250 | 0 | 0 | 1 |
| Can I use multiple delivery addresses for one order or just one? | good | 1.000 | 1 | 1 | 1 |
| Why does my payment status show as canceled or pending on HopShop? | adversarial | 0.500 | 1 | 0 | 0 |
| Why does my payment status show as canceled or pending on HopShop? | bad | 0.500 | 1 | 0 | 0 |
| Why does my payment status show as canceled or pending on HopShop? | good | 1.000 | 1 | 1 | 1 |
| How can I find the seller's email and phone number after I make a purchase? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I find the seller's email and phone number after I make a purchase? | bad | 0.250 | 0 | 0 | 1 |
| How can I find the seller's email and phone number after I make a purchase? | good | 1.000 | 1 | 1 | 1 |
| What should I do if my parcel was damaged when I picked it up? | adversarial | 0.500 | 1 | 0 | 0 |
| What should I do if my parcel was damaged when I picked it up? | bad | 0.250 | 0 | 0 | 1 |
| What should I do if my parcel was damaged when I picked it up? | good | 1.000 | 1 | 1 | 1 |
| How do I sign up using my Google or Facebook account? | adversarial | 0.500 | 1 | 0 | 0 |
| How do I sign up using my Google or Facebook account? | bad | 0.250 | 0 | 0 | 1 |
| How do I sign up using my Google or Facebook account? | good | 1.000 | 1 | 1 | 1 |
| How can I find my parcel's tracking number and check its delivery status on HopShop? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I find my parcel's tracking number and check its delivery status on HopShop? | bad | 0.500 | 1 | 0 | 0 |
| How can I find my parcel's tracking number and check its delivery status on HopShop? | good | 1.000 | 1 | 1 | 1 |
| How will I receive my refund from the seller? | adversarial | 0.500 | 1 | 0 | 0 |
| How will I receive my refund from the seller? | bad | 0.000 | 0 | 0 | 1 |
| How will I receive my refund from the seller? | good | 1.000 | 1 | 1 | 1 |
| How long does it take to get a refund for a wire transfer, and what if I used a postal order? | adversarial | 0.500 | 1 | 0 | 0 |
| How long does it take to get a refund for a wire transfer, and what if I used a postal order? | bad | 0.500 | 1 | 0 | 0 |
| How long does it take to get a refund for a wire transfer, and what if I used a postal order? | good | 1.000 | 1 | 1 | 1 |
| How is the estimated delivery time calculated on HopShop? | adversarial | 0.500 | 1 | 0 | 0 |
| How is the estimated delivery time calculated on HopShop? | bad | 0.500 | 1 | 0 | 0 |
| How is the estimated delivery time calculated on HopShop? | good | 1.000 | 1 | 1 | 1 |
| What happens to my gift card if I return an order I paid for with it? | adversarial | 0.500 | 1 | 0 | 0 |
| What happens to my gift card if I return an order I paid for with it? | bad | 0.000 | 0 | 0 | 1 |
| What happens to my gift card if I return an order I paid for with it? | good | 1.000 | 1 | 1 | 1 |
| How can I reorder a single product from my past purchases? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I reorder a single product from my past purchases? | bad | 0.500 | 1 | 0 | 0 |
| How can I reorder a single product from my past purchases? | good | 1.000 | 1 | 1 | 1 |
| How will I be notified when my refund is processed? | adversarial | 0.500 | 1 | 0 | 0 |
| How will I be notified when my refund is processed? | bad | 0.000 | 0 | 0 | 1 |
| How will I be notified when my refund is processed? | good | 1.000 | 1 | 1 | 1 |
| How can I open a Discussion if I canceled an order paid through HopShop Finance and haven’t received a refund? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I open a Discussion if I canceled an order paid through HopShop Finance and haven’t received a refund? | bad | 0.500 | 1 | 0 | 0 |
| How can I open a Discussion if I canceled an order paid through HopShop Finance and haven’t received a refund? | good | 1.000 | 1 | 1 | 1 |
| Why might my actual delivery time be different from the estimated delivery time? | adversarial | 0.500 | 1 | 0 | 0 |
| Why might my actual delivery time be different from the estimated delivery time? | bad | 0.500 | 1 | 0 | 0 |
| Why might my actual delivery time be different from the estimated delivery time? | good | 1.000 | 1 | 1 | 1 |
| Who is responsible if an item is damaged during delivery when buying from an entrepreneur? | adversarial | 0.500 | 1 | 0 | 0 |
| Who is responsible if an item is damaged during delivery when buying from an entrepreneur? | bad | 0.000 | 0 | 0 | 1 |
| Who is responsible if an item is damaged during delivery when buying from an entrepreneur? | good | 1.000 | 1 | 1 | 1 |
| What should I do if my pick-up code isn’t working at the parcel locker? | adversarial | 0.500 | 1 | 0 | 0 |
| What should I do if my pick-up code isn’t working at the parcel locker? | bad | 0.500 | 1 | 0 | 0 |
| What should I do if my pick-up code isn’t working at the parcel locker? | good | 1.000 | 1 | 1 | 1 |
| What happens if I frequently cancel or don't pay for my purchases on HopShop? | adversarial | 0.500 | 1 | 0 | 0 |
| What happens if I frequently cancel or don't pay for my purchases on HopShop? | bad | 0.250 | 0 | 0 | 1 |
| What happens if I frequently cancel or don't pay for my purchases on HopShop? | good | 1.000 | 1 | 1 | 1 |
| What do I need to do to pick up my parcel from a pick-up point? | adversarial | 0.500 | 1 | 0 | 0 |
| What do I need to do to pick up my parcel from a pick-up point? | bad | 0.500 | 1 | 0 | 0 |
| What do I need to do to pick up my parcel from a pick-up point? | good | 1.000 | 1 | 1 | 1 |
| How long does it take to get a BLIK refund and where can I see it in my bank account? | adversarial | 0.500 | 1 | 0 | 0 |
| How long does it take to get a BLIK refund and where can I see it in my bank account? | bad | 0.250 | 0 | 0 | 1 |
| How long does it take to get a BLIK refund and where can I see it in my bank account? | good | 1.000 | 1 | 1 | 1 |
| How do I pay for my order using PayPal and how does currency conversion work? | adversarial | 0.500 | 1 | 0 | 0 |
| How do I pay for my order using PayPal and how does currency conversion work? | bad | 0.250 | 0 | 0 | 1 |
| How do I pay for my order using PayPal and how does currency conversion work? | good | 1.000 | 1 | 1 | 1 |
| How can I change my parcel locker or pick-up point before the seller ships my order? | adversarial | 0.750 | 1 | 0 | 0 |
| How can I change my parcel locker or pick-up point before the seller ships my order? | bad | 0.250 | 0 | 0 | 1 |
| How can I change my parcel locker or pick-up point before the seller ships my order? | good | 1.000 | 1 | 1 | 1 |
| What are the options for returning a HopShop Delivery parcel? | adversarial | 0.500 | 1 | 0 | 0 |
| What are the options for returning a HopShop Delivery parcel? | bad | 0.000 | 0 | 0 | 1 |
| What are the options for returning a HopShop Delivery parcel? | good | 1.000 | 1 | 1 | 1 |
| How long will my parcel be held at the pick-up point before being sent back? | adversarial | 0.500 | 1 | 0 | 0 |
| How long will my parcel be held at the pick-up point before being sent back? | bad | 0.250 | 0 | 0 | 1 |
| How long will my parcel be held at the pick-up point before being sent back? | good | 1.000 | 1 | 1 | 1 |
| What should I do if I'm unsure about my parcel status? | adversarial | 0.500 | 1 | 0 | 0 |
| What should I do if I'm unsure about my parcel status? | bad | 0.000 | 0 | 0 | 1 |
| What should I do if I'm unsure about my parcel status? | good | 1.000 | 1 | 1 | 1 |
| What happens if the parcel locker has no available space for my package? | adversarial | 0.250 | 0 | 0 | 1 |
| What happens if the parcel locker has no available space for my package? | bad | 0.250 | 0 | 0 | 1 |
| What happens if the parcel locker has no available space for my package? | good | 1.000 | 1 | 1 | 1 |
| Can I open a Discussion for a purchase made more than two years ago? | adversarial | 0.500 | 1 | 0 | 0 |
| Can I open a Discussion for a purchase made more than two years ago? | bad | 0.250 | 0 | 0 | 1 |
| Can I open a Discussion for a purchase made more than two years ago? | good | 1.000 | 1 | 1 | 1 |
| How can I collect my parcel from a parcel locker using a pick-up code or the HopShop app? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I collect my parcel from a parcel locker using a pick-up code or the HopShop app? | bad | 0.000 | 0 | 0 | 1 |
| How can I collect my parcel from a parcel locker using a pick-up code or the HopShop app? | good | 1.000 | 1 | 1 | 1 |
| How can I share my HopShop Delivery pick-up code with someone else using the app? | adversarial | 0.750 | 1 | 0 | 0 |
| How can I share my HopShop Delivery pick-up code with someone else using the app? | bad | 0.250 | 0 | 0 | 1 |
| How can I share my HopShop Delivery pick-up code with someone else using the app? | good | 1.000 | 1 | 1 | 1 |
| How long does it take to get a refund to my bank account if I used a debit card? | adversarial | 0.500 | 1 | 0 | 0 |
| How long does it take to get a refund to my bank account if I used a debit card? | bad | 0.250 | 0 | 0 | 1 |
| How long does it take to get a refund to my bank account if I used a debit card? | good | 1.000 | 1 | 1 | 1 |
| How can I track my HopShop Delivery parcel and know when it's ready for collection? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I track my HopShop Delivery parcel and know when it's ready for collection? | bad | 0.250 | 0 | 0 | 1 |
| How can I track my HopShop Delivery parcel and know when it's ready for collection? | good | 1.000 | 1 | 1 | 1 |
| How can I find out which delivery options are available for an item on HopShop? | adversarial | 1.000 | 1 | 0 | 0 |
| How can I find out which delivery options are available for an item on HopShop? | bad | 0.250 | 0 | 0 | 1 |
| How can I find out which delivery options are available for an item on HopShop? | good | 1.000 | 1 | 1 | 1 |
| Can I withdraw from the agreement if my account is older than 14 days? | adversarial | 0.250 | 0 | 0 | 1 |
| Can I withdraw from the agreement if my account is older than 14 days? | bad | 0.000 | 0 | 0 | 1 |
| Can I withdraw from the agreement if my account is older than 14 days? | good | 1.000 | 1 | 1 | 1 |
| How can I make a purchase or set up recurring orders on HopShop? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I make a purchase or set up recurring orders on HopShop? | bad | 0.250 | 0 | 0 | 1 |
| How can I make a purchase or set up recurring orders on HopShop? | good | 1.000 | 1 | 1 | 1 |
| Can I split payment for multiple orders from different sellers? | adversarial | 0.250 | 0 | 0 | 1 |
| Can I split payment for multiple orders from different sellers? | bad | 0.250 | 0 | 0 | 1 |
| Can I split payment for multiple orders from different sellers? | good | 1.000 | 1 | 1 | 1 |
| How long does a seller have to respond to my complaint before it is considered upheld? | adversarial | 0.500 | 1 | 0 | 0 |
| How long does a seller have to respond to my complaint before it is considered upheld? | bad | 0.250 | 0 | 0 | 1 |
| How long does a seller have to respond to my complaint before it is considered upheld? | good | 1.000 | 1 | 1 | 1 |
| How can I enable sign-in with my email and password? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I enable sign-in with my email and password? | bad | 0.500 | 1 | 0 | 0 |
| How can I enable sign-in with my email and password? | good | 1.000 | 1 | 1 | 1 |
| What are the ways to contact a seller on HopShop? | adversarial | 0.500 | 1 | 0 | 0 |
| What are the ways to contact a seller on HopShop? | bad | 0.000 | 0 | 0 | 1 |
| What are the ways to contact a seller on HopShop? | good | 1.000 | 1 | 1 | 1 |
| Where can I find the estimated delivery time for an offer? | adversarial | 1.000 | 1 | 0 | 0 |
| Where can I find the estimated delivery time for an offer? | bad | 0.000 | 0 | 0 | 1 |
| Where can I find the estimated delivery time for an offer? | good | 1.000 | 1 | 1 | 1 |
| Can I combine shipping costs when buying multiple items from different sellers? | adversarial | 0.250 | 0 | 0 | 1 |
| Can I combine shipping costs when buying multiple items from different sellers? | bad | 0.000 | 0 | 0 | 1 |
| Can I combine shipping costs when buying multiple items from different sellers? | good | 1.000 | 1 | 1 | 1 |
| What are the ways to register for a HopShop account? | adversarial | 0.500 | 1 | 0 | 0 |
| What are the ways to register for a HopShop account? | bad | 0.000 | 0 | 0 | 1 |
| What are the ways to register for a HopShop account? | good | 1.000 | 1 | 1 | 1 |
| Why isn't my usual pick-up point showing on the delivery map? | adversarial | 0.500 | 1 | 0 | 0 |
| Why isn't my usual pick-up point showing on the delivery map? | bad | 0.500 | 1 | 0 | 0 |
| Why isn't my usual pick-up point showing on the delivery map? | good | 1.000 | 1 | 1 | 1 |
| Why is my payment still pending after I paid by wire transfer through a third party? | adversarial | 0.500 | 1 | 0 | 0 |
| Why is my payment still pending after I paid by wire transfer through a third party? | bad | 0.500 | 1 | 0 | 0 |
| Why is my payment still pending after I paid by wire transfer through a third party? | good | 1.000 | 1 | 1 | 1 |
| What should I do if the product I received is defective? | adversarial | 0.000 | 0 | 0 | 1 |
| What should I do if the product I received is defective? | bad | 0.000 | 0 | 0 | 1 |
| What should I do if the product I received is defective? | good | 0.000 | 0 | 1 | 0 |
| How long does it take to get a refund on my credit card for a Mastercard or Visa? | adversarial | 0.500 | 1 | 0 | 0 |
| How long does it take to get a refund on my credit card for a Mastercard or Visa? | bad | 0.000 | 0 | 0 | 1 |
| How long does it take to get a refund on my credit card for a Mastercard or Visa? | good | 1.000 | 1 | 1 | 1 |
| What situations allow me to file a complaint about your delivery service? | adversarial | 0.500 | 1 | 0 | 0 |
| What situations allow me to file a complaint about your delivery service? | bad | 0.250 | 0 | 0 | 1 |
| What situations allow me to file a complaint about your delivery service? | good | 1.000 | 1 | 1 | 1 |
| How do I close my HopShop account? | adversarial | 0.500 | 1 | 0 | 0 |
| How do I close my HopShop account? | bad | 0.000 | 0 | 0 | 1 |
| How do I close my HopShop account? | good | 1.000 | 1 | 1 | 1 |
| Do I have to use the original packaging or include the receipt when sending a product back for a complaint? | adversarial | 0.000 | 0 | 0 | 1 |
| Do I have to use the original packaging or include the receipt when sending a product back for a complaint? | bad | 0.000 | 0 | 0 | 1 |
| Do I have to use the original packaging or include the receipt when sending a product back for a complaint? | good | 1.000 | 1 | 1 | 1 |
| How can I change the delivery date before my order is dispatched? | adversarial | 0.500 | 1 | 0 | 0 |
| How can I change the delivery date before my order is dispatched? | bad | 0.250 | 0 | 0 | 1 |
| How can I change the delivery date before my order is dispatched? | good | 1.000 | 1 | 1 | 1 |
| What should I do if my order delivery is delayed and I can't contact the seller? | adversarial | 1.000 | 1 | 0 | 0 |
| What should I do if my order delivery is delayed and I can't contact the seller? | bad | 0.000 | 0 | 0 | 1 |
| What should I do if my order delivery is delayed and I can't contact the seller? | good | 1.000 | 1 | 1 | 1 |
