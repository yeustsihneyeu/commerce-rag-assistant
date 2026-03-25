# FAQ Groundedness Evaluation Report

Source notebook: `notebooks/12_faq_groundedness_evaluating.ipynb`

## Overview

- Evaluated questions: 50
- Mean groundedness: 0.905

## Summary Tables

### Final Metrics

| row | groundedness |
| --- | --- |
| mean | 0.905 |

## Detailed Results

### Question 1/50

**Query:** Will I get a full refund including shipping if I return my order?

**Groundedness:** 0.000

**Relevant docs:** `[83]`

**Retrieved docs:** `[93]`

**Reference answer:**

The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you paid for the purchase.
In some cases, the seller may reduce the refund amount ― for example, if the product has been damaged in transport or has clear signs of use. If the seller refunds you only partially, you will find a justification for that in an email.
The seller is not obliged to refund you for all the additional expenses. For example, if you choose a different delivery option than the cheapest one offered by the seller, they will refund you the cost of the cheapest option.

**Generated answer:**

The information was not found. You can call the support center by number +48 123123123.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 93 | What to do if the seller does not issue a refund | 2.523 | What to do if the seller does not issue a refund If you return your purchase, but the seller does not refund it, start a Discussion. The seller has 24 hours to respond. If you cannot reach an agreement, click [Ask Hop... |

### Question 2/50

**Query:** Can I use multiple delivery addresses for one order or just one?

**Groundedness:** 1.000

**Relevant docs:** `[25]`

**Retrieved docs:** `[25]`

**Reference answer:**

Select one delivery address and one set of VAT invoice details for the whole order.

**Generated answer:**

You can only select one delivery address for the whole order.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 25 | One delivery address | 3.250 | One delivery address Select one delivery address and one set of VAT invoice details for the whole order. |

### Question 3/50

**Query:** Why does my payment status show as canceled or pending on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[33]`

**Retrieved docs:** `[33, 34]`

**Reference answer:**

Your payment may have the Canceled status if:
the payment has not been made through HopShop Finance within 10 days of selecting the payment method
you have canceled your payment (in this case, we will refund you to the bank account you paid from)
the bank has not accepted your payment
a PayU S.A. or PayPro S.A. employee has canceled your payment (it may happen if the payment is suspected to be incorrect).
If you cancel your payment, the seller will not get funds. Remember that the seller may still expect you to finalize the transaction.
What to do next
If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] by the unpaid order.
If the payment is Canceled and your bank account has been charged, you will get a refund to the same bank account.
Note
Every payment starts with the Pending status.
If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it:
Open the Purchase History tab.
Click [retry payment] by the unpaid order.
Select the delivery and payment method ― you can choose different methods than before.

**Generated answer:**

Your payment may show as pending or canceled if:  
- The payment was not made through HopShop Finance within 10 days.
- You canceled the payment.
- The bank didn't accept your payment.
- A PayU S.A. or PayPro S.A. employee canceled your payment due to suspected issues.
Pending status also appears before payment is completed, or if there are technical/banking delays.  
If your bank account hasn’t been charged, you can retry the payment from your Purchase History tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 33 | Why your payment is pending or canceled | 7.997 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payment method you have canceled your payment... |
| 2 | 34 | Other reasons why your payment may be pending | 6.842 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time ... |

### Question 4/50

**Query:** How can I find the seller's email and phone number after I make a purchase?

**Groundedness:** 1.000

**Relevant docs:** `[21]`

**Retrieved docs:** `[21]`

**Reference answer:**

After completing each transaction, we will email you the seller's contact information, including their email address and phone number.
After signing in, you can also check that information:
before making the purchase — on the offer page, in the Contact sub-section of the About Seller section (if the seller provided contact details)
after making the purchase — when you click [purchase details] next to a given order in the Purchase History tab.

**Generated answer:**

After making a purchase, you can find the seller's email and phone number by clicking [purchase details] next to your order in the Purchase History tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 21 | The seller's contact information | 7.805 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After signing in, you can also check that informa... |

### Question 5/50

**Query:** What should I do if my parcel was damaged when I picked it up?

**Groundedness:** 1.000

**Relevant docs:** `[69]`

**Retrieved docs:** `[69]`

**Reference answer:**

If you notice the damage in the pick-up point:
do not collect the parcel — it will be returned to the seller or
collect the parcel but complete the damage report (the document is available in Polish) together with the pick-up point employee, and file a complaint.
If you collect the parcel from a parcel locker and the package is damaged — report it through the app. Click [file a delivery complaint] in the purchase details.
If you notice the damage after you have collected the parcel, complete the damage report (the document is available in Polish), and file a complaint.

**Generated answer:**

If you noticed the damage at the pick-up point, you can either not collect the parcel (it will be returned to the seller) or collect it and complete a damage report with the pick-up point employee, then file a complaint. If you collected it from a parcel locker and it was damaged, report it through the app by clicking [file a delivery complaint] in the purchase details. If you noticed the damage after collecting the parcel, complete the damage report (available in Polish) and file a complaint.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 69 | The parcel is damaged. What should I do? | 9.028 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but complete the damage report (the document ... |

### Question 6/50

**Query:** How do I sign up using my Google or Facebook account?

**Groundedness:** 1.000

**Relevant docs:** `[3]`

**Retrieved docs:** `[3]`

**Reference answer:**

Open the sign in page.
Select signing in through Facebook or Google.
Sign in to your Facebook or Google account. Then, we will automatically redirect you to the registration page.
Determine whether you are over 18 years old. If not, provide your exact date of birth. You will hold a Junior account which will be transformed into a regular account once you turn 18.
Accept the HopShop Terms & Conditions and click [register].
Done! We will give you a default username― you can change it in the Account details tab.

**Generated answer:**

To sign up using your Google or Facebook account, open the sign in page, select signing in through Facebook or Google, and sign in to your account. You’ll be redirected to the registration page, where you confirm your age, accept the Terms & Conditions, and click register. Done!

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 3 | How to register with Google or Facebook account | 7.880 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will automatically redirect you to the registra... |

### Question 7/50

**Query:** How can I find my parcel's tracking number and check its delivery status on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[42]`

**Retrieved docs:** `[42]`

**Reference answer:**

You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the order you want to track, and then, [expand purchase details] the email notification the HopShop app ― on the purchase list, in the Purchase details section and in the My Parcels tab the My Parcels tab ― on your computer. provided that these 2 conditions are met: you complete the delivery and payment form while paying for your purchase through HopShop Finance the seller enters the tracking number in the Payment card. If those conditions are met, you can find the following basic order information in the Purchase details of the Purchase History tab: the seller's details the offer title and ID date of purchase the selected carrier the tracking number the current order status (for example, Pending dispatch, Dispatched, In transit, Pick up your parcel). You can also ask the seller to provide you with the tracking number, and then, track your parcel on the carrier's website: Poczta Polska DHL UPS GLS ORLEN InPost DPD Pocztex FedEx TNT Express Geis DB Schenker Raben.

**Generated answer:**

You can check your parcel's tracking number and delivery status in the Purchase History tab by clicking [purchase details] and expanding the details, in the email notification, or in the HopShop app under Purchase details or the My Parcels tab. Make sure you completed the delivery and payment form through HopShop Finance and the seller entered the tracking number.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 42 | Where to check the parcel tracking number and delivery status | 8.957 | Where to check the parcel tracking number and delivery status You can check the delivery status of your parcel in: the Purchase History tab ― click [purchase details] under the order you want to track, and then, [expa... |

### Question 8/50

**Query:** How will I receive my refund from the seller?

**Groundedness:** 0.000

**Relevant docs:** `[85]`

**Retrieved docs:** `[83]`

**Reference answer:**

The refund method depends on the payment method you chose for your purchase. Keep reading to learn how the refund works for each method.

**Generated answer:**

The information was not found. You can call the support center by number +48 123123123.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 83 | How much refund you can get from the seller | 6.950 | How much refund you can get from the seller The seller refunds you for the returned products and the cheapest delivery option. However, you may not receive the full amount you paid for the purchase. In some cases, the... |

### Question 9/50

**Query:** How long does it take to get a refund for a wire transfer, and what if I used a postal order?

**Groundedness:** 1.000

**Relevant docs:** `[91]`

**Retrieved docs:** `[91]`

**Reference answer:**

You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email you and ask you to provide details necessary to issue a refund. The money transferred with a postal order are booked in the account within 14 days.

**Generated answer:**

You will get the refund within 3 business days to the bank account you provided. If you used a postal order, the money will be booked in the account within 14 days.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 91 | Wire transfer | 8.146 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email you and ask you to provide details necess... |

### Question 10/50

**Query:** How is the estimated delivery time calculated on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[43]`

**Retrieved docs:** `[43]`

**Reference answer:**

For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your parcel will reach you or the pick-up point.
Estimated delivery time is influenced by:
dispatch time ― it is the estimated time the seller needs to prepare a parcel for dispatch, counted from the seller receiving the payment to the dispatch
transit time ― it is the time when the parcel is being transported to you by the carrier.

**Generated answer:**

The estimated delivery time on HopShop is calculated based on dispatch time (how long it takes the seller to prepare and send your parcel after receiving payment) and transit time (how long the carrier takes to deliver it to you).

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 43 | Estimated delivery time | 7.210 | Estimated delivery time For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your parcel will reach you or the pick-up po... |

### Question 11/50

**Query:** What happens to my gift card if I return an order I paid for with it?

**Groundedness:** 1.000

**Relevant docs:** `[92]`

**Retrieved docs:** `[92]`

**Reference answer:**

If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to make the purchase. The terms of use and expiration date of the card will not change. If the seller issues the refund after the gift card is expired, you can use it within 14 days of the refund. You will find the gift card in the Coupons tab and during transaction finalization in the (Pay less) section.

**Generated answer:**

If you return an order paid with a gift card, the value of the refund will be added back to your gift card. The gift card will appear in the Coupons tab and during checkout in the (Pay less) section. The terms and expiration date will not change.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 92 | A gift card | 7.677 | A gift card If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to make the purchase. The terms of use and ex... |

### Question 12/50

**Query:** How can I reorder a single product from my past purchases?

**Groundedness:** 1.000

**Relevant docs:** `[16]`

**Retrieved docs:** `[16]`

**Reference answer:**

Go to the Purchase History tab.
Click [purchase details] next to the selected order.
Under each product in that order, you will see 2 buttons:
[to cart] — click to add the product to cart
[buy now] — click to go to the form where you can select the delivery option and payment method.
If the offer with the product you selected is already inactive, we will show you other offers with the same product.

**Generated answer:**

To reorder a single product from your past purchases, go to the Purchase History tab, click [purchase details] next to the selected order, and use the [to cart] or [buy now] button under the product you want to reorder.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 16 | How to buy again a single product | 3.848 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: [to cart] — click to add the product to ... |

### Question 13/50

**Query:** How will I be notified when my refund is processed?

**Groundedness:** 1.000

**Relevant docs:** `[84]`

**Retrieved docs:** `[84]`

**Reference answer:**

We will let you know by email when the seller issues the refund. In the email, you will find information about the purchase which the refund concerns, as well as the refund amount, and method. You can find the refund information in the details of your purchase.

**Generated answer:**

You will be notified by email when the seller issues the refund. The email will include information about the purchase, the refund amount, and the method.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 84 | How you will learn about the refund | 0.003 | How you will learn about the refund We will let you know by email when the seller issues the refund. In the email, you will find information about the purchase which the refund concerns, as well as the refund amount, ... |

### Question 14/50

**Query:** How can I open a Discussion if I canceled an order paid through HopShop Finance and haven’t received a refund?

**Groundedness:** 1.000

**Relevant docs:** `[71]`

**Retrieved docs:** `[71]`

**Reference answer:**

If you have paid for your order through HopShop Finance, you can open a Discussion by yourself. You can do it in the Purchase History tab by clicking [report a problem with the purchase] under a given order. If you paid for your order outside HopShop Finance (for example, with a wire transfer), we can open a Discussion on your behalf. In this case, contact us. When you can open a Discussion for a canceled order You can do it when you cancel an order you have paid for through HopShop Finance and the seller: has not refunded you has not refunded your whole payment has delivered the order to you (even though you had canceled it) and you want to file a complaint.

**Generated answer:**

You can open a Discussion yourself in the Purchase History tab by clicking [report a problem with the purchase] under the given order.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 71 | How to open a Discussion for a canceled order | 9.263 | How to open a Discussion for a canceled order If you have paid for your order through HopShop Finance, you can open a Discussion by yourself. You can do it in the Purchase History tab by clicking [report a problem wit... |

### Question 15/50

**Query:** Why might my actual delivery time be different from the estimated delivery time?

**Groundedness:** 1.000

**Relevant docs:** `[45]`

**Retrieved docs:** `[45]`

**Reference answer:**

We calculate the estimated delivery time based on the available data. It may differ from the actual delivery time because the algorithm cannot predict random incidents or unplanned delays of sellers and carriers.

**Generated answer:**

Your actual delivery time might be different from the estimated delivery time because the estimate is based on available data, but the algorithm cannot predict random incidents or unplanned delays of sellers and carriers.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 45 | The estimated delivery time may differ from the actual delivery time | 8.938 | The estimated delivery time may differ from the actual delivery time We calculate the estimated delivery time based on the available data. It may differ from the actual delivery time because the algorithm cannot predi... |

### Question 16/50

**Query:** Who is responsible if an item is damaged during delivery when buying from an entrepreneur?

**Groundedness:** 1.000

**Relevant docs:** `[72]`

**Retrieved docs:** `[72, 73]`

**Reference answer:**

If a consumer buys an item from an entrepreneur, then the entrepreneur (in this case: the seller) is responsible for the risk of the item being damaged or lost until the item is collected by the buyer.
Exception
When a buyer chooses a different carrier than those offered by the entrepreneur (for example, they will ask to ship the item by post, although the seller has only offered courier delivery), the responsibility for the parcel passes to the buyer.

**Generated answer:**

If a consumer buys from an entrepreneur, the entrepreneur is responsible for the item being damaged or lost until the buyer collects it, unless the buyer chooses a different carrier than those offered by the seller.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 72 | Consumer purchase from an entrepreneur | 8.587 | Consumer purchase from an entrepreneur If a consumer buys an item from an entrepreneur, then the entrepreneur (in this case: the seller) is responsible for the risk of the item being damaged or lost until the item is ... |
| 2 | 73 | Purchases from private individuals or transactions between entrepreneurs | 7.339 | Purchases from private individuals or transactions between entrepreneurs If a buyer purchases an item from a private individual or if both sides of the transaction act as entrepreneurs — the purchased items are releas... |

### Question 17/50

**Query:** What should I do if my pick-up code isn’t working at the parcel locker?

**Groundedness:** 1.000

**Relevant docs:** `[68]`

**Retrieved docs:** `[68]`

**Reference answer:**

Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase History tabs. If it does not help — call the number that is directly below the parcel locker's screen or click [contact us] below this article.

**Generated answer:**

Firstly, make sure you enter the correct pick-up code found in your order details (My Parcels or Purchase History tabs). If it still doesn’t work, call the number directly below the parcel locker's screen or click [contact us] below the article.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 68 | The pick-up code does not work. What should I do? | 8.597 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase History tabs. If it does not help — call the ... |

### Question 18/50

**Query:** What happens if I frequently cancel or don't pay for my purchases on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[79]`

**Retrieved docs:** `[79]`

**Reference answer:**

If you have failed to pay for the purchase or collect a POD parcel again ― the seller may think you do this on purpose and ask us for help. We will check if you do not violate our rules. This is why you should inform the seller about any payment delay or order cancelation. This way, you can avoid potential misunderstanding. We work hard to keep transactions on HopShop safe. We monitor them with our tools for internal use. If you often cancel your orders, we might ask you for an explanation. How to open a Discussion and resolve an issue with the seller If you have not succeeded in contacting the seller or solving the problem with them, you can open a Discussion. You can open only one Discussion per transaction. If you close the Discussion, you can re-open it only once. You can do it within 2 years of making a given purchase.

**Generated answer:**

If you often cancel your orders or fail to pay, HopShop may ask you for an explanation and check if you are violating their rules. It’s best to inform the seller about any payment delay or order cancellation to avoid misunderstandings.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 79 | What if you resign from purchases repeatedly | 7.016 | What if you resign from purchases repeatedly If you have failed to pay for the purchase or collect a POD parcel again ― the seller may think you do this on purpose and ask us for help. We will check if you do not viol... |

### Question 19/50

**Query:** What do I need to do to pick up my parcel from a pick-up point?

**Groundedness:** 0.250

**Relevant docs:** `[55]`

**Retrieved docs:** `[69]`

**Reference answer:**

When you get the pick-up code — go to the pick-up point, provide the employee with the code, and collect your parcel.

**Generated answer:**

The information was not found. You can call the support center by number +48 123123123.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 69 | The parcel is damaged. What should I do? | 6.957 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but complete the damage report (the document ... |

### Question 20/50

**Query:** How long does it take to get a BLIK refund and where can I see it in my bank account?

**Groundedness:** 1.000

**Relevant docs:** `[90]`

**Retrieved docs:** `[90]`

**Reference answer:**

You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase. You will be refunded within 3 business days. ?

**Generated answer:**

You will be refunded within 3 business days. You can see the refund details in your account history below the date of payment for the purchase.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 90 | BLIK | 7.463 | BLIK You will get the refund to your bank account. For the majority of banks, you will see the refund details in your account history below the date of payment for the purchase. You will be refunded within 3 business ... |

### Question 21/50

**Query:** How do I pay for my order using PayPal and how does currency conversion work?

**Groundedness:** 1.000

**Relevant docs:** `[31]`

**Retrieved docs:** `[31]`

**Reference answer:**

When you are ready to pay for your order, go to the delivery and payment form. In the Payment method section, select PayPal. Click [buy and pay]. You will be redirected to the PayPal website. Follow the instructions there to pay. Done! How currency conversion works Depending on the currency you choose to pay in and the currency of the funds on your bank account: if the payment currency and your bank account currency are the same ― you are charged the price in this currency if the payment currency and your bank account currency are different ― the card issuer converts the payment into your bank account currency. Examples You want to pay in EUR. The currency of money on your card is EUR. When you pay, you will pay in EUR ― with no currency conversion needed. You want to pay in PLN. The currency of the funds on your card is EUR. When you pay, the bank will convert the payment currency from PLN into EUR. The conversion rate is calculated by PayU ― the payment service provider ― and updated daily.

**Generated answer:**

To pay with PayPal, go to the delivery and payment form, select PayPal as the payment method, and click [buy and pay]. You’ll be redirected to the PayPal website—just follow the instructions to complete your payment.

For currency conversion:  
- If your payment currency and bank account currency are the same, you pay that amount with no conversion.
- If they are different, your card issuer converts the payment into your account currency, using a rate calculated by PayU and updated daily.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 31 | How to pay with PayPal | 7.878 | How to pay with PayPal When you are ready to pay for your order, go to the delivery and payment form. In the Payment method section, select PayPal. Click [buy and pay]. You will be redirected to the PayPal website. Fo... |

### Question 22/50

**Query:** How can I change my parcel locker or pick-up point before the seller ships my order?

**Groundedness:** 1.000

**Relevant docs:** `[66]`

**Retrieved docs:** `[66]`

**Reference answer:**

If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or parcel locker. You can find the seller's contact information in the email purchase confirmation.

**Generated answer:**

If the seller has not yet dispatched your parcel, contact them and ask them to change the pick-up point or parcel locker. You can find the seller's contact information in the email purchase confirmation.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 66 | I want to change the pick-up point or parcel locker. What should I do? | 6.717 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or parcel locker. You can find the seller's ... |

### Question 23/50

**Query:** What are the options for returning a HopShop Delivery parcel?

**Groundedness:** 1.000

**Relevant docs:** `[58]`

**Retrieved docs:** `[58, 47]`

**Reference answer:**

You can do it in several ways:
within Smart! free of charge
outside Smart! free of charge
with the payable DPD and InPost return options
on your own at your expense.
You can return HopShop Delivery parcels the same way as regular parcels. Learn how to do it.
Having issues with the return? Click [contact us] under this article and describe your issue — we are here to help you!

**Generated answer:**

You can return a HopShop Delivery parcel in several ways:
- within Smart! free of charge
- outside Smart! free of charge
- with payable DPD and InPost return options
- on your own at your expense.

You can return HopShop Delivery parcels the same way as regular parcels.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 58 | How to return an HopShop Delivery parcel | 7.245 | How to return an HopShop Delivery parcel You can do it in several ways: within Smart! free of charge outside Smart! free of charge with the payable DPD and InPost return options on your own at your expense. You can re... |
| 2 | 47 | The HopShop Delivery program — information for buyers | 6.251 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the program in some offers since June 4. HopShop D... |

### Question 24/50

**Query:** How long will my parcel be held at the pick-up point before being sent back?

**Groundedness:** 1.000

**Relevant docs:** `[57]`

**Retrieved docs:** `[57]`

**Reference answer:**

The parcel will wait for you for:
2 working days — in HopShop One pick-up points and parcel lockers
3 working days — in ORLEN Paczka pick-up points and parcel lockers.
We will remind you about the parcel on the second day. If you do not collect your parcel on time, we will return it to the seller, and change the parcel status to Parcel sent back to sender.

**Generated answer:**

Your parcel will be held at the pick-up point for 2 working days in HopShop One locations and 3 working days in ORLEN Paczka locations before being sent back.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 57 | How much time you have to collect a parcel | 6.098 | How much time you have to collect a parcel The parcel will wait for you for: 2 working days — in HopShop One pick-up points and parcel lockers 3 working days — in ORLEN Paczka pick-up points and parcel lockers. We wil... |

### Question 25/50

**Query:** What should I do if I'm unsure about my parcel status?

**Groundedness:** 0.250

**Relevant docs:** `[52]`

**Retrieved docs:** `[69]`

**Reference answer:**

If you have any doubts regarding what your parcel status means — click [contact us] below this article.

**Generated answer:**

The information was not found. You can call the support center by number +48 123123123.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 69 | The parcel is damaged. What should I do? | 2.287 | The parcel is damaged. What should I do? If you notice the damage in the pick-up point: do not collect the parcel — it will be returned to the seller or collect the parcel but complete the damage report (the document ... |

### Question 26/50

**Query:** What happens if the parcel locker has no available space for my package?

**Groundedness:** 0.250

**Relevant docs:** `[65]`

**Retrieved docs:** `[63]`

**Reference answer:**

We will redirect your parcel to a different parcel locker or pick-up point and send you a notification.

**Generated answer:**

The information was not found; you can call the support center by number +48 123123123.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 1.946 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If you cannot see a specific pick-up point, i... |

### Question 27/50

**Query:** Can I open a Discussion for a purchase made more than two years ago?

**Groundedness:** 1.000

**Relevant docs:** `[80]`

**Retrieved docs:** `[80]`

**Reference answer:**

If 2 years (730 days) have passed from making the purchase, it is impossible to open a Discussion.
If your order included a purchase in several offers, you can indicate only the offer for which the problem occurred.

**Generated answer:**

No, you cannot open a Discussion for a purchase made more than two years ago.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 80 | Check the Discussion time frame | 5.876 | Check the Discussion time frame If 2 years (730 days) have passed from making the purchase, it is impossible to open a Discussion. If your order included a purchase in several offers, you can indicate only the offer f... |

### Question 28/50

**Query:** How can I collect my parcel from a parcel locker using a pick-up code or the HopShop app?

**Groundedness:** 1.000

**Relevant docs:** `[56]`

**Retrieved docs:** `[56]`

**Reference answer:**

You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the HopShop app. If you select ORLEN Paczka delivery options within HopShop Delivery — you will collect your parcel using the HopShop app or with a code only.

**Generated answer:**

You can collect your parcel from a parcel locker by entering the pick-up code on the locker screen or by using the HopShop app.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 56 | How to collect a parcel from a parcel locker | 9.776 | How to collect a parcel from a parcel locker You can do it in 2 ways: directly at the locker — enter the pick-up code on the locker screen or scan the QR code remotely with the HopShop app. If you select ORLEN Paczka ... |

### Question 29/50

**Query:** How can I share my HopShop Delivery pick-up code with someone else using the app?

**Groundedness:** 1.000

**Relevant docs:** `[54]`

**Retrieved docs:** `[54]`

**Reference answer:**

You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app.
From the [Purchase History](https://HopShop.pl/moje-HopShop/zakupy/kupione or the My parcels tab, go to Purchase details and click [share pick-up code].
Choose the way you want to share your pick-up code (for example, SMS).
We will automatically redirect you to the app you choose and add the content of the message in it with information about the pick-up code and the address of the parcel locker or pick-up point.
Remember that when you share a pick-up code with another person, you take responsibility for transferring to that person the right to collect your parcel.

**Generated answer:**

You can share your HopShop Delivery pick-up code with someone else using the mobile app. Go to Purchase History or the My parcels tab, enter Purchase details, and click [share pick-up code]. Then choose how you want to share it (e.g., SMS). The app will fill in the message with the pick-up code and pick-up point address.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 54 | How to share the pick-up code with others | 9.641 | How to share the pick-up code with others You can share the pick-up code of an HopShop Delivery parcel with others using our mobile app. From the [Purchase History](https://HopShop.pl/moje-HopShop/zakupy/kupione or th... |

### Question 30/50

**Query:** How long does it take to get a refund to my bank account if I used a debit card?

**Groundedness:** 1.000

**Relevant docs:** `[86]`

**Retrieved docs:** `[86, 87]`

**Reference answer:**

You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to the date of payment for the purchase. If you paid for your order with: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business days.

**Generated answer:**

If you used a debit card, the refund will be processed to your bank account. For Mastercard, it takes up to 3 business days. For Visa, it takes up to 7 business days.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 86 | A debit card | 7.985 | A debit card You will receive a refund to your bank account. For the majority of banks, you will see the refund details in your bank statement or your account history next to the date of payment for the purchase. If y... |
| 2 | 87 | A credit card | 5.556 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business days. For the majority of banks, you wil... |

### Question 31/50

**Query:** How can I track my HopShop Delivery parcel and know when it's ready for collection?

**Groundedness:** 1.000

**Relevant docs:** `[51]`

**Retrieved docs:** `[41, 51]`

**Reference answer:**

You can check your parcel status in several places: in the email, SMS, and notifications in the HopShop app • in the Purchase History tab, when you click on the details of a given purchase: if the parcel is in transit — you can find its current status at the top if the parcel has been collected — click [expand delivery details]. when the parcel is in transit, you can track it in the app or on this website.

**Generated answer:**

You can track your HopShop Delivery parcel status in several ways:  
- Check emails, SMS, or notifications in the HopShop app.  
- Go to the Purchase History tab and click on the details of your order to see the current status.  
- When the parcel is ready for collection, you’ll see the update in these places.  
- You can also track it in the app or on the provided website link.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 41 | How can I track a parcel? | 6.815 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in the payment card. If those conditions are... |
| 2 | 51 | How to check the status of an HopShop Delivery parcel and how to collect it | 6.687 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopShop app • in the Purchase History tab, wh... |

### Question 32/50

**Query:** How can I find out which delivery options are available for an item on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[36]`

**Retrieved docs:** `[36, 15]`

**Reference answer:**

When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Delivery and payment section to check what delivery options are available for the offer you are interested in.

**Generated answer:**

To find out which delivery options are available for an item on HopShop, go to the Delivery and payment section of the offer you are interested in.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 36 | Delivery options on HopShop | 7.283 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Delivery and payment section to check what de... |
| 2 | 15 | How to buy a product on HopShop | 6.504 | How to buy a product on HopShop 1. Find the product you need Use the search engine to find the product you are looking for. You can use sorting options and filters to better match your search results. 2. Read the prod... |

### Question 33/50

**Query:** Can I withdraw from the agreement if my account is older than 14 days?

**Groundedness:** 1.000

**Relevant docs:** `[10]`

**Retrieved docs:** `[10, 9]`

**Reference answer:**

To withdraw from the agreement, submit this application. You will then get a confirmation email from us.
You will not be able to submit the application for an account older than 14 days or submit multiple applications for the same account. If you try to do it, we will display a message with a hint.
You will lose access to your account immediately after submitting the application. We will log you out and you will not sign in again.
What happens next
Usually, we consider the application right away ― within minutes. It may take us up to 7 days.
If there were no sales or purchases on your account ― we will completely and irreversibly delete your personal details from our systems.
If you have made a purchase or listed an offer on that account ― we will store your data until that purchase or sale has been processed. In that case, you may use the second option: termination of agreement with HopShop.
If we find that you do not meet the conditions above (for example, you made a purchase or listed an offer on that account) ― we will reject your application and you will regain access to your account. We will inform you about it by email. If that is the case, you can use the other option ― terminating the agreement.

**Generated answer:**

No, you cannot withdraw from the agreement if your account is older than 14 days.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 10 | How to withdraw from the agreement | 8.267 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the application for an account older than 14 d... |
| 2 | 9 | When you can withdraw from the agreement | 6.414 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account was registered you have no financial li... |

### Question 34/50

**Query:** How can I make a purchase or set up recurring orders on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[14]`

**Retrieved docs:** `[14]`

**Reference answer:**

In this article, you will learn
how to buy a product on HopShop
how to buy the same product or all products from an order again
how to make recurring purchases.
Buying on HopShop is simple and you can do it in several ways — depending on your needs.

**Generated answer:**

To make a purchase or set up recurring orders on HopShop, you can buy a product, reorder the same product or all products from a previous order, and make recurring purchases. Buying is simple and can be done in several ways depending on your needs.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 14 | How to buy on HopShop | 5.490 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purchases. Buying on HopShop is simple and yo... |

### Question 35/50

**Query:** Can I split payment for multiple orders from different sellers?

**Groundedness:** 1.000

**Relevant docs:** `[30]`

**Retrieved docs:** `[24, 30]`

**Reference answer:**

In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller.
How to pay for your order ― information for buyers outside Poland
Before you pay, you can choose in which currency you want to pay ― the Polish zloty (PLN) or the Euro (EUR) ― in the localization settings.
You can pay for your purchases on HopShop with:
a payment card
PayPal ― only when you pay in EUR.
Payment by card
You can pay with a card if you hold a MasterCard or a VISA payment card. Check how to pay with a card.

**Generated answer:**

Yes, you can split payment for multiple orders from different sellers by selecting only those orders you want to pay for in the Purchase History tab and then clicking [pay].

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 24 | How to pay for orders made from multiple sellers | 6.708 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |
| 2 | 30 | How to split the payment | 5.575 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to pay for your order ― information for buye... |

### Question 36/50

**Query:** How long does a seller have to respond to my complaint before it is considered upheld?

**Groundedness:** 1.000

**Relevant docs:** `[95]`

**Retrieved docs:** `[95]`

**Reference answer:**

When the seller receives your complaint, they have 14 days to address it. If they do not do it by the due date, your complaint is considered upheld.

**Generated answer:**

The seller has 14 days to respond to your complaint. If they do not respond within this time, your complaint is considered upheld.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 95 | Deadline for processing a complaint | 7.648 | Deadline for processing a complaint When the seller receives your complaint, they have 14 days to address it. If they do not do it by the due date, your complaint is considered upheld. |

### Question 37/50

**Query:** How can I enable sign-in with my email and password?

**Groundedness:** 1.000

**Relevant docs:** `[4]`

**Retrieved docs:** `[4]`

**Reference answer:**

If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Password tab.

**Generated answer:**

To enable sign-in with your email and password, set a password in the Sign-in and Password tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 4 | Signing in with a password and email address | 5.492 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Password tab. |

### Question 38/50

**Query:** What are the ways to contact a seller on HopShop?

**Groundedness:** 1.000

**Relevant docs:** `[19]`

**Retrieved docs:** `[19]`

**Reference answer:**

You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through the Message Center by opening a Discussion.

**Generated answer:**

You can contact the seller on HopShop by clicking [Ask a question] on the offer page, using their direct contact information, through the Message Center, or by opening a Discussion.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 19 | How to contact the seller | 8.865 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through the Message Center by opening a Discussion. |

### Question 39/50

**Query:** Where can I find the estimated delivery time for an offer?

**Groundedness:** 1.000

**Relevant docs:** `[46]`

**Retrieved docs:** `[46]`

**Reference answer:**

We display the estimated delivery time individually for each offer in a few locations on different purchase stages:
on the offer list
on the offer page
if you click [delivery] on the offer page
in the payment and delivery form
on the thank you page
in the order details you can find in the Purchase History tab
in selected sections of the recommended offers ― if delivery time is up to 2 business days
in the Buy and Pay section ― if it is available in the offer.
We display estimated delivery time as:
(today), (tomorrow) or (in 2 days) – in selected locations if delivery time does not exceed 2 business days
a specific date or time range ― if the delivery time is 7 days or fewer; for example:
(Mon. Dec. 2 in a pick-up point)
(Mon. Dec. 2 ― Wed. Dec. 4 in your house)
a number of days ― if delivery time is longer than 7 days; for example:
in 13 ― 31 days in your house)
(immediately) ―for email deliveries and parcels for personal pick-up from the seller.
Additional information
You can filter search results by the estimated delivery time.
In exceptional situations, such as Christmas or extreme weather conditions, the estimated delivery time might be longer.
The estimated delivery time accounts for weekends, bank holidays, and sellers’ vacation.
The shipping time depends on the carrier.

**Generated answer:**

You can find the estimated delivery time for an offer on the offer list, on the offer page, by clicking [delivery] on the offer page, in the payment and delivery form, on the thank you page, and in the order details in your Purchase History tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 46 | Where you can see the estimated delivery time | 8.674 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer list on the offer page if you click [deliv... |

### Question 40/50

**Query:** Can I combine shipping costs when buying multiple items from different sellers?

**Groundedness:** 1.000

**Relevant docs:** `[40]`

**Retrieved docs:** `[40]`

**Reference answer:**

You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those available in each offer. You can merge delivery costs if you buy from one seller provided that the seller enables you to do so. Depending on the seller’s settings, you will pay: the cost of the most expensive delivery method among the offers you buy in the cost of the cheapest delivery method among the offers you buy in the total cost of delivery from all the offers — the parcels will be dispatched separately.

**Generated answer:**

You cannot merge delivery costs if you buy from different sellers.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 40 | I am buying many products — which delivery method should I choose? | 6.621 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |

### Question 41/50

**Query:** What are the ways to register for a HopShop account?

**Groundedness:** 1.000

**Relevant docs:** `[1]`

**Retrieved docs:** `[1]`

**Reference answer:**

If you want to be an active user of HopShop, register in a few simple steps. It is free of charge.
Check how to register
with an email address
with a Google or Facebook account
with a phone number.

**Generated answer:**

You can register for a HopShop account using an email address, a Google or Facebook account, or a phone number.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 1 | How to register on HopShop | 6.975 | How to register on HopShop If you want to be an active user of HopShop, register in a few simple steps. It is free of charge. Check how to register with an email address with a Google or Facebook account with a phone ... |

### Question 42/50

**Query:** Why isn't my usual pick-up point showing on the delivery map?

**Groundedness:** 1.000

**Relevant docs:** `[63]`

**Retrieved docs:** `[63]`

**Reference answer:**

We only display operating pick-up points and parcel lockers on the map. If you cannot see a specific pick-up point, it might be temporarily closed. In that case, choose a different pick-up point or parcel locker.

**Generated answer:**

Your usual pick-up point might be temporarily closed. Only operating pick-up points and parcel lockers are shown on the map. Please choose a different one.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 63 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? | 6.087 | Why can I not find a pick-up point or a parcel locker on the map while selecting a delivery option? We only display operating pick-up points and parcel lockers on the map. If you cannot see a specific pick-up point, i... |

### Question 43/50

**Query:** Why is my payment still pending after I paid by wire transfer through a third party?

**Groundedness:** 1.000

**Relevant docs:** `[34]`

**Retrieved docs:** `[34]`

**Reference answer:**

If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time depends on that party. Such payment is settled within 3 days ― do not retry the payment earlier. If you do, you will cancel your previous payment and it will be transferred back to the institution which made the transfer. If that is the case, and the institution does not have your funds, contact us.
If you pay for your order directly to the seller's bank account ― your payment will have the Pending status for 10 days. After this time, the payment will be canceled automatically, because it has not been made through HopShop.
Your payment method may be unavailable in a given moment - check the time your bank makes online transfers on the bank's website.
There have been technical issues with your payment.
If you have chosen to pay by a wire transfer in the delivery and payment form, and you want to issue an online transfer ― we will generate details on which you should make the transfer.

**Generated answer:**

If you have paid by wire transfer through a third party (like Poczta Polska), the transfer time depends on that party and can take up to 3 days. Do not retry the payment earlier, as it may cancel your previous payment. If the institution does not have your funds, contact us.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 34 | Other reasons why your payment may be pending | 8.209 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time ... |

### Question 44/50

**Query:** What should I do if the product I received is defective?

**Groundedness:** 0.500

**Relevant docs:** `[94]`

**Retrieved docs:** `[94]`

**Reference answer:**



**Generated answer:**

If you have received a defective product, please follow the instructions provided in the FAQ for defective items.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 94 | I have received a defective product. What should I do? | 6.506 | I have received a defective product. What should I do? |

### Question 45/50

**Query:** How long does it take to get a refund on my credit card for a Mastercard or Visa?

**Groundedness:** 1.000

**Relevant docs:** `[87]`

**Retrieved docs:** `[87]`

**Reference answer:**

You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business days. For the majority of banks, you will see the refund details in your bank statement or your account history next to the date of payment for the purchase. In some cases you may not see this information immediately after the refund. You might need to wait until the next billing period.

**Generated answer:**

For a Mastercard, you will get the refund within 3 business days. For a Visa, you will get the refund within 7 business days.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 87 | A credit card | 8.929 | A credit card You will get your refund to the card. In the case of: Mastercard ― you will get the refund within 3 business days Visa ― you will get the refund within 7 business days. For the majority of banks, you wil... |

### Question 46/50

**Query:** What situations allow me to file a complaint about your delivery service?

**Groundedness:** 1.000

**Relevant docs:** `[60]`

**Retrieved docs:** `[60]`

**Reference answer:**

You can file a complaint if:
the parcel goes missing
the parcel is damaged in transit
we do not perform the service on time
we provide the service incorrectly.
Who can file a complaint and when
As a buyer, you can file a complaint if:
you have already received your parcel
you have yet to receive the parcel, but the seller has waived the right to pursue claims to you (the document available in Polish)
If, upon parcel receipt, you find a defect or damage unnoticeable on the outside — you have 7 days to file a complaint about such a parcel. In other cases, you can file a complaint against our service up to 12 months from dispatching the parcel.
HopShop Delivery – frequently asked questions
Click on the question to see the answer.

**Generated answer:**

You can file a complaint if the parcel goes missing, the parcel is damaged in transit, we do not perform the service on time, or we provide the service incorrectly.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 60 | For what reasons you can file a complaint about the service | 5.621 | For what reasons you can file a complaint about the service You can file a complaint if: the parcel goes missing the parcel is damaged in transit we do not perform the service on time we provide the service incorrectl... |

### Question 47/50

**Query:** How do I close my HopShop account?

**Groundedness:** 1.000

**Relevant docs:** `[8]`

**Retrieved docs:** `[8]`

**Reference answer:**

You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement.

**Generated answer:**

You can close your HopShop account by withdrawing from the agreement or terminating the agreement.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 8 | How to close your HopShop account | 8.666 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |

### Question 48/50

**Query:** Do I have to use the original packaging or include the receipt when sending a product back for a complaint?

**Groundedness:** 1.000

**Relevant docs:** `[96]`

**Retrieved docs:** `[96]`

**Reference answer:**

If you send the product back as a part of the complaint, you should secure it properly. Usually, you are not required to return it in the original packaging. You are not required to include the receipt.

**Generated answer:**

You are not required to return the product in the original packaging or include the receipt when sending it back for a complaint.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 96 | Sending a product back to the seller | 8.169 | Sending a product back to the seller If you send the product back as a part of the complaint, you should secure it properly. Usually, you are not required to return it in the original packaging. You are not required t... |

### Question 49/50

**Query:** How can I change the delivery date before my order is dispatched?

**Groundedness:** 1.000

**Relevant docs:** `[67]`

**Retrieved docs:** `[67]`

**Reference answer:**

If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You can find the seller's contact information in the email purchase confirmation.

**Generated answer:**

If the seller has yet to dispatch your parcel, contact them and ask them to dispatch the parcel on a different date. You can find the seller's contact information in the email purchase confirmation.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 67 | I want to change the delivery day. What should I do? | 5.383 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You can find the seller's contact information ... |

### Question 50/50

**Query:** What should I do if my order delivery is delayed and I can't contact the seller?

**Groundedness:** 1.000

**Relevant docs:** `[77]`

**Retrieved docs:** `[74, 77]`

**Reference answer:**

Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have provided in the form ― find the relevant order in the Purchase History tab and click [purchase details]. If the information is incorrect, contact the seller as soon as possible.
Sometimes, the seller just dispatches the parcel late. Ask the seller when they had dispatched it:
open the Purchase History tab.
under the relevant order, click [purchase details]
you will find their contact information in the seller's details
email or call them.
Note that a parcel dispatched at the end of the week may reach you after the weekend.
You can find a tracking number in the details of the relevant order in the (Your parcel) section. Apart from the tracking number and carrier name, you can also find the parcel status and history there.
You will see a tracking number only if you have paid through HopShop Finance, and the seller has entered the tracking number in the payment card. If they have not done it, or you have paid outside HopShop Finance, ask the seller to send you a tracking number.
If you cannot contact the seller, try resolving the issue through a Discussion.
What to expect as a buyer in a Discussion
In a Discussion:
the seller should reply within 24 hours
if you do not reach an agreement, you can mark the Discussion as Unresolved — we will then join it
after 7 days ― if the Discussion has been opened for the following reason: I have not received the product.
after 14 days ― if the Discussion has been opened for a reason other than I have not received the product
you can ask us for help
if the issue has been resolved, you can close the Discussion at any time.
During the Discussion, the seller may ask you once to mark it as resolved.
We participate in a Discussion as an impartial party and our role is to help you both reach an agreement.
Check the list of your Discussions here.
What Discussions are and how they work
If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can describe the issue, and attach all necessary documents, receipts and photos in one place. All of that can make communication with the seller easier and help solve your issue fast.
Open a Discussion and provide all the details. This way, the seller can find all the necessary information about your matter.
What if you resign from the purchase and do not pay for it
If you confirm a purchase or win an auction, you automatically enter into an agreement with the seller. This means you are obliged to pay and collect an item you have bought. If you want to resign from a purchase for some reason, contact the seller ― for example, by email.

**Generated answer:**

If you can't contact the seller and your order delivery is delayed, try resolving the issue through a Discussion. If you do not reach an agreement, you can mark the Discussion as Unresolved and request help after 7 days.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 74 | What you should do if you do not receive your order | 7.359 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery declared in the offer has not been met. Cont... |
| 2 | 77 | I have been waiting a long time for my order delivery | 6.537 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have provided in the form ― find the relevan... |
