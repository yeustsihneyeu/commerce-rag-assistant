# FAQ Reranking Evaluation Report

Source notebook: `notebooks/09_faq_reranking_evaluating.ipynb`

## Overview

- Evaluated questions: 50
- Mean precision: 0.105 -> 0.105
- Mean recall: 1.000 -> 1.000
- Mean MRR: 0.891 -> 0.912
- Mean nDCG: 0.919 -> 0.934

## Summary Tables

### Final Metrics

| questions | precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | 0.105 | 0.105 | 1.000 | 1.000 | 0.891 | 0.912 | 0.919 | 0.934 |

## Detailed Results

### Question 1

**Query:** Will I get a full refund including shipping if I return my order?

**Relevant docs:** [83]

**Retrieved docs:** [83, 77, 93, 82, 70, 94, 40, 41, 86]

**Reranked docs:** [93, 83, 82, 86, 77, 70, 40, 41, 94]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 |

### Question 2

**Query:** Can I use multiple delivery addresses for one order or just one?

**Relevant docs:** [25]

**Retrieved docs:** [25, 7, 40, 24, 26, 47, 48, 28, 77, 67]

**Reranked docs:** [25, 26, 24, 40, 28, 77, 48, 7, 47, 67]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 3

**Query:** Why does my payment status show as canceled or pending on HopShop?

**Relevant docs:** [33]

**Retrieved docs:** [33, 34, 35, 29, 71, 42, 51, 32, 30, 77]

**Reranked docs:** [33, 34, 29, 71, 35, 42, 32, 77, 51, 30]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 4

**Query:** How can I find the seller's email and phone number after I make a purchase?

**Relevant docs:** [21]

**Retrieved docs:** [21, 41, 67, 66, 77, 20, 42, 68, 84]

**Reranked docs:** [21, 20, 77, 42, 67, 41, 66, 84, 68]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 5

**Query:** What should I do if my parcel was damaged when I picked it up?

**Relevant docs:** [69]

**Retrieved docs:** [69, 66, 68, 94, 67, 77, 60, 63, 41, 74]

**Reranked docs:** [69, 66, 68, 60, 67, 63, 77, 94, 74, 41]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 6

**Query:** How do I sign up using my Google or Facebook account?

**Relevant docs:** [3]

**Retrieved docs:** [3, 1, 7, 2, 4, 68, 5, 54, 10, 64]

**Reranked docs:** [3, 5, 1, 4, 2, 10, 7, 54, 68, 64]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 7

**Query:** How can I find my parcel's tracking number and check its delivery status on HopShop?

**Relevant docs:** [42]

**Retrieved docs:** [42, 51, 41, 77, 50, 59, 58, 64, 47, 49]

**Reranked docs:** [42, 41, 51, 77, 59, 50, 47, 58, 49, 64]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 8

**Query:** How will I receive my refund from the seller?

**Relevant docs:** [85]

**Retrieved docs:** [83, 85, 82, 84, 93, 77, 81, 74, 86]

**Reranked docs:** [83, 85, 82, 84, 81, 93, 86, 77, 74]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 0.500 | 0.500 | 0.631 | 0.631 |

### Question 9

**Query:** How long does it take to get a refund for a wire transfer, and what if I used a postal order?

**Relevant docs:** [91]

**Retrieved docs:** [91, 89, 93, 77, 34, 83, 86, 87, 90]

**Reranked docs:** [91, 34, 89, 86, 90, 87, 77, 93, 83]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 10

**Query:** How is the estimated delivery time calculated on HopShop?

**Relevant docs:** [43]

**Retrieved docs:** [43, 44, 45, 46, 50, 37, 49, 47, 36, 48]

**Reranked docs:** [43, 45, 44, 46, 37, 36, 48, 49, 47, 50]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 11

**Query:** What happens to my gift card if I return an order I paid for with it?

**Relevant docs:** [92]

**Retrieved docs:** [92, 32, 77, 86, 70, 94, 68, 67, 87]

**Reranked docs:** [92, 32, 86, 70, 77, 87, 68, 94, 67]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 12

**Query:** How can I reorder a single product from my past purchases?

**Relevant docs:** [16]

**Retrieved docs:** [16, 15, 17, 18, 35, 14, 77, 41, 79]

**Reranked docs:** [16, 17, 18, 15, 35, 77, 79, 14, 41]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 13

**Query:** How will I be notified when my refund is processed?

**Relevant docs:** [84]

**Retrieved docs:** [84, 85, 82, 77, 83, 88, 35, 90, 87]

**Reranked docs:** [84, 82, 87, 85, 90, 88, 83, 35, 77]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 14

**Query:** How can I open a Discussion if I canceled an order paid through HopShop Finance and haven’t received a refund?

**Relevant docs:** [71]

**Retrieved docs:** [71, 70, 81, 77, 33, 76, 93, 35, 75]

**Reranked docs:** [71, 76, 33, 81, 70, 77, 93, 35, 75]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 15

**Query:** Why might my actual delivery time be different from the estimated delivery time?

**Relevant docs:** [45]

**Retrieved docs:** [45, 46, 43, 44, 37, 77, 63, 34, 67]

**Reranked docs:** [45, 43, 46, 37, 44, 77, 34, 67, 63]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 16

**Query:** Who is responsible if an item is damaged during delivery when buying from an entrepreneur?

**Relevant docs:** [72]

**Retrieved docs:** [72, 97, 73, 69, 40, 60, 83, 36, 77]

**Reranked docs:** [72, 73, 97, 69, 60, 83, 77, 40, 36]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 17

**Query:** What should I do if my pick-up code isn’t working at the parcel locker?

**Relevant docs:** [68]

**Retrieved docs:** [68, 66, 53, 63, 64, 69, 56, 65, 55, 54]

**Reranked docs:** [68, 66, 69, 63, 53, 56, 65, 54, 64, 55]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 18

**Query:** What happens if I frequently cancel or don't pay for my purchases on HopShop?

**Relevant docs:** [79]

**Retrieved docs:** [79, 35, 77, 12, 13, 7, 32, 29, 14]

**Reranked docs:** [79, 29, 12, 35, 32, 7, 77, 13, 14]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 19

**Query:** What do I need to do to pick up my parcel from a pick-up point?

**Relevant docs:** [55]

**Retrieved docs:** [55, 66, 64, 68, 53, 63, 69, 56, 54, 57]

**Reranked docs:** [69, 66, 55, 53, 68, 54, 63, 64, 56, 57]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 0.333 | 1.000 | 0.500 |

### Question 20

**Query:** How long does it take to get a BLIK refund and where can I see it in my bank account?

**Relevant docs:** [90]

**Retrieved docs:** [90, 89, 86, 87, 77, 83, 46, 91, 88, 93]

**Reranked docs:** [90, 89, 87, 86, 91, 93, 77, 88, 46, 83]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 21

**Query:** How do I pay for my order using PayPal and how does currency conversion work?

**Relevant docs:** [31]

**Retrieved docs:** [31, 30, 77, 68, 24, 35, 28, 40, 41]

**Reranked docs:** [31, 30, 28, 24, 77, 40, 35, 41, 68]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 22

**Query:** How can I change my parcel locker or pick-up point before the seller ships my order?

**Relevant docs:** [66]

**Retrieved docs:** [66, 64, 63, 68, 67, 55, 65, 56, 53, 77]

**Reranked docs:** [66, 63, 65, 68, 53, 56, 64, 67, 77, 55]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 23

**Query:** What are the options for returning a HopShop Delivery parcel?

**Relevant docs:** [58]

**Retrieved docs:** [36, 58, 47, 48, 50, 61, 56, 51, 59, 49]

**Reranked docs:** [58, 47, 36, 50, 48, 56, 59, 49, 51, 61]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 24

**Query:** How long will my parcel be held at the pick-up point before being sent back?

**Relevant docs:** [57]

**Retrieved docs:** [64, 55, 57, 66, 63, 53, 65, 68, 54, 77]

**Reranked docs:** [57, 77, 53, 63, 66, 55, 65, 64, 54, 68]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.333 | 1.000 | 0.500 | 1.000 |

### Question 25

**Query:** What should I do if I'm unsure about my parcel status?

**Relevant docs:** [52]

**Retrieved docs:** [66, 67, 69, 68, 52, 94, 77, 41, 74, 42]

**Reranked docs:** [69, 52, 66, 67, 68, 41, 77, 42, 74, 94]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.200 | 0.500 | 0.387 | 0.631 |

### Question 26

**Query:** What happens if the parcel locker has no available space for my package?

**Relevant docs:** [65]

**Retrieved docs:** [65, 66, 64, 69, 56, 63, 68, 35, 77, 61]

**Reranked docs:** [63, 66, 69, 65, 68, 56, 64, 77, 61, 35]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 0.250 | 1.000 | 0.431 |

### Question 27

**Query:** Can I open a Discussion for a purchase made more than two years ago?

**Relevant docs:** [80]

**Retrieved docs:** [70, 80, 71, 81, 76, 7, 75, 77, 79]

**Reranked docs:** [80, 75, 76, 79, 81, 71, 70, 77, 7]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 28

**Query:** How can I collect my parcel from a parcel locker using a pick-up code or the HopShop app?

**Relevant docs:** [56]

**Retrieved docs:** [56, 55, 54, 53, 68, 64, 66, 63, 51, 57]

**Reranked docs:** [56, 54, 53, 55, 57, 51, 68, 66, 64, 63]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 29

**Query:** How can I share my HopShop Delivery pick-up code with someone else using the app?

**Relevant docs:** [54]

**Retrieved docs:** [54, 53, 68, 56, 47, 48, 64, 55, 50, 51]

**Reranked docs:** [54, 56, 53, 48, 47, 51, 50, 68, 55, 64]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 30

**Query:** How long does it take to get a refund to my bank account if I used a debit card?

**Relevant docs:** [86]

**Retrieved docs:** [86, 87, 88, 89, 90, 91, 92, 77, 93, 83]

**Reranked docs:** [86, 87, 89, 90, 91, 92, 88, 93, 77, 83]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 31

**Query:** How can I track my HopShop Delivery parcel and know when it's ready for collection?

**Relevant docs:** [51]

**Retrieved docs:** [41, 51, 42, 50, 58, 77, 53, 47, 56, 59]

**Reranked docs:** [41, 51, 53, 56, 42, 59, 77, 50, 47, 58]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 0.500 | 0.631 | 0.631 |

### Question 32

**Query:** How can I find out which delivery options are available for an item on HopShop?

**Relevant docs:** [36]

**Retrieved docs:** [36, 47, 40, 58, 50, 49, 51, 26, 15, 41]

**Reranked docs:** [36, 15, 47, 50, 51, 49, 26, 58, 41, 40]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 33

**Query:** Can I withdraw from the agreement if my account is older than 14 days?

**Relevant docs:** [10]

**Retrieved docs:** [9, 10, 11, 12, 7, 8, 77, 76, 80]

**Reranked docs:** [10, 9, 76, 11, 12, 8, 77, 7, 80]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 34

**Query:** How can I make a purchase or set up recurring orders on HopShop?

**Relevant docs:** [14]

**Retrieved docs:** [18, 14, 39, 15, 32, 50, 7, 48, 1]

**Reranked docs:** [14, 18, 15, 32, 7, 39, 50, 48, 1]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 35

**Query:** Can I split payment for multiple orders from different sellers?

**Relevant docs:** [30]

**Retrieved docs:** [24, 30, 28, 40, 26, 29, 41, 70, 67, 35]

**Reranked docs:** [24, 30, 40, 26, 28, 29, 41, 70, 35, 67]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 0.500 | 0.631 | 0.631 |

### Question 36

**Query:** How long does a seller have to respond to my complaint before it is considered upheld?

**Relevant docs:** [95]

**Retrieved docs:** [95, 77, 75, 93, 60, 59, 76, 82, 78]

**Reranked docs:** [95, 75, 60, 76, 82, 93, 77, 59, 78]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 37

**Query:** How can I enable sign-in with my email and password?

**Relevant docs:** [4]

**Retrieved docs:** [4, 2, 3, 41, 35, 77, 66, 6, 1]

**Reranked docs:** [4, 2, 3, 6, 77, 1, 41, 66, 35]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 38

**Query:** What are the ways to contact a seller on HopShop?

**Relevant docs:** [19]

**Retrieved docs:** [19, 21, 20, 93, 32, 36, 22, 14, 58, 48]

**Reranked docs:** [19, 22, 20, 32, 36, 93, 58, 14, 21, 48]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 39

**Query:** Where can I find the estimated delivery time for an offer?

**Relevant docs:** [46]

**Retrieved docs:** [46, 43, 37, 45, 44, 77, 67, 42, 38, 41]

**Reranked docs:** [46, 43, 37, 45, 44, 38, 77, 42, 41, 67]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 40

**Query:** Can I combine shipping costs when buying multiple items from different sellers?

**Relevant docs:** [40]

**Retrieved docs:** [40, 24, 26, 41, 39, 38, 28, 83, 67, 73]

**Reranked docs:** [40, 26, 24, 38, 73, 83, 28, 39, 41, 67]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 41

**Query:** What are the ways to register for a HopShop account?

**Relevant docs:** [1]

**Retrieved docs:** [1, 3, 2, 5, 7, 8, 14, 6, 48]

**Reranked docs:** [1, 2, 3, 5, 7, 6, 8, 14, 48]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 42

**Query:** Why isn't my usual pick-up point showing on the delivery map?

**Relevant docs:** [63]

**Retrieved docs:** [63, 64, 66, 55, 68, 53, 47, 54, 48, 46]

**Reranked docs:** [63, 64, 66, 46, 53, 48, 54, 68, 47, 55]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 43

**Query:** Why is my payment still pending after I paid by wire transfer through a third party?

**Relevant docs:** [34]

**Retrieved docs:** [34, 33, 91, 35, 77, 89, 29, 28, 71]

**Reranked docs:** [34, 33, 71, 91, 28, 35, 77, 89, 29]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 44

**Query:** What should I do if the product I received is defective?

**Relevant docs:** [94]

**Retrieved docs:** [94, 69, 67, 74, 68, 66, 96, 77, 93, 40]

**Reranked docs:** [94, 74, 69, 96, 77, 67, 66, 93, 68, 40]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 45

**Query:** How long does it take to get a refund on my credit card for a Mastercard or Visa?

**Relevant docs:** [87]

**Retrieved docs:** [87, 86, 88, 93, 83, 92, 90, 91, 89, 77]

**Reranked docs:** [87, 86, 90, 89, 91, 92, 93, 88, 77, 83]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 46

**Query:** What situations allow me to file a complaint about your delivery service?

**Relevant docs:** [60]

**Retrieved docs:** [60, 59, 95, 69, 74, 67, 77, 97, 48]

**Reranked docs:** [60, 59, 97, 69, 95, 77, 67, 48, 74]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 47

**Query:** How do I close my HopShop account?

**Relevant docs:** [8]

**Retrieved docs:** [8, 13, 7, 1, 12, 3, 6, 39, 10, 2]

**Reranked docs:** [8, 13, 12, 7, 2, 10, 6, 39, 3, 1]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 48

**Query:** Do I have to use the original packaging or include the receipt when sending a product back for a complaint?

**Relevant docs:** [96]

**Retrieved docs:** [96, 94, 60, 69, 59, 95, 97, 77, 82, 73]

**Reranked docs:** [96, 97, 82, 60, 59, 73, 69, 95, 94, 77]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 49

**Query:** How can I change the delivery date before my order is dispatched?

**Relevant docs:** [67]

**Retrieved docs:** [67, 77, 66, 78, 41, 40, 70, 46, 50]

**Reranked docs:** [67, 77, 78, 41, 66, 46, 40, 50, 70]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 50

**Query:** What should I do if my order delivery is delayed and I can't contact the seller?

**Relevant docs:** [77]

**Retrieved docs:** [67, 77, 74, 66, 68, 94, 40, 69, 70]

**Reranked docs:** [74, 77, 67, 70, 66, 69, 40, 68, 94]

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.111 | 0.111 | 1.000 | 1.000 | 0.500 | 0.500 | 0.631 | 0.631 |
