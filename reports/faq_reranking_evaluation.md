# FAQ Reranking Evaluation Report

Source notebook: `notebooks/09_faq_reranking.ipynb`

## Summary

- Evaluated questions: 50
- Mean precision@5: 0.198 -> 0.198
- Mean recall@5: 0.980 -> 0.980
- Mean MRR: 0.857 -> 0.910
- Mean nDCG@5: 0.889 -> 0.928

## Final Metrics

| questions | precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | 0.198 | 0.198 | 0.980 | 0.980 | 0.857 | 0.910 | 0.889 | 0.928 |

## Per-question Results

### Question 1

- Query: How do I register for a HopShop account using my email address?
- Relevant docs: [1]
- Retrieved docs: [1, 2, 6, 4, 49]
- Reranked docs: [1, 2, 49, 4, 6]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 2

- Query: How can I sign up using my Google or Facebook account?
- Relevant docs: [2]
- Retrieved docs: [2, 6, 1, 3, 75]
- Reranked docs: [2, 3, 1, 6, 75]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 3

- Query: How can I enable signing in with my email address and password?
- Relevant docs: [3]
- Retrieved docs: [3, 1, 2, 51, 49]
- Reranked docs: [3, 1, 2, 49, 51]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 4

- Query: How do I register for a HopShop account using my phone number?
- Relevant docs: [4]
- Retrieved docs: [4, 1, 2, 6]
- Reranked docs: [4, 1, 2, 6]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.250 | 0.250 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 5

- Query: How can I download my personal data from my HopShop account under GDPR?
- Relevant docs: [5]
- Retrieved docs: [5, 7, 8, 6, 11]
- Reranked docs: [5, 11, 6, 7, 8]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 6

- Query: Am I allowed to have multiple HopShop accounts, and are there any restrictions?
- Relevant docs: [6]
- Retrieved docs: [6, 50, 40, 46, 17]
- Reranked docs: [6, 40, 46, 17, 50]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 7

- Query: How do I close my HopShop account?
- Relevant docs: [7]
- Retrieved docs: [7, 16, 6, 14, 2]
- Reranked docs: [7, 16, 14, 6, 2]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 8

- Query: How can I withdraw from my agreement with HopShop?
- Relevant docs: [8]
- Retrieved docs: [9, 8, 10, 7, 14]
- Reranked docs: [9, 7, 8, 14, 10]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 0.333 | 0.631 | 0.500 |

### Question 9

- Query: Under what conditions can I withdraw from my agreement with HopShop?
- Relevant docs: [9]
- Retrieved docs: [9, 8, 10, 12, 13]
- Reranked docs: [9, 8, 12, 13, 10]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 10

- Query: How can I withdraw from my agreement and what happens to my account after I do?
- Relevant docs: [10]
- Retrieved docs: [10, 9, 15, 11, 13]
- Reranked docs: [10, 9, 11, 13, 15]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 11

- Query: What are the possible outcomes after I submit an account deletion request?
- Relevant docs: [11]
- Retrieved docs: [15, 11, 10, 6, 107]
- Reranked docs: [11, 10, 15, 6, 107]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 12

- Query: How can I terminate my agreement with HopShop?
- Relevant docs: [12]
- Retrieved docs: [14, 12, 13, 7, 8]
- Reranked docs: [14, 7, 12, 8, 13]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 0.333 | 0.631 | 0.500 |

### Question 13

- Query: When am I allowed to terminate the agreement?
- Relevant docs: [13]
- Retrieved docs: [13, 14, 9, 12, 8]
- Reranked docs: [13, 14, 9, 12, 8]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 14

- Query: How can I terminate my agreement with HopShop?
- Relevant docs: [14]
- Retrieved docs: [14, 12, 13, 7, 8]
- Reranked docs: [14, 7, 12, 8, 13]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 15

- Query: What happens after I submit my account termination application on HopShop?
- Relevant docs: [15]
- Retrieved docs: [11, 15, 12, 14, 7]
- Reranked docs: [15, 11, 14, 7, 12]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 16

- Query: What steps do I need to take before my notice period with HopShop ends?
- Relevant docs: [16]
- Retrieved docs: [16, 15, 12, 8, 7]
- Reranked docs: [16, 15, 7, 12, 8]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 17

- Query: How do I buy products or make recurring purchases on HopShop?
- Relevant docs: [17]
- Retrieved docs: [17, 26, 18, 25, 40]
- Reranked docs: [17, 26, 40, 18, 25]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 18

- Query: How can I purchase a product on HopShop?
- Relevant docs: [18]
- Retrieved docs: [18, 17, 51, 24, 6]
- Reranked docs: [17, 18, 6, 51, 24]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 |

### Question 19

- Query: How can I search for a specific product and filter the results?
- Relevant docs: [19]
- Retrieved docs: [19, 57, 18, 24, 23]
- Reranked docs: [19, 57, 23, 24, 18]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 20

- Query: How can I check a seller’s ratings and read the product description before buying?
- Relevant docs: [20]
- Retrieved docs: [20, 23, 29, 51, 50]
- Reranked docs: [20, 23, 29, 50, 51]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 21

- Query: What are the different ways I can buy a product?
- Relevant docs: [21]
- Retrieved docs: [21, 17, 18, 24, 50]
- Reranked docs: [21, 50, 24, 17, 18]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 22

- Query: How do I choose my delivery and payment options when placing an order?
- Relevant docs: [22]
- Retrieved docs: [34, 46, 50, 90, 22]
- Reranked docs: [22, 34, 50, 90, 46]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.200 | 1.000 | 0.387 | 1.000 |

### Question 23

- Query: How do I rate the seller and the product after making a purchase?
- Relevant docs: [23]
- Retrieved docs: [23, 20, 29, 94, 107]
- Reranked docs: [23, 29, 94, 20, 107]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 24

- Query: How can I repurchase an individual product from a previous order?
- Relevant docs: [24]
- Retrieved docs: [25, 24, 23, 26, 17]
- Reranked docs: [25, 23, 24, 26, 17]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 0.333 | 0.631 | 0.500 |

### Question 25

- Query: How can I reorder all items from a previous purchase?
- Relevant docs: [25]
- Retrieved docs: [25, 24, 78, 23, 51]
- Reranked docs: [25, 23, 24, 51, 78]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 26

- Query: How can I quickly reorder products I buy regularly?
- Relevant docs: [26]
- Retrieved docs: [25, 26, 50, 17, 24]
- Reranked docs: [26, 25, 24, 50, 17]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 27

- Query: What are the ways I can contact a seller on HopShop?
- Relevant docs: [27]
- Retrieved docs: [27, 29, 78, 77, 28]
- Reranked docs: [27, 28, 29, 78, 77]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 28

- Query: How can I contact a seller with a question about an item on HopShop?
- Relevant docs: [28]
- Retrieved docs: [27, 28, 29, 70, 40]
- Reranked docs: [28, 27, 40, 70, 29]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 29

- Query: How can I find the seller's contact information after making a purchase?
- Relevant docs: [29]
- Retrieved docs: [29, 27, 78, 77, 51]
- Reranked docs: [29, 27, 78, 77, 51]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 30

- Query: How can I contact a seller on HopShop without leaving the website or app?
- Relevant docs: [30]
- Retrieved docs: [27, 51, 30, 29, 62]
- Reranked docs: [30, 27, 51, 62, 29]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.333 | 1.000 | 0.500 | 1.000 |

### Question 31

- Query: What should I do if I have an issue with my order, like not receiving it or problems with returning it?
- Relevant docs: [31]
- Retrieved docs: [107, 90, 87, 78]
- Reranked docs: [87, 90, 107, 78]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 32

- Query: How can I pay for items from multiple sellers in a single transaction?
- Relevant docs: [32]
- Retrieved docs: [32, 36, 50, 34, 38]
- Reranked docs: [32, 36, 38, 34, 50]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 33

- Query: Can I choose just one delivery address and one set of VAT invoice details for my entire order?
- Relevant docs: [33]
- Retrieved docs: [33, 50, 49, 34, 36]
- Reranked docs: [33, 34, 49, 50, 36]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 34

- Query: How do I choose a delivery option when buying from one or multiple sellers?
- Relevant docs: [34]
- Retrieved docs: [34, 50, 32, 36, 22]
- Reranked docs: [34, 50, 32, 36, 22]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 35

- Query: How is the delivery cost calculated if there are or aren't price lists in the seller's offers?
- Relevant docs: [35]
- Retrieved docs: [35, 48, 50, 34, 60]
- Reranked docs: [35, 48, 50, 60, 34]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 36

- Query: How can I pay for both auction items and buy now purchases together in a single payment?
- Relevant docs: [36]
- Retrieved docs: [36, 37, 32, 24, 38]
- Reranked docs: [36, 37, 32, 24, 38]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 37

- Query: Can I use installments or HopShop Pay to pay for auction items?
- Relevant docs: [37]
- Retrieved docs: [37, 36, 32, 22, 6]
- Reranked docs: [37, 36, 22, 6, 32]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 38

- Query: Can I split the payment for multiple orders or orders from the same seller?
- Relevant docs: [38]
- Retrieved docs: [32, 38, 36, 50, 37]
- Reranked docs: [32, 38, 50, 36, 37]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 0.500 | 0.631 | 0.631 |

### Question 39

- Query: How do I pay for my order using PayPal, and how does currency conversion work?
- Relevant docs: [39]
- Retrieved docs: [39, 38, 90, 79, 32]
- Reranked docs: [39, 38, 32, 90, 79]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 40

- Query: How can I use a HopShop gift card to make a purchase on HopShop.pl or the app?
- Relevant docs: [40]
- Retrieved docs: [40, 105, 17, 62]
- Reranked docs: [40, 105, 17, 62]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.250 | 0.250 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 41

- Query: Why is my payment marked as pending or canceled?
- Relevant docs: [41]
- Retrieved docs: [41, 44, 43, 45, 42]
- Reranked docs: [41, 44, 43, 42, 45]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 42

- Query: What should I do if my payment was canceled and I want to retry or get a refund?
- Relevant docs: [42]
- Retrieved docs: [42, 45, 41, 78, 77]
- Reranked docs: [42, 41, 45, 78, 77]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 43

- Query: What should I do if my payment status is stuck on Pending?
- Relevant docs: [43]
- Retrieved docs: [44, 41, 43, 78, 45]
- Reranked docs: [44, 43, 41, 45, 78]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.333 | 0.500 | 0.500 | 0.631 |

### Question 44

- Query: Why is my payment still pending, and what should I do if I paid by wire transfer or directly to the seller's bank account?
- Relevant docs: [44]
- Retrieved docs: [44, 41, 104, 78, 102]
- Reranked docs: [44, 41, 104, 102, 78]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 45

- Query: How can I retry a payment that didn’t go through?
- Relevant docs: [45]
- Retrieved docs: [45, 43, 42, 37, 41]
- Reranked docs: [45, 42, 43, 37, 41]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 46

- Query: How can I find out what delivery options are available for a product on HopShop?
- Relevant docs: [46]
- Retrieved docs: [46, 58, 61, 18, 60]
- Reranked docs: [46, 58, 61, 60, 18]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 47

- Query: How is the delivery time provided for each offer?
- Relevant docs: [47]
- Retrieved docs: [47, 56, 53, 54, 55]
- Reranked docs: [47, 56, 53, 54, 55]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 48

- Query: How can I find out the delivery cost for a product?
- Relevant docs: [48]
- Retrieved docs: [48, 35, 50, 78, 51]
- Reranked docs: [48, 35, 50, 51, 78]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 49

- Query: How can I add or change my shipping address on HopShop when placing an order?
- Relevant docs: [49]
- Retrieved docs: [49, 61, 77, 90, 51]
- Reranked docs: [49, 90, 61, 51, 77]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 50

- Query: How does delivery work if I buy multiple products, possibly from different sellers?
- Relevant docs: [50]
- Retrieved docs: [50, 32, 34, 48, 25]
- Reranked docs: [50, 34, 32, 25, 48]

| precision@5 | RERANKED_precision@5 | recall@5 | RERANKED_recall@5 | mrr | RERANKED_mrr | ndcg@5 | RERANKED_ndcg@5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

