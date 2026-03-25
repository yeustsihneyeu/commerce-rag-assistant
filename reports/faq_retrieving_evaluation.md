# FAQ Retrieval Evaluation Report

Source notebook: `notebooks/08_faq_retrieve_evaluating.ipynb`

## Overview

- Evaluated questions: 50
- Mean precision: 0.105
- Mean recall: 1.000
- Mean MRR: 0.891
- Mean ndcg: 0.919
- Mean context relevance: 0.960

## Summary Tables

### Final Metrics

| row | precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- | --- |
| mean | 0.105 | 1.000 | 0.891 | 0.919 | 0.960 |

## Detailed Results

### Question 1/50

**Query:** Will I get a full refund including shipping if I return my order?

**Relevant docs:** `[83]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 83 | How much refund you can get from the seller | 0.906 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 2 | no | 77 | I have been waiting a long time for my order delivery | 0.762 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 3 | no | 93 | What to do if the seller does not issue a refund | 0.728 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 4 | no | 82 | When the seller will issue a refund | 0.676 | When the seller will issue a refund The seller has a particular deadline for issuing a refund: Cancelling a paid purchase ― if you order and pay for a purchase, and then cancel ... |
| 5 | no | 77 | I have been waiting a long time for my order delivery | 0.637 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 6 | no | 70 | Can I open a Discussion for a canceled order | 0.609 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
| 7 | no | 94 | I have received a defective product. What should I do? | 0.605 | I have received a defective product. What should I do? |
| 8 | no | 40 | I am buying many products — which delivery method should I choose? | 0.599 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 9 | no | 41 | How can I track a parcel? | 0.582 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 10 | no | 86 | A debit card | 0.574 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |

### Question 2/50

**Query:** Can I use multiple delivery addresses for one order or just one?

**Relevant docs:** `[25]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 25 | One delivery address | 0.989 | One delivery address Select one delivery address and one set of VAT invoice details for the whole order. |
| 2 | no | 7 | Can I have more than one HopShop account | 0.835 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 3 | no | 40 | I am buying many products — which delivery method should I choose? | 0.740 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 24 | How to pay for orders made from multiple sellers | 0.682 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 5 | no | 26 | How to choose a delivery option | 0.625 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 6 | no | 47 | The HopShop Delivery program — information for buyers | 0.551 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 7 | no | 48 | What you gain with HopShop Delivery | 0.525 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |
| 8 | no | 28 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.505 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 9 | no | 77 | I have been waiting a long time for my order delivery | 0.500 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 10 | no | 67 | I want to change the delivery day. What should I do? | 0.492 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |

### Question 3/50

**Query:** Why does my payment status show as canceled or pending on HopShop?

**Relevant docs:** `[33]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 33 | Why your payment is pending or canceled | 1.000 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 2 | no | 34 | Other reasons why your payment may be pending | 0.757 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 3 | no | 35 | My payment has not gone through. How to retry the payment? | 0.576 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 4 | no | 29 | Payment methods | 0.458 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 5 | no | 71 | How to open a Discussion for a canceled order | 0.449 | How to open a Discussion for a canceled order If you have paid for your order through HopShop Finance, you can open a Discussion by yourself. You can do it in the Purchase Histo... |
| 6 | no | 42 | Where to check the parcel tracking number and delivery status | 0.445 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the ... |
| 7 | no | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.426 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |
| 8 | no | 32 | HopShop gift cards | 0.396 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 9 | no | 30 | How to split the payment | 0.359 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.355 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |

### Question 4/50

**Query:** How can I find the seller's email and phone number after I make a purchase?

**Relevant docs:** `[21]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 21 | The seller's contact information | 1.000 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 2 | no | 41 | How can I track a parcel? | 0.761 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 3 | no | 67 | I want to change the delivery day. What should I do? | 0.725 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 4 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.675 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 5 | no | 77 | I have been waiting a long time for my order delivery | 0.648 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.574 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 7 | no | 20 | Ask a question the seller | 0.562 | Ask a question the seller If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, ... |
| 8 | no | 42 | Where to check the parcel tracking number and delivery status | 0.559 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the ... |
| 9 | no | 68 | The pick-up code does not work. What should I do? | 0.554 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 10 | no | 84 | How you will learn about the refund | 0.507 | How you will learn about the refund We will let you know by email when the seller issues the refund. In the email, you will find information about the purchase which the refund ... |

### Question 5/50

**Query:** What should I do if my parcel was damaged when I picked it up?

**Relevant docs:** `[69]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 69 | The parcel is damaged. What should I do? | 1.000 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 2 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.736 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 3 | no | 68 | The pick-up code does not work. What should I do? | 0.703 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 4 | no | 94 | I have received a defective product. What should I do? | 0.678 | I have received a defective product. What should I do? |
| 5 | no | 67 | I want to change the delivery day. What should I do? | 0.621 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.507 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 60 | For what reasons you can file a complaint about the service | 0.433 | For what reasons you can file a complaint about the service You can file a complaint if: the parcel goes missing the parcel is damaged in transit we do not perform the service o... |
| 8 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.428 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 9 | no | 41 | How can I track a parcel? | 0.422 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 10 | no | 74 | What you should do if you do not receive your order | 0.419 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |

### Question 6/50

**Query:** How do I sign up using my Google or Facebook account?

**Relevant docs:** `[3]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 3 | How to register with Google or Facebook account | 1.000 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 2 | no | 1 | How to register on HopShop | 0.478 | How to register on HopShop If you want to be an active user of HopShop, register in a few simple steps. It is free of charge. Check how to register with an email address with a ... |
| 3 | no | 7 | Can I have more than one HopShop account | 0.339 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 4 | no | 2 | How to register with an email | 0.337 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 5 | no | 4 | Signing in with a password and email address | 0.310 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Passwo... |
| 6 | no | 68 | The pick-up code does not work. What should I do? | 0.304 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 7 | no | 5 | How to register with your phone number | 0.301 | How to register with your phone number Open the registration page. Select whether you want to create a regular or business account. Select Contact number and enter your phone nu... |
| 8 | no | 54 | How to share the pick-up code with others | 0.292 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |
| 9 | no | 10 | How to withdraw from the agreement | 0.287 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 10 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.280 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |

### Question 7/50

**Query:** How can I find my parcel's tracking number and check its delivery status on HopShop?

**Relevant docs:** `[42]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 42 | Where to check the parcel tracking number and delivery status | 1.000 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the ... |
| 2 | no | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.829 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |
| 3 | no | 41 | How can I track a parcel? | 0.754 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 4 | no | 77 | I have been waiting a long time for my order delivery | 0.601 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | no | 50 | How to order a parcel with HopShop Delivery | 0.557 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 6 | no | 59 | How to file a complaint about an HopShop Delivery parcel | 0.553 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |
| 7 | no | 58 | How to return an HopShop Delivery parcel | 0.477 | How to return an HopShop Delivery parcel You can do it in several ways: within Smart! free of charge outside Smart! free of charge with the payable DPD and InPost return options... |
| 8 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.454 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 9 | no | 47 | The HopShop Delivery program — information for buyers | 0.445 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 10 | no | 49 | How much HopShop Delivery is | 0.440 | How much HopShop Delivery is Delivery within HopShop Smart! is free of charge. See the parcel prices outside HopShop Smart! in the table below: You can pay on delivery if a sell... |

### Question 8/50

**Query:** How will I receive my refund from the seller?

**Relevant docs:** `[85]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 83 | How much refund you can get from the seller | 1.000 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 2 | yes | 85 | How the seller will refund you | 0.851 | How the seller will refund you The refund method depends on the payment method you chose for your purchase. Keep reading to learn how the refund works for each method. |
| 3 | no | 82 | When the seller will issue a refund | 0.790 | When the seller will issue a refund The seller has a particular deadline for issuing a refund: Cancelling a paid purchase ― if you order and pay for a purchase, and then cancel ... |
| 4 | no | 84 | How you will learn about the refund | 0.782 | How you will learn about the refund We will let you know by email when the seller issues the refund. In the email, you will find information about the purchase which the refund ... |
| 5 | no | 93 | What to do if the seller does not issue a refund | 0.693 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.670 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 77 | I have been waiting a long time for my order delivery | 0.646 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 8 | no | 81 | How to open a Discussion | 0.597 | How to open a Discussion In the Purchase History tab, select the order for which you want to open a Discussion. Go to purchase details and click [report purchase problems]. In t... |
| 9 | no | 74 | What you should do if you do not receive your order | 0.573 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |
| 10 | no | 86 | A debit card | 0.570 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |

### Question 9/50

**Query:** How long does it take to get a refund for a wire transfer, and what if I used a postal order?

**Relevant docs:** `[91]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 91 | Wire transfer | 1.000 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email y... |
| 2 | no | 89 | Bank transfer | 0.578 | Bank transfer You will get the refund to the bank account you paid from for your purchase. You will be refunded within 3 business days. For the majority of banks, you will see t... |
| 3 | no | 93 | What to do if the seller does not issue a refund | 0.520 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 4 | no | 77 | I have been waiting a long time for my order delivery | 0.502 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | no | 34 | Other reasons why your payment may be pending | 0.453 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 6 | no | 83 | How much refund you can get from the seller | 0.448 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 7 | no | 86 | A debit card | 0.434 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.430 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 9 | no | 87 | A credit card | 0.398 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business ... |
| 10 | no | 90 | BLIK | 0.379 | BLIK You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase.... |

### Question 10/50

**Query:** How is the estimated delivery time calculated on HopShop?

**Relevant docs:** `[43]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 43 | Estimated delivery time | 1.000 | Estimated delivery time For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your... |
| 2 | no | 44 | How we calculate the estimated delivery time | 0.876 | How we calculate the estimated delivery time A dedicated algorithm calculates it based on the previous parcels of a given seller and carriers' deliveries. |
| 3 | no | 45 | The estimated delivery time may differ from the actual delivery time | 0.823 | The estimated delivery time may differ from the actual delivery time We calculate the estimated delivery time based on the available data. It may differ from the actual delivery... |
| 4 | no | 46 | Where you can see the estimated delivery time | 0.779 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |
| 5 | no | 50 | How to order a parcel with HopShop Delivery | 0.629 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 6 | no | 37 | What is the delivery time? | 0.625 | What is the delivery time? The estimated delivery time is usually a few days. We provide it separately for each offer as a specific date, a date range, or a number of days in mu... |
| 7 | no | 49 | How much HopShop Delivery is | 0.606 | How much HopShop Delivery is Delivery within HopShop Smart! is free of charge. See the parcel prices outside HopShop Smart! in the table below: You can pay on delivery if a sell... |
| 8 | no | 47 | The HopShop Delivery program — information for buyers | 0.561 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 9 | no | 36 | Delivery options on HopShop | 0.551 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 10 | no | 48 | What you gain with HopShop Delivery | 0.538 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |

### Question 11/50

**Query:** What happens to my gift card if I return an order I paid for with it?

**Relevant docs:** `[92]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 92 | A gift card | 1.000 | A gift card If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to ma... |
| 2 | no | 32 | HopShop gift cards | 0.597 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 3 | no | 77 | I have been waiting a long time for my order delivery | 0.587 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 4 | no | 86 | A debit card | 0.529 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |
| 5 | no | 70 | Can I open a Discussion for a canceled order | 0.500 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
| 6 | no | 94 | I have received a defective product. What should I do? | 0.498 | I have received a defective product. What should I do? |
| 7 | no | 77 | I have been waiting a long time for my order delivery | 0.473 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 8 | no | 68 | The pick-up code does not work. What should I do? | 0.461 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 9 | no | 67 | I want to change the delivery day. What should I do? | 0.453 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 10 | no | 87 | A credit card | 0.447 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business ... |

### Question 12/50

**Query:** How can I reorder a single product from my past purchases?

**Relevant docs:** `[16]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 16 | How to buy again a single product | 1.000 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 2 | no | 15 | How to buy a product on HopShop | 0.825 | to buy the same product or all products from an order again On HopShop, you can buy the same products again without having to look them up each time. You can buy again a single ... |
| 3 | no | 17 | How to buy again all products from a previous order | 0.743 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the p... |
| 4 | no | 18 | How to make recurring purchases | 0.672 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the ... |
| 5 | no | 15 | How to buy a product on HopShop | 0.600 | How to buy a product on HopShop 1. Find the product you need Use the search engine to find the product you are looking for. You can use sorting options and filters to better mat... |
| 6 | no | 35 | My payment has not gone through. How to retry the payment? | 0.525 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 7 | no | 14 | How to buy on HopShop | 0.511 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.503 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 9 | no | 41 | How can I track a parcel? | 0.451 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 10 | no | 79 | What if you resign from purchases repeatedly | 0.449 | What if you resign from purchases repeatedly If you have failed to pay for the purchase or collect a POD parcel again ― the seller may think you do this on purpose and ask us fo... |

### Question 13/50

**Query:** How will I be notified when my refund is processed?

**Relevant docs:** `[84]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 84 | How you will learn about the refund | 0.985 | How you will learn about the refund We will let you know by email when the seller issues the refund. In the email, you will find information about the purchase which the refund ... |
| 2 | no | 85 | How the seller will refund you | 0.746 | How the seller will refund you The refund method depends on the payment method you chose for your purchase. Keep reading to learn how the refund works for each method. |
| 3 | no | 82 | When the seller will issue a refund | 0.741 | When the seller will issue a refund The seller has a particular deadline for issuing a refund: Cancelling a paid purchase ― if you order and pay for a purchase, and then cancel ... |
| 4 | no | 77 | I have been waiting a long time for my order delivery | 0.682 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | no | 83 | How much refund you can get from the seller | 0.634 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 6 | no | 88 | Refund and card block | 0.607 | Refund and card block If your card has been blocked, restricted, or deactivated, the refund will go to the bank's technical account. In order to recover the money, contact your ... |
| 7 | no | 35 | My payment has not gone through. How to retry the payment? | 0.561 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 8 | no | 90 | BLIK | 0.532 | BLIK You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase.... |
| 9 | no | 87 | A credit card | 0.529 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business ... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.527 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |

### Question 14/50

**Query:** How can I open a Discussion if I canceled an order paid through HopShop Finance and haven’t received a refund?

**Relevant docs:** `[71]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 71 | How to open a Discussion for a canceled order | 0.969 | How to open a Discussion for a canceled order If you have paid for your order through HopShop Finance, you can open a Discussion by yourself. You can do it in the Purchase Histo... |
| 2 | no | 70 | Can I open a Discussion for a canceled order | 0.894 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
| 3 | no | 81 | How to open a Discussion | 0.650 | How to open a Discussion In the Purchase History tab, select the order for which you want to open a Discussion. Go to purchase details and click [report purchase problems]. In t... |
| 4 | no | 77 | I have been waiting a long time for my order delivery | 0.614 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | no | 77 | I have been waiting a long time for my order delivery | 0.523 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 6 | no | 33 | Why your payment is pending or canceled | 0.518 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 7 | no | 76 | Discussion time frames | 0.496 | Discussion time frames 1 hour after the purchase ― the buyer can open the Discussion 24 hours ― this is how much time the seller has to reply to the buyer’s discussion (excludin... |
| 8 | no | 93 | What to do if the seller does not issue a refund | 0.488 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 9 | no | 35 | My payment has not gone through. How to retry the payment? | 0.465 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 10 | no | 75 | If the issue still has not been resolved or the seller does not reply to your messages | 0.464 | If the issue still has not been resolved or the seller does not reply to your messages open a Discussion. You can do it 1 hour after the purchase at the earliest, and 2 years af... |

### Question 15/50

**Query:** Why might my actual delivery time be different from the estimated delivery time?

**Relevant docs:** `[45]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 45 | The estimated delivery time may differ from the actual delivery time | 1.000 | The estimated delivery time may differ from the actual delivery time We calculate the estimated delivery time based on the available data. It may differ from the actual delivery... |
| 2 | no | 46 | Where you can see the estimated delivery time | 0.686 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |
| 3 | no | 43 | Estimated delivery time | 0.658 | Estimated delivery time For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your... |
| 4 | no | 44 | How we calculate the estimated delivery time | 0.617 | How we calculate the estimated delivery time A dedicated algorithm calculates it based on the previous parcels of a given seller and carriers' deliveries. |
| 5 | no | 37 | What is the delivery time? | 0.594 | What is the delivery time? The estimated delivery time is usually a few days. We provide it separately for each offer as a specific date, a date range, or a number of days in mu... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.481 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.388 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.350 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 9 | no | 34 | Other reasons why your payment may be pending | 0.346 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 10 | no | 67 | I want to change the delivery day. What should I do? | 0.342 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |

### Question 16/50

**Query:** Who is responsible if an item is damaged during delivery when buying from an entrepreneur?

**Relevant docs:** `[72]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 72 | Consumer purchase from an entrepreneur | 1.000 | Consumer purchase from an entrepreneur If a consumer buys an item from an entrepreneur, then the entrepreneur (in this case: the seller) is responsible for the risk of the item ... |
| 2 | no | 97 | Consumer sales (when a consumer buys from an entrepreneur) | 0.717 | Consumer sales (when a consumer buys from an entrepreneur) If you receive a product that does not conform to the contract, you can file a complaint. The entrepreneur is liable f... |
| 3 | no | 73 | Purchases from private individuals or transactions between entrepreneurs | 0.706 | Purchases from private individuals or transactions between entrepreneurs If a buyer purchases an item from a private individual or if both sides of the transaction act as entrep... |
| 4 | no | 69 | The parcel is damaged. What should I do? | 0.474 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 5 | no | 40 | I am buying many products — which delivery method should I choose? | 0.437 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 6 | no | 60 | For what reasons you can file a complaint about the service | 0.370 | For what reasons you can file a complaint about the service You can file a complaint if: the parcel goes missing the parcel is damaged in transit we do not perform the service o... |
| 7 | no | 83 | How much refund you can get from the seller | 0.343 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 8 | no | 36 | Delivery options on HopShop | 0.321 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 9 | no | 77 | I have been waiting a long time for my order delivery | 0.298 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.293 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |

### Question 17/50

**Query:** What should I do if my pick-up code isn’t working at the parcel locker?

**Relevant docs:** `[68]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 68 | The pick-up code does not work. What should I do? | 1.000 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 2 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.798 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 3 | no | 53 | When you receive a pick-up code | 0.623 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 4 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.602 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 5 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.602 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 6 | no | 69 | The parcel is damaged. What should I do? | 0.585 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 7 | no | 56 | How to collect a parcel from a parcel locker | 0.573 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 8 | no | 65 | What if the parcel locker is full? | 0.553 | What if the parcel locker is full? We will redirect your parcel to a different parcel locker or pick-up point and send you a notification. |
| 9 | no | 55 | How to collect a parcel from a pick-up point | 0.547 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 10 | no | 54 | How to share the pick-up code with others | 0.533 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |

### Question 18/50

**Query:** What happens if I frequently cancel or don't pay for my purchases on HopShop?

**Relevant docs:** `[79]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 79 | What if you resign from purchases repeatedly | 1.000 | What if you resign from purchases repeatedly If you have failed to pay for the purchase or collect a POD parcel again ― the seller may think you do this on purpose and ask us fo... |
| 2 | no | 35 | My payment has not gone through. How to retry the payment? | 0.811 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 3 | no | 77 | I have been waiting a long time for my order delivery | 0.660 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 4 | no | 77 | I have been waiting a long time for my order delivery | 0.641 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | no | 12 | How to terminate the agreement | 0.636 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the accou... |
| 6 | no | 13 | What you should do before the notice period ends | 0.625 | What you should do before the notice period ends Pay any arrears to HopShop. If you have an open invoice account ― settle the balance on the HopShop account, and close it in the... |
| 7 | no | 7 | Can I have more than one HopShop account | 0.607 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 8 | no | 32 | HopShop gift cards | 0.596 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 9 | no | 29 | Payment methods | 0.574 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 10 | no | 14 | How to buy on HopShop | 0.568 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |

### Question 19/50

**Query:** What do I need to do to pick up my parcel from a pick-up point?

**Relevant docs:** `[55]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 55 | How to collect a parcel from a pick-up point | 0.891 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 2 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.854 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 3 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.761 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 4 | no | 68 | The pick-up code does not work. What should I do? | 0.739 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 5 | no | 53 | When you receive a pick-up code | 0.666 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 6 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.661 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 7 | no | 69 | The parcel is damaged. What should I do? | 0.610 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 8 | no | 56 | How to collect a parcel from a parcel locker | 0.553 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 9 | no | 54 | How to share the pick-up code with others | 0.518 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |
| 10 | no | 57 | How much time you have to collect a parcel | 0.483 | How much time you have to collect a parcel The parcel will wait for you for: 2 working days — in HopShop One pick-up points and parcel lockers 3 working days — in ORLEN Paczka p... |

### Question 20/50

**Query:** How long does it take to get a BLIK refund and where can I see it in my bank account?

**Relevant docs:** `[90]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 90 | BLIK | 1.000 | BLIK You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase.... |
| 2 | no | 89 | Bank transfer | 0.700 | Bank transfer You will get the refund to the bank account you paid from for your purchase. You will be refunded within 3 business days. For the majority of banks, you will see t... |
| 3 | no | 86 | A debit card | 0.592 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |
| 4 | no | 87 | A credit card | 0.578 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business ... |
| 5 | no | 77 | I have been waiting a long time for my order delivery | 0.535 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 6 | no | 83 | How much refund you can get from the seller | 0.532 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 7 | no | 46 | Where you can see the estimated delivery time | 0.509 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |
| 8 | no | 91 | Wire transfer | 0.505 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email y... |
| 9 | no | 88 | Refund and card block | 0.494 | Refund and card block If your card has been blocked, restricted, or deactivated, the refund will go to the bank's technical account. In order to recover the money, contact your ... |
| 10 | no | 93 | What to do if the seller does not issue a refund | 0.465 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |

### Question 21/50

**Query:** How do I pay for my order using PayPal and how does currency conversion work?

**Relevant docs:** `[31]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 31 | How to pay with PayPal | 1.000 | How to pay with PayPal When you are ready to pay for your order, go to the delivery and payment form. In the Payment method section, select PayPal. Click [buy and pay]. You will... |
| 2 | no | 30 | How to split the payment | 0.561 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |
| 3 | no | 77 | I have been waiting a long time for my order delivery | 0.539 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 4 | no | 68 | The pick-up code does not work. What should I do? | 0.520 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 5 | no | 24 | How to pay for orders made from multiple sellers | 0.478 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.436 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 35 | My payment has not gone through. How to retry the payment? | 0.428 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 8 | no | 28 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.422 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 9 | no | 40 | I am buying many products — which delivery method should I choose? | 0.359 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 10 | no | 41 | How can I track a parcel? | 0.348 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 22/50

**Query:** How can I change my parcel locker or pick-up point before the seller ships my order?

**Relevant docs:** `[66]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.984 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 2 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.819 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 3 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.665 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 4 | no | 68 | The pick-up code does not work. What should I do? | 0.538 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 5 | no | 67 | I want to change the delivery day. What should I do? | 0.535 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 6 | no | 55 | How to collect a parcel from a pick-up point | 0.518 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 7 | no | 65 | What if the parcel locker is full? | 0.486 | What if the parcel locker is full? We will redirect your parcel to a different parcel locker or pick-up point and send you a notification. |
| 8 | no | 56 | How to collect a parcel from a parcel locker | 0.465 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 9 | no | 53 | When you receive a pick-up code | 0.451 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.449 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |

### Question 23/50

**Query:** What are the options for returning a HopShop Delivery parcel?

**Relevant docs:** `[58]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 36 | Delivery options on HopShop | 0.899 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 2 | yes | 58 | How to return an HopShop Delivery parcel | 0.828 | How to return an HopShop Delivery parcel You can do it in several ways: within Smart! free of charge outside Smart! free of charge with the payable DPD and InPost return options... |
| 3 | no | 47 | The HopShop Delivery program — information for buyers | 0.747 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 4 | no | 48 | What you gain with HopShop Delivery | 0.712 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |
| 5 | no | 50 | How to order a parcel with HopShop Delivery | 0.699 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 6 | no | 61 | What are the maximum dimensions and weight of an HopShop Delivery parcel? | 0.680 | What are the maximum dimensions and weight of an HopShop Delivery parcel? You can order parcels up to 20 kg, with maximum dimensions: 41 cm x 38 cm x 64 cm to pick-up points and... |
| 7 | no | 56 | How to collect a parcel from a parcel locker | 0.607 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 8 | no | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.581 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |
| 9 | no | 59 | How to file a complaint about an HopShop Delivery parcel | 0.574 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |
| 10 | no | 49 | How much HopShop Delivery is | 0.563 | How much HopShop Delivery is Delivery within HopShop Smart! is free of charge. See the parcel prices outside HopShop Smart! in the table below: You can pay on delivery if a sell... |

### Question 24/50

**Query:** How long will my parcel be held at the pick-up point before being sent back?

**Relevant docs:** `[57]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 0.333 | 0.500 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.802 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 2 | no | 55 | How to collect a parcel from a pick-up point | 0.788 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 3 | yes | 57 | How much time you have to collect a parcel | 0.766 | How much time you have to collect a parcel The parcel will wait for you for: 2 working days — in HopShop One pick-up points and parcel lockers 3 working days — in ORLEN Paczka p... |
| 4 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.686 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 5 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.640 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 6 | no | 53 | When you receive a pick-up code | 0.583 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 7 | no | 65 | What if the parcel locker is full? | 0.522 | What if the parcel locker is full? We will redirect your parcel to a different parcel locker or pick-up point and send you a notification. |
| 8 | no | 68 | The pick-up code does not work. What should I do? | 0.508 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 9 | no | 54 | How to share the pick-up code with others | 0.506 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.474 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |

### Question 25/50

**Query:** What should I do if I'm unsure about my parcel status?

**Relevant docs:** `[52]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 0.200 | 0.387 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.808 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 2 | no | 67 | I want to change the delivery day. What should I do? | 0.786 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 3 | no | 69 | The parcel is damaged. What should I do? | 0.765 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 4 | no | 68 | The pick-up code does not work. What should I do? | 0.738 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 5 | yes | 52 | If the parcel status is not clear | 0.733 | If the parcel status is not clear If you have any doubts regarding what your parcel status means — click [contact us] below this article. |
| 6 | no | 94 | I have received a defective product. What should I do? | 0.707 | I have received a defective product. What should I do? |
| 7 | no | 77 | I have been waiting a long time for my order delivery | 0.678 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 8 | no | 41 | How can I track a parcel? | 0.627 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 9 | no | 74 | What you should do if you do not receive your order | 0.624 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |
| 10 | no | 42 | Where to check the parcel tracking number and delivery status | 0.569 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the ... |

### Question 26/50

**Query:** What happens if the parcel locker has no available space for my package?

**Relevant docs:** `[65]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 65 | What if the parcel locker is full? | 0.972 | What if the parcel locker is full? We will redirect your parcel to a different parcel locker or pick-up point and send you a notification. |
| 2 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.777 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 3 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.761 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 4 | no | 69 | The parcel is damaged. What should I do? | 0.673 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 5 | no | 56 | How to collect a parcel from a parcel locker | 0.635 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 6 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.593 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 7 | no | 68 | The pick-up code does not work. What should I do? | 0.568 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 8 | no | 35 | My payment has not gone through. How to retry the payment? | 0.462 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 9 | no | 77 | I have been waiting a long time for my order delivery | 0.447 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 10 | no | 61 | What are the maximum dimensions and weight of an HopShop Delivery parcel? | 0.443 | What are the maximum dimensions and weight of an HopShop Delivery parcel? You can order parcels up to 20 kg, with maximum dimensions: 41 cm x 38 cm x 64 cm to pick-up points and... |

### Question 27/50

**Query:** Can I open a Discussion for a purchase made more than two years ago?

**Relevant docs:** `[80]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 70 | Can I open a Discussion for a canceled order | 0.794 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
| 2 | yes | 80 | Check the Discussion time frame | 0.793 | Check the Discussion time frame If 2 years (730 days) have passed from making the purchase, it is impossible to open a Discussion. If your order included a purchase in several o... |
| 3 | no | 71 | How to open a Discussion for a canceled order | 0.701 | How to open a Discussion for a canceled order If you have paid for your order through HopShop Finance, you can open a Discussion by yourself. You can do it in the Purchase Histo... |
| 4 | no | 81 | How to open a Discussion | 0.687 | How to open a Discussion In the Purchase History tab, select the order for which you want to open a Discussion. Go to purchase details and click [report purchase problems]. In t... |
| 5 | no | 76 | Discussion time frames | 0.617 | Discussion time frames 1 hour after the purchase ― the buyer can open the Discussion 24 hours ― this is how much time the seller has to reply to the buyer’s discussion (excludin... |
| 6 | no | 7 | Can I have more than one HopShop account | 0.598 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 7 | no | 75 | If the issue still has not been resolved or the seller does not reply to your messages | 0.574 | If the issue still has not been resolved or the seller does not reply to your messages open a Discussion. You can do it 1 hour after the purchase at the earliest, and 2 years af... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.528 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 9 | no | 77 | I have been waiting a long time for my order delivery | 0.524 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 10 | no | 79 | What if you resign from purchases repeatedly | 0.517 | What if you resign from purchases repeatedly If you have failed to pay for the purchase or collect a POD parcel again ― the seller may think you do this on purpose and ask us fo... |

### Question 28/50

**Query:** How can I collect my parcel from a parcel locker using a pick-up code or the HopShop app?

**Relevant docs:** `[56]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 56 | How to collect a parcel from a parcel locker | 1.000 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 2 | no | 55 | How to collect a parcel from a pick-up point | 0.781 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 3 | no | 54 | How to share the pick-up code with others | 0.769 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |
| 4 | no | 53 | When you receive a pick-up code | 0.766 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 5 | no | 68 | The pick-up code does not work. What should I do? | 0.694 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 6 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.682 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 7 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.642 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 8 | no | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 0.604 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 9 | no | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.590 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |
| 10 | no | 57 | How much time you have to collect a parcel | 0.544 | How much time you have to collect a parcel The parcel will wait for you for: 2 working days — in HopShop One pick-up points and parcel lockers 3 working days — in ORLEN Paczka p... |

### Question 29/50

**Query:** How can I share my HopShop Delivery pick-up code with someone else using the app?

**Relevant docs:** `[54]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 54 | How to share the pick-up code with others | 1.000 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |
| 2 | no | 53 | When you receive a pick-up code | 0.614 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 3 | no | 68 | The pick-up code does not work. What should I do? | 0.546 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 4 | no | 56 | How to collect a parcel from a parcel locker | 0.498 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 5 | no | 47 | The HopShop Delivery program — information for buyers | 0.440 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 6 | no | 48 | What you gain with HopShop Delivery | 0.422 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |
| 7 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.406 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 8 | no | 55 | How to collect a parcel from a pick-up point | 0.405 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 9 | no | 50 | How to order a parcel with HopShop Delivery | 0.404 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 10 | no | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.399 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |

### Question 30/50

**Query:** How long does it take to get a refund to my bank account if I used a debit card?

**Relevant docs:** `[86]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 86 | A debit card | 1.000 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |
| 2 | no | 87 | A credit card | 0.725 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business ... |
| 3 | no | 88 | Refund and card block | 0.662 | Refund and card block If your card has been blocked, restricted, or deactivated, the refund will go to the bank's technical account. In order to recover the money, contact your ... |
| 4 | no | 89 | Bank transfer | 0.656 | Bank transfer You will get the refund to the bank account you paid from for your purchase. You will be refunded within 3 business days. For the majority of banks, you will see t... |
| 5 | no | 90 | BLIK | 0.563 | BLIK You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase.... |
| 6 | no | 91 | Wire transfer | 0.529 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email y... |
| 7 | no | 92 | A gift card | 0.472 | A gift card If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to ma... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.453 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 9 | no | 93 | What to do if the seller does not issue a refund | 0.445 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 10 | no | 83 | How much refund you can get from the seller | 0.427 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |

### Question 31/50

**Query:** How can I track my HopShop Delivery parcel and know when it's ready for collection?

**Relevant docs:** `[51]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 41 | How can I track a parcel? | 0.892 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 2 | yes | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.786 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |
| 3 | no | 42 | Where to check the parcel tracking number and delivery status | 0.687 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the ... |
| 4 | no | 50 | How to order a parcel with HopShop Delivery | 0.642 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 5 | no | 58 | How to return an HopShop Delivery parcel | 0.566 | How to return an HopShop Delivery parcel You can do it in several ways: within Smart! free of charge outside Smart! free of charge with the payable DPD and InPost return options... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.562 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 53 | When you receive a pick-up code | 0.561 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 8 | no | 47 | The HopShop Delivery program — information for buyers | 0.538 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 9 | no | 56 | How to collect a parcel from a parcel locker | 0.533 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the ... |
| 10 | no | 59 | How to file a complaint about an HopShop Delivery parcel | 0.533 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |

### Question 32/50

**Query:** How can I find out which delivery options are available for an item on HopShop?

**Relevant docs:** `[36]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 36 | Delivery options on HopShop | 1.000 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 2 | no | 47 | The HopShop Delivery program — information for buyers | 0.815 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 3 | no | 40 | I am buying many products — which delivery method should I choose? | 0.720 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 58 | How to return an HopShop Delivery parcel | 0.668 | How to return an HopShop Delivery parcel You can do it in several ways: within Smart! free of charge outside Smart! free of charge with the payable DPD and InPost return options... |
| 5 | no | 50 | How to order a parcel with HopShop Delivery | 0.668 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 6 | no | 49 | How much HopShop Delivery is | 0.661 | How much HopShop Delivery is Delivery within HopShop Smart! is free of charge. See the parcel prices outside HopShop Smart! in the table below: You can pay on delivery if a sell... |
| 7 | no | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.656 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |
| 8 | no | 26 | How to choose a delivery option | 0.647 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 9 | no | 15 | How to buy a product on HopShop | 0.603 | How to buy a product on HopShop 1. Find the product you need Use the search engine to find the product you are looking for. You can use sorting options and filters to better mat... |
| 10 | no | 41 | How can I track a parcel? | 0.602 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 33/50

**Query:** Can I withdraw from the agreement if my account is older than 14 days?

**Relevant docs:** `[10]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 9 | When you can withdraw from the agreement | 1.000 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account... |
| 2 | yes | 10 | How to withdraw from the agreement | 0.924 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 3 | no | 11 | When you can terminate the agreement | 0.608 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |
| 4 | no | 12 | How to terminate the agreement | 0.516 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the accou... |
| 5 | no | 7 | Can I have more than one HopShop account | 0.501 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 6 | no | 8 | How to close your HopShop account | 0.416 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 7 | no | 77 | I have been waiting a long time for my order delivery | 0.391 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.383 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 9 | no | 76 | Discussion time frames | 0.354 | Discussion time frames 1 hour after the purchase ― the buyer can open the Discussion 24 hours ― this is how much time the seller has to reply to the buyer’s discussion (excludin... |
| 10 | no | 80 | Check the Discussion time frame | 0.340 | Check the Discussion time frame If 2 years (730 days) have passed from making the purchase, it is impossible to open a Discussion. If your order included a purchase in several o... |

### Question 34/50

**Query:** How can I make a purchase or set up recurring orders on HopShop?

**Relevant docs:** `[14]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 18 | How to make recurring purchases | 0.838 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the ... |
| 2 | yes | 14 | How to buy on HopShop | 0.815 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 3 | no | 39 | How to provide shipping details? | 0.604 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |
| 4 | no | 15 | How to buy a product on HopShop | 0.602 | How to buy a product on HopShop 1. Find the product you need Use the search engine to find the product you are looking for. You can use sorting options and filters to better mat... |
| 5 | no | 32 | HopShop gift cards | 0.592 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 6 | no | 50 | How to order a parcel with HopShop Delivery | 0.581 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 7 | no | 15 | How to buy a product on HopShop | 0.575 | to buy the same product or all products from an order again On HopShop, you can buy the same products again without having to look them up each time. You can buy again a single ... |
| 8 | no | 7 | Can I have more than one HopShop account | 0.556 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 9 | no | 48 | What you gain with HopShop Delivery | 0.550 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |
| 10 | no | 1 | How to register on HopShop | 0.513 | How to register on HopShop If you want to be an active user of HopShop, register in a few simple steps. It is free of charge. Check how to register with an email address with a ... |

### Question 35/50

**Query:** Can I split payment for multiple orders from different sellers?

**Relevant docs:** `[30]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 0.500 | 0.631 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 24 | How to pay for orders made from multiple sellers | 1.000 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 2 | yes | 30 | How to split the payment | 0.728 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |
| 3 | no | 28 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.554 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 4 | no | 40 | I am buying many products — which delivery method should I choose? | 0.537 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 5 | no | 26 | How to choose a delivery option | 0.476 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 6 | no | 29 | Payment methods | 0.436 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 7 | no | 41 | How can I track a parcel? | 0.421 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 8 | no | 70 | Can I open a Discussion for a canceled order | 0.345 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
| 9 | no | 67 | I want to change the delivery day. What should I do? | 0.336 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 10 | no | 35 | My payment has not gone through. How to retry the payment? | 0.332 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |

### Question 36/50

**Query:** How long does a seller have to respond to my complaint before it is considered upheld?

**Relevant docs:** `[95]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 95 | Deadline for processing a complaint | 1.000 | Deadline for processing a complaint When the seller receives your complaint, they have 14 days to address it. If they do not do it by the due date, your complaint is considered ... |
| 2 | no | 77 | I have been waiting a long time for my order delivery | 0.728 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 3 | no | 77 | I have been waiting a long time for my order delivery | 0.695 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 4 | no | 75 | If the issue still has not been resolved or the seller does not reply to your messages | 0.588 | If the issue still has not been resolved or the seller does not reply to your messages open a Discussion. You can do it 1 hour after the purchase at the earliest, and 2 years af... |
| 5 | no | 93 | What to do if the seller does not issue a refund | 0.569 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 6 | no | 60 | For what reasons you can file a complaint about the service | 0.533 | For what reasons you can file a complaint about the service You can file a complaint if: the parcel goes missing the parcel is damaged in transit we do not perform the service o... |
| 7 | no | 59 | How to file a complaint about an HopShop Delivery parcel | 0.504 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |
| 8 | no | 76 | Discussion time frames | 0.432 | Discussion time frames 1 hour after the purchase ― the buyer can open the Discussion 24 hours ― this is how much time the seller has to reply to the buyer’s discussion (excludin... |
| 9 | no | 82 | When the seller will issue a refund | 0.412 | When the seller will issue a refund The seller has a particular deadline for issuing a refund: Cancelling a paid purchase ― if you order and pay for a purchase, and then cancel ... |
| 10 | no | 78 | Cancelling an order | 0.388 | Cancelling an order You can cancel an order in the Purchase History tab, as long as the seller: does not change your order status to: In progress, Prepared for dispatch or Sent ... |

### Question 37/50

**Query:** How can I enable sign-in with my email and password?

**Relevant docs:** `[4]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 4 | Signing in with a password and email address | 1.000 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Passwo... |
| 2 | no | 2 | How to register with an email | 0.594 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 3 | no | 3 | How to register with Google or Facebook account | 0.475 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 4 | no | 41 | How can I track a parcel? | 0.399 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 5 | no | 35 | My payment has not gone through. How to retry the payment? | 0.363 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.361 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 77 | I have been waiting a long time for my order delivery | 0.361 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 8 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.347 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 9 | no | 6 | GDPR — how you can download your personal data from the HopShop account. | 0.347 | GDPR — how you can download your personal data from the HopShop account. On the Copies of your data page, you can download the personal data gathered throughout your activity on... |
| 10 | no | 1 | How to register on HopShop | 0.339 | How to register on HopShop If you want to be an active user of HopShop, register in a few simple steps. It is free of charge. Check how to register with an email address with a ... |

### Question 38/50

**Query:** What are the ways to contact a seller on HopShop?

**Relevant docs:** `[19]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 19 | How to contact the seller | 1.000 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through th... |
| 2 | no | 21 | The seller's contact information | 0.655 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 3 | no | 20 | Ask a question the seller | 0.642 | Ask a question the seller If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, ... |
| 4 | no | 93 | What to do if the seller does not issue a refund | 0.558 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 5 | no | 32 | HopShop gift cards | 0.527 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 6 | no | 36 | Delivery options on HopShop | 0.514 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 7 | no | 22 | The Message Center | 0.500 | The Message Center If you do not want to exit the HopShop website or app, contact the seller through the Message Center. It is really easy to use, as it combines the convenience... |
| 8 | no | 14 | How to buy on HopShop | 0.493 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 9 | no | 58 | How to return an HopShop Delivery parcel | 0.483 | How to return an HopShop Delivery parcel You can do it in several ways: within Smart! free of charge outside Smart! free of charge with the payable DPD and InPost return options... |
| 10 | no | 48 | What you gain with HopShop Delivery | 0.456 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |

### Question 39/50

**Query:** Where can I find the estimated delivery time for an offer?

**Relevant docs:** `[46]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 46 | Where you can see the estimated delivery time | 1.000 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |
| 2 | no | 43 | Estimated delivery time | 0.760 | Estimated delivery time For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your... |
| 3 | no | 37 | What is the delivery time? | 0.687 | What is the delivery time? The estimated delivery time is usually a few days. We provide it separately for each offer as a specific date, a date range, or a number of days in mu... |
| 4 | no | 45 | The estimated delivery time may differ from the actual delivery time | 0.673 | The estimated delivery time may differ from the actual delivery time We calculate the estimated delivery time based on the available data. It may differ from the actual delivery... |
| 5 | no | 44 | How we calculate the estimated delivery time | 0.642 | How we calculate the estimated delivery time A dedicated algorithm calculates it based on the previous parcels of a given seller and carriers' deliveries. |
| 6 | no | 77 | I have been waiting a long time for my order delivery | 0.492 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 7 | no | 67 | I want to change the delivery day. What should I do? | 0.456 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 8 | no | 42 | Where to check the parcel tracking number and delivery status | 0.439 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the ... |
| 9 | no | 38 | How much does delivery cost? | 0.413 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packagin... |
| 10 | no | 41 | How can I track a parcel? | 0.412 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 40/50

**Query:** Can I combine shipping costs when buying multiple items from different sellers?

**Relevant docs:** `[40]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 40 | I am buying many products — which delivery method should I choose? | 1.000 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 2 | no | 24 | How to pay for orders made from multiple sellers | 0.945 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 3 | no | 26 | How to choose a delivery option | 0.652 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 4 | no | 41 | How can I track a parcel? | 0.520 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 5 | no | 39 | How to provide shipping details? | 0.488 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |
| 6 | no | 38 | How much does delivery cost? | 0.473 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packagin... |
| 7 | no | 28 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.436 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 8 | no | 83 | How much refund you can get from the seller | 0.418 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 9 | no | 67 | I want to change the delivery day. What should I do? | 0.414 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 10 | no | 73 | Purchases from private individuals or transactions between entrepreneurs | 0.379 | Purchases from private individuals or transactions between entrepreneurs If a buyer purchases an item from a private individual or if both sides of the transaction act as entrep... |

### Question 41/50

**Query:** What are the ways to register for a HopShop account?

**Relevant docs:** `[1]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 1 | How to register on HopShop | 0.998 | How to register on HopShop If you want to be an active user of HopShop, register in a few simple steps. It is free of charge. Check how to register with an email address with a ... |
| 2 | no | 3 | How to register with Google or Facebook account | 0.954 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 3 | no | 2 | How to register with an email | 0.893 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 4 | no | 5 | How to register with your phone number | 0.849 | How to register with your phone number Open the registration page. Select whether you want to create a regular or business account. Select Contact number and enter your phone nu... |
| 5 | no | 7 | Can I have more than one HopShop account | 0.714 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 6 | no | 8 | How to close your HopShop account | 0.657 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 7 | no | 5 | How to register with your phone number | 0.610 | your account within 3 business days, and return a bank transfer amount entirely to your bank account. Bank transfer - if your bank is not on the list of available banks, select ... |
| 8 | no | 14 | How to buy on HopShop | 0.545 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 9 | no | 6 | GDPR — how you can download your personal data from the HopShop account. | 0.534 | GDPR — how you can download your personal data from the HopShop account. On the Copies of your data page, you can download the personal data gathered throughout your activity on... |
| 10 | no | 48 | What you gain with HopShop Delivery | 0.522 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |

### Question 42/50

**Query:** Why isn't my usual pick-up point showing on the delivery map?

**Relevant docs:** `[63]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 1.000 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If yo... |
| 2 | no | 64 | How to find a pick-up point or parcel locker closest to my location? | 0.774 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |
| 3 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.570 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 4 | no | 55 | How to collect a parcel from a pick-up point | 0.528 | How to collect a parcel from a pick-up point When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel. |
| 5 | no | 68 | The pick-up code does not work. What should I do? | 0.512 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 6 | no | 53 | When you receive a pick-up code | 0.462 | When you receive a pick-up code You will receive the pick-up code when the parcel is ready to be collected from the parcel locker or pick-up point. You can find it: in the email... |
| 7 | no | 47 | The HopShop Delivery program — information for buyers | 0.410 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 8 | no | 54 | How to share the pick-up code with others | 0.398 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopS... |
| 9 | no | 48 | What you gain with HopShop Delivery | 0.372 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |
| 10 | no | 46 | Where you can see the estimated delivery time | 0.371 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |

### Question 43/50

**Query:** Why is my payment still pending after I paid by wire transfer through a third party?

**Relevant docs:** `[34]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 34 | Other reasons why your payment may be pending | 1.000 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 2 | no | 33 | Why your payment is pending or canceled | 0.716 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 3 | no | 91 | Wire transfer | 0.645 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email y... |
| 4 | no | 35 | My payment has not gone through. How to retry the payment? | 0.528 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 5 | no | 77 | I have been waiting a long time for my order delivery | 0.456 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 6 | no | 89 | Bank transfer | 0.427 | Bank transfer You will get the refund to the bank account you paid from for your purchase. You will be refunded within 3 business days. For the majority of banks, you will see t... |
| 7 | no | 29 | Payment methods | 0.363 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 8 | no | 28 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.355 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 9 | no | 71 | How to open a Discussion for a canceled order | 0.322 | How to open a Discussion for a canceled order If you have paid for your order through HopShop Finance, you can open a Discussion by yourself. You can do it in the Purchase Histo... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.299 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |

### Question 44/50

**Query:** What should I do if the product I received is defective?

**Relevant docs:** `[94]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 94 | I have received a defective product. What should I do? | 1.000 | I have received a defective product. What should I do? |
| 2 | no | 69 | The parcel is damaged. What should I do? | 0.427 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 3 | no | 67 | I want to change the delivery day. What should I do? | 0.396 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 4 | no | 74 | What you should do if you do not receive your order | 0.363 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |
| 5 | no | 68 | The pick-up code does not work. What should I do? | 0.355 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 6 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.340 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 7 | no | 96 | Sending a product back to the seller | 0.328 | Sending a product back to the seller If you send the product back as a part of the complaint, you should secure it properly. Usually, you are not required to return it in the or... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.300 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 9 | no | 93 | What to do if the seller does not issue a refund | 0.250 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 10 | no | 40 | I am buying many products — which delivery method should I choose? | 0.237 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |

### Question 45/50

**Query:** How long does it take to get a refund on my credit card for a Mastercard or Visa?

**Relevant docs:** `[87]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 87 | A credit card | 1.000 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business ... |
| 2 | no | 86 | A debit card | 0.765 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to th... |
| 3 | no | 88 | Refund and card block | 0.508 | Refund and card block If your card has been blocked, restricted, or deactivated, the refund will go to the bank's technical account. In order to recover the money, contact your ... |
| 4 | no | 93 | What to do if the seller does not issue a refund | 0.457 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you c... |
| 5 | no | 83 | How much refund you can get from the seller | 0.428 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you p... |
| 6 | no | 92 | A gift card | 0.409 | A gift card If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to ma... |
| 7 | no | 90 | BLIK | 0.407 | BLIK You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase.... |
| 8 | no | 91 | Wire transfer | 0.394 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email y... |
| 9 | no | 89 | Bank transfer | 0.390 | Bank transfer You will get the refund to the bank account you paid from for your purchase. You will be refunded within 3 business days. For the majority of banks, you will see t... |
| 10 | no | 77 | I have been waiting a long time for my order delivery | 0.385 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |

### Question 46/50

**Query:** What situations allow me to file a complaint about your delivery service?

**Relevant docs:** `[60]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 60 | For what reasons you can file a complaint about the service | 1.000 | For what reasons you can file a complaint about the service You can file a complaint if: the parcel goes missing the parcel is damaged in transit we do not perform the service o... |
| 2 | no | 59 | How to file a complaint about an HopShop Delivery parcel | 0.746 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |
| 3 | no | 95 | Deadline for processing a complaint | 0.486 | Deadline for processing a complaint When the seller receives your complaint, they have 14 days to address it. If they do not do it by the due date, your complaint is considered ... |
| 4 | no | 69 | The parcel is damaged. What should I do? | 0.474 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 5 | no | 74 | What you should do if you do not receive your order | 0.451 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |
| 6 | no | 67 | I want to change the delivery day. What should I do? | 0.424 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 7 | no | 77 | I have been waiting a long time for my order delivery | 0.392 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 8 | no | 97 | Consumer sales (when a consumer buys from an entrepreneur) | 0.373 | Consumer sales (when a consumer buys from an entrepreneur) If you receive a product that does not conform to the contract, you can file a complaint. The entrepreneur is liable f... |
| 9 | no | 77 | I have been waiting a long time for my order delivery | 0.361 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 10 | no | 48 | What you gain with HopShop Delivery | 0.350 | What you gain with HopShop Delivery Convenient delivery in your area — with the extensive network of 17,000 HopShop One and ORLEN Paczka parcel lockers and pick-up points. Free ... |

### Question 47/50

**Query:** How do I close my HopShop account?

**Relevant docs:** `[8]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 8 | How to close your HopShop account | 1.000 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 2 | no | 13 | What you should do before the notice period ends | 0.640 | What you should do before the notice period ends Pay any arrears to HopShop. If you have an open invoice account ― settle the balance on the HopShop account, and close it in the... |
| 3 | no | 7 | Can I have more than one HopShop account | 0.586 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 4 | no | 1 | How to register on HopShop | 0.517 | How to register on HopShop If you want to be an active user of HopShop, register in a few simple steps. It is free of charge. Check how to register with an email address with a ... |
| 5 | no | 12 | How to terminate the agreement | 0.513 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the accou... |
| 6 | no | 3 | How to register with Google or Facebook account | 0.493 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 7 | no | 6 | GDPR — how you can download your personal data from the HopShop account. | 0.490 | GDPR — how you can download your personal data from the HopShop account. On the Copies of your data page, you can download the personal data gathered throughout your activity on... |
| 8 | no | 39 | How to provide shipping details? | 0.484 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |
| 9 | no | 10 | How to withdraw from the agreement | 0.474 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 10 | no | 2 | How to register with an email | 0.468 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |

### Question 48/50

**Query:** Do I have to use the original packaging or include the receipt when sending a product back for a complaint?

**Relevant docs:** `[96]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 96 | Sending a product back to the seller | 1.000 | Sending a product back to the seller If you send the product back as a part of the complaint, you should secure it properly. Usually, you are not required to return it in the or... |
| 2 | no | 94 | I have received a defective product. What should I do? | 0.495 | I have received a defective product. What should I do? |
| 3 | no | 60 | For what reasons you can file a complaint about the service | 0.402 | For what reasons you can file a complaint about the service You can file a complaint if: the parcel goes missing the parcel is damaged in transit we do not perform the service o... |
| 4 | no | 69 | The parcel is damaged. What should I do? | 0.382 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 5 | no | 59 | How to file a complaint about an HopShop Delivery parcel | 0.375 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |
| 6 | no | 95 | Deadline for processing a complaint | 0.373 | Deadline for processing a complaint When the seller receives your complaint, they have 14 days to address it. If they do not do it by the due date, your complaint is considered ... |
| 7 | no | 97 | Consumer sales (when a consumer buys from an entrepreneur) | 0.360 | Consumer sales (when a consumer buys from an entrepreneur) If you receive a product that does not conform to the contract, you can file a complaint. The entrepreneur is liable f... |
| 8 | no | 77 | I have been waiting a long time for my order delivery | 0.266 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 9 | no | 82 | When the seller will issue a refund | 0.264 | When the seller will issue a refund The seller has a particular deadline for issuing a refund: Cancelling a paid purchase ― if you order and pay for a purchase, and then cancel ... |
| 10 | no | 73 | Purchases from private individuals or transactions between entrepreneurs | 0.249 | Purchases from private individuals or transactions between entrepreneurs If a buyer purchases an item from a private individual or if both sides of the transaction act as entrep... |

### Question 49/50

**Query:** How can I change the delivery date before my order is dispatched?

**Relevant docs:** `[67]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 67 | I want to change the delivery day. What should I do? | 0.990 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 2 | no | 77 | I have been waiting a long time for my order delivery | 0.797 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 3 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.731 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 4 | no | 78 | Cancelling an order | 0.602 | Cancelling an order You can cancel an order in the Purchase History tab, as long as the seller: does not change your order status to: In progress, Prepared for dispatch or Sent ... |
| 5 | no | 77 | I have been waiting a long time for my order delivery | 0.576 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 6 | no | 41 | How can I track a parcel? | 0.557 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 7 | no | 40 | I am buying many products — which delivery method should I choose? | 0.551 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 8 | no | 70 | Can I open a Discussion for a canceled order | 0.516 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
| 9 | no | 46 | Where you can see the estimated delivery time | 0.478 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |
| 10 | no | 50 | How to order a parcel with HopShop Delivery | 0.460 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |

### Question 50/50

**Query:** What should I do if my order delivery is delayed and I can't contact the seller?

**Relevant docs:** `[77]`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 0.500 | 0.631 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 67 | I want to change the delivery day. What should I do? | 0.939 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 2 | yes | 77 | I have been waiting a long time for my order delivery | 0.917 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 3 | no | 74 | What you should do if you do not receive your order | 0.835 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |
| 4 | yes | 77 | I have been waiting a long time for my order delivery | 0.748 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 5 | no | 66 | I want to change the pick-up point or parcel locker. What should I do? | 0.743 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 6 | no | 68 | The pick-up code does not work. What should I do? | 0.666 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 7 | no | 94 | I have received a defective product. What should I do? | 0.654 | I have received a defective product. What should I do? |
| 8 | no | 40 | I am buying many products — which delivery method should I choose? | 0.623 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 9 | no | 69 | The parcel is damaged. What should I do? | 0.622 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but c... |
| 10 | no | 70 | Can I open a Discussion for a canceled order | 0.580 | Can I open a Discussion for a canceled order Yes, but only if you have paid for the order and the seller has yet to process it. If you cancel an unpaid order ― you cannot open a... |
