# FAQ Retrieval Evaluation Report

Source notebook: `notebooks/08_faq_retrieving.ipynb`

## Summary

- Evaluated questions: 50
- Mean precision@5: 0.198
- Mean recall@5: 0.980
- Mean MRR: 0.857
- Mean nDCG@5: 0.889
- Mean context relevance: 0.960

## Final Metrics

| row | precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- | --- |
| mean | 0.198 | 0.980 | 0.857 | 0.889 | 0.960 |

## Per-question Results

### Question 1/50

**Query:** How do I register for a HopShop account using my email address?

**Relevant docs:** `[1]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 1 | How to register with an email | 1.000 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 2 | no | 2 | How to register with Google or Facebook account | 0.757 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 3 | no | 6 | Can I have more than one HopShop account | 0.678 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 4 | no | 4 | How to register with your phone number | 0.672 | How to register with your phone number Open the registration page. Select whether you want to create a regular or business account. Select Contact number and enter your phone nu... |
| 5 | no | 49 | How to provide shipping details? | 0.598 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |

### Question 2/50

**Query:** How can I sign up using my Google or Facebook account?

**Relevant docs:** `[2]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 2 | How to register with Google or Facebook account | 1.000 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 2 | no | 6 | Can I have more than one HopShop account | 0.393 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 3 | no | 1 | How to register with an email | 0.348 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 4 | no | 3 | Signing in with a password and email address | 0.317 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Passwo... |
| 5 | no | 75 | How to find a pick-up point or parcel locker closest to my location? | 0.298 | How to find a pick-up point or parcel locker closest to my location? You will find the address of the nearest pick-up point or parcel locker in the Delivery and payment form, in... |

### Question 3/50

**Query:** How can I enable signing in with my email address and password?

**Relevant docs:** `[3]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 3 | Signing in with a password and email address | 1.000 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Passwo... |
| 2 | no | 1 | How to register with an email | 0.500 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 3 | no | 2 | How to register with Google or Facebook account | 0.414 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 4 | no | 51 | How can I track a parcel? | 0.276 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 5 | no | 49 | How to provide shipping details? | 0.275 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |

### Question 4/50

**Query:** How do I register for a HopShop account using my phone number?

**Relevant docs:** `[4]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.250 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 4 | How to register with your phone number | 0.998 | How to register with your phone number Open the registration page. Select whether you want to create a regular or business account. Select Contact number and enter your phone nu... |
| 2 | yes | 4 | How to register with your phone number | 0.747 | your account within 3 business days, and return a bank transfer amount entirely to your bank account. Bank transfer - if your bank is not on the list of available banks, select ... |
| 3 | no | 1 | How to register with an email | 0.730 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password... |
| 4 | no | 2 | How to register with Google or Facebook account | 0.720 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |
| 5 | no | 6 | Can I have more than one HopShop account | 0.597 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |

### Question 5/50

**Query:** How can I download my personal data from my HopShop account under GDPR?

**Relevant docs:** `[5]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 5 | GDPR — how you can download your personal data from the HopShop account. | 1.000 | GDPR — how you can download your personal data from the HopShop account. On the Copies of your data page, you can download the personal data gathered throughout your activity on... |
| 2 | no | 7 | How to close your HopShop account | 0.402 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 3 | no | 8 | Withdrawing from the agreement with HopShop | 0.343 | Withdrawing from the agreement with HopShop |
| 4 | no | 6 | Can I have more than one HopShop account | 0.342 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 5 | no | 11 | What happens next | 0.329 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will co... |

### Question 6/50

**Query:** Am I allowed to have multiple HopShop accounts, and are there any restrictions?

**Relevant docs:** `[6]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 6 | Can I have more than one HopShop account | 1.000 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 2 | no | 50 | I am buying many products — which delivery method should I choose? | 0.469 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 3 | no | 40 | HopShop gift cards | 0.348 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 4 | no | 46 | Delivery options on HopShop | 0.338 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 5 | no | 17 | How to buy on HopShop | 0.328 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |

### Question 7/50

**Query:** How do I close my HopShop account?

**Relevant docs:** `[7]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 7 | How to close your HopShop account | 1.000 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 2 | no | 16 | What you should do before the notice period ends | 0.621 | What you should do before the notice period ends Pay any arrears to HopShop. If you have an open invoice account ― settle the balance on the HopShop account, and close it in the... |
| 3 | no | 6 | Can I have more than one HopShop account | 0.557 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 4 | no | 14 | How to terminate the agreement | 0.525 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 5 | no | 2 | How to register with Google or Facebook account | 0.465 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will au... |

### Question 8/50

**Query:** How can I withdraw from my agreement with HopShop?

**Relevant docs:** `[8]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 9 | When you can withdraw from the agreement | 0.944 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account... |
| 2 | yes | 8 | Withdrawing from the agreement with HopShop | 0.776 | Withdrawing from the agreement with HopShop |
| 3 | no | 10 | How to withdraw from the agreement | 0.710 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 4 | no | 7 | How to close your HopShop account | 0.664 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 5 | no | 14 | How to terminate the agreement | 0.631 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |

### Question 9/50

**Query:** Under what conditions can I withdraw from my agreement with HopShop?

**Relevant docs:** `[9]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 9 | When you can withdraw from the agreement | 0.989 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account... |
| 2 | no | 8 | Withdrawing from the agreement with HopShop | 0.776 | Withdrawing from the agreement with HopShop |
| 3 | no | 10 | How to withdraw from the agreement | 0.632 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 4 | no | 12 | Termination of the agreement with HopShop | 0.632 | Termination of the agreement with HopShop |
| 5 | no | 13 | When you can terminate the agreement | 0.570 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |

### Question 10/50

**Query:** How can I withdraw from my agreement and what happens to my account after I do?

**Relevant docs:** `[10]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 10 | How to withdraw from the agreement | 1.000 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 2 | no | 9 | When you can withdraw from the agreement | 0.889 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account... |
| 3 | no | 15 | What happens next | 0.646 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your accoun... |
| 4 | no | 11 | What happens next | 0.641 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will co... |
| 5 | no | 13 | When you can terminate the agreement | 0.596 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |

### Question 11/50

**Query:** What are the possible outcomes after I submit an account deletion request?

**Relevant docs:** `[11]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 15 | What happens next | 0.880 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your accoun... |
| 2 | yes | 11 | What happens next | 0.777 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will co... |
| 3 | no | 10 | How to withdraw from the agreement | 0.679 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the ap... |
| 4 | no | 6 | Can I have more than one HopShop account | 0.580 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |
| 5 | no | 107 | I have received a defective product. What should I do? | 0.569 | I have received a defective product. What should I do? |

### Question 12/50

**Query:** How can I terminate my agreement with HopShop?

**Relevant docs:** `[12]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 14 | How to terminate the agreement | 0.997 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 2 | yes | 12 | Termination of the agreement with HopShop | 0.723 | Termination of the agreement with HopShop |
| 3 | no | 13 | When you can terminate the agreement | 0.716 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |
| 4 | no | 7 | How to close your HopShop account | 0.714 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 5 | no | 8 | Withdrawing from the agreement with HopShop | 0.697 | Withdrawing from the agreement with HopShop |

### Question 13/50

**Query:** When am I allowed to terminate the agreement?

**Relevant docs:** `[13]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 13 | When you can terminate the agreement | 1.000 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |
| 2 | no | 14 | How to terminate the agreement | 0.769 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 3 | no | 9 | When you can withdraw from the agreement | 0.591 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account... |
| 4 | no | 12 | Termination of the agreement with HopShop | 0.468 | Termination of the agreement with HopShop |
| 5 | no | 8 | Withdrawing from the agreement with HopShop | 0.413 | Withdrawing from the agreement with HopShop |

### Question 14/50

**Query:** How can I terminate my agreement with HopShop?

**Relevant docs:** `[14]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 14 | How to terminate the agreement | 0.997 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 2 | no | 12 | Termination of the agreement with HopShop | 0.723 | Termination of the agreement with HopShop |
| 3 | no | 13 | When you can terminate the agreement | 0.716 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |
| 4 | no | 7 | How to close your HopShop account | 0.715 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 5 | no | 8 | Withdrawing from the agreement with HopShop | 0.697 | Withdrawing from the agreement with HopShop |

### Question 15/50

**Query:** What happens after I submit my account termination application on HopShop?

**Relevant docs:** `[15]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 11 | What happens next | 0.999 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will co... |
| 2 | yes | 15 | What happens next | 0.962 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your accoun... |
| 3 | no | 12 | Termination of the agreement with HopShop | 0.804 | Termination of the agreement with HopShop |
| 4 | no | 14 | How to terminate the agreement | 0.709 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 5 | no | 7 | How to close your HopShop account | 0.665 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |

### Question 16/50

**Query:** What steps do I need to take before my notice period with HopShop ends?

**Relevant docs:** `[16]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 16 | What you should do before the notice period ends | 1.000 | What you should do before the notice period ends Pay any arrears to HopShop. If you have an open invoice account ― settle the balance on the HopShop account, and close it in the... |
| 2 | no | 15 | What happens next | 0.530 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your accoun... |
| 3 | no | 12 | Termination of the agreement with HopShop | 0.421 | Termination of the agreement with HopShop |
| 4 | no | 8 | Withdrawing from the agreement with HopShop | 0.416 | Withdrawing from the agreement with HopShop |
| 5 | no | 7 | How to close your HopShop account | 0.412 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |

### Question 17/50

**Query:** How do I buy products or make recurring purchases on HopShop?

**Relevant docs:** `[17]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 17 | How to buy on HopShop | 0.905 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 2 | no | 26 | How to make recurring purchases | 0.833 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the ... |
| 3 | no | 18 | How to buy a product on HopShop | 0.654 | How to buy a product on HopShop |
| 4 | no | 25 | How to buy again all products from a previous order | 0.534 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the p... |
| 5 | no | 40 | HopShop gift cards | 0.473 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |

### Question 18/50

**Query:** How can I purchase a product on HopShop?

**Relevant docs:** `[18]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 18 | How to buy a product on HopShop | 0.978 | How to buy a product on HopShop |
| 2 | no | 17 | How to buy on HopShop | 0.840 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 3 | no | 51 | How can I track a parcel? | 0.705 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 4 | no | 24 | How to buy again a single product | 0.700 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 5 | no | 6 | Can I have more than one HopShop account | 0.681 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |

### Question 19/50

**Query:** How can I search for a specific product and filter the results?

**Relevant docs:** `[19]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 19 | 1. Find the product you need | 1.000 | 1. Find the product you need Use the search engine to find the product you are looking for. You can use sorting options and filters to better match your search results. |
| 2 | no | 57 | Additional information | 0.537 | Additional information You can filter search results by the estimated delivery time. In exceptional situations, such as Christmas or extreme weather conditions, the estimated de... |
| 3 | no | 18 | How to buy a product on HopShop | 0.515 | How to buy a product on HopShop |
| 4 | no | 24 | How to buy again a single product | 0.508 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 5 | no | 23 | 5. Rate the seller and the product | 0.498 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the t... |

### Question 20/50

**Query:** How can I check a seller’s ratings and read the product description before buying?

**Relevant docs:** `[20]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 20 | 2. Read the product description and seller’s ratings | 1.000 | 2. Read the product description and seller’s ratings Go to the selected offer — read the product description and check its parameters. Check the information about delivery optio... |
| 2 | no | 23 | 5. Rate the seller and the product | 0.419 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the t... |
| 3 | no | 29 | The seller's contact information | 0.408 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 4 | no | 51 | How can I track a parcel? | 0.331 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 5 | no | 50 | I am buying many products — which delivery method should I choose? | 0.330 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |

### Question 21/50

**Query:** What are the different ways I can buy a product?

**Relevant docs:** `[21]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 21 | 3. Select the way of purchasing the product | 0.805 | 3. Select the way of purchasing the product Make an instant purchase — click [buy and pay] and skip the delivery and payment form because we automatically complete delivery deta... |
| 2 | no | 17 | How to buy on HopShop | 0.765 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 3 | no | 18 | How to buy a product on HopShop | 0.748 | How to buy a product on HopShop |
| 4 | no | 24 | How to buy again a single product | 0.727 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 5 | no | 50 | I am buying many products — which delivery method should I choose? | 0.666 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |

### Question 22/50

**Query:** How do I choose my delivery and payment options when placing an order?

**Relevant docs:** `[22]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.200 | 0.387 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 34 | How to choose a delivery option | 0.947 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 2 | no | 46 | Delivery options on HopShop | 0.864 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 3 | no | 50 | I am buying many products — which delivery method should I choose? | 0.846 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 90 | I have been waiting a long time for my order delivery | 0.714 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | yes | 22 | 4. Select the delivery option and payment method | 0.694 | 4. Select the delivery option and payment method Complete the delivery and payment form — select the payment method and delivery option. If you pay in advance, use HopShop Finan... |

### Question 23/50

**Query:** How do I rate the seller and the product after making a purchase?

**Relevant docs:** `[23]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 23 | 5. Rate the seller and the product | 1.000 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the t... |
| 2 | no | 20 | 2. Read the product description and seller’s ratings | 0.555 | 2. Read the product description and seller’s ratings Go to the selected offer — read the product description and check its parameters. Check the information about delivery optio... |
| 3 | no | 29 | The seller's contact information | 0.489 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 4 | no | 94 | How to open a Discussion | 0.474 | How to open a Discussion In the Purchase History tab, select the order for which you want to open a Discussion. Go to purchase details and click [report purchase problems]. In t... |
| 5 | no | 107 | I have received a defective product. What should I do? | 0.458 | I have received a defective product. What should I do? |

### Question 24/50

**Query:** How can I repurchase an individual product from a previous order?

**Relevant docs:** `[24]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 25 | How to buy again all products from a previous order | 0.977 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the p... |
| 2 | yes | 24 | How to buy again a single product | 0.748 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 3 | no | 23 | 5. Rate the seller and the product | 0.604 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the t... |
| 4 | no | 26 | How to make recurring purchases | 0.448 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the ... |
| 5 | no | 17 | How to buy on HopShop | 0.448 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |

### Question 25/50

**Query:** How can I reorder all items from a previous purchase?

**Relevant docs:** `[25]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 25 | How to buy again all products from a previous order | 1.000 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the p... |
| 2 | no | 24 | How to buy again a single product | 0.476 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 3 | no | 78 | I want to change the delivery day. What should I do? | 0.461 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 4 | no | 23 | 5. Rate the seller and the product | 0.451 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the t... |
| 5 | no | 51 | How can I track a parcel? | 0.440 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 26/50

**Query:** How can I quickly reorder products I buy regularly?

**Relevant docs:** `[26]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 25 | How to buy again all products from a previous order | 0.846 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the p... |
| 2 | yes | 26 | How to make recurring purchases | 0.832 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the ... |
| 3 | no | 50 | I am buying many products — which delivery method should I choose? | 0.724 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 17 | How to buy on HopShop | 0.646 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 5 | no | 24 | How to buy again a single product | 0.600 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |

### Question 27/50

**Query:** What are the ways I can contact a seller on HopShop?

**Relevant docs:** `[27]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 27 | How to contact the seller | 1.000 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through th... |
| 2 | no | 29 | The seller's contact information | 0.639 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 3 | no | 78 | I want to change the delivery day. What should I do? | 0.630 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 4 | no | 77 | I want to change the pick-up point or parcel locker. What should I do? | 0.595 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 5 | no | 28 | Ask a question | 0.547 | Ask a question If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, you need to... |

### Question 28/50

**Query:** How can I contact a seller with a question about an item on HopShop?

**Relevant docs:** `[28]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 27 | How to contact the seller | 0.985 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through th... |
| 2 | yes | 28 | Ask a question | 0.961 | Ask a question If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, you need to... |
| 3 | no | 29 | The seller's contact information | 0.596 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 4 | no | 70 | How to file a complaint about an HopShop Delivery parcel | 0.578 | How to file a complaint about an HopShop Delivery parcel You can file a complaint about an HopShop Delivery parcel through our complaint form — regardless of the delivery option... |
| 5 | no | 40 | HopShop gift cards | 0.541 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |

### Question 29/50

**Query:** How can I find the seller's contact information after making a purchase?

**Relevant docs:** `[29]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 29 | The seller's contact information | 1.000 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 2 | no | 27 | How to contact the seller | 0.603 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through th... |
| 3 | no | 78 | I want to change the delivery day. What should I do? | 0.514 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 4 | no | 77 | I want to change the pick-up point or parcel locker. What should I do? | 0.459 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 5 | no | 51 | How can I track a parcel? | 0.457 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 30/50

**Query:** How can I contact a seller on HopShop without leaving the website or app?

**Relevant docs:** `[30]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.333 | 0.500 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 27 | How to contact the seller | 1.000 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through th... |
| 2 | no | 51 | How can I track a parcel? | 0.666 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |
| 3 | yes | 30 | The Message Center | 0.662 | The Message Center If you do not want to exit the HopShop website or app, contact the seller through the Message Center. It is really easy to use, as it combines the convenience... |
| 4 | no | 29 | The seller's contact information | 0.650 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After sig... |
| 5 | no | 62 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.573 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |

### Question 31/50

**Query:** What should I do if I have an issue with my order, like not receiving it or problems with returning it?

**Relevant docs:** `[31]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 107 | I have received a defective product. What should I do? | 1.000 | I have received a defective product. What should I do? |
| 2 | no | 90 | I have been waiting a long time for my order delivery | 0.900 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 3 | no | 90 | I have been waiting a long time for my order delivery | 0.791 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 4 | no | 87 | What you should do if you do not receive your order | 0.770 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery decl... |
| 5 | no | 78 | I want to change the delivery day. What should I do? | 0.722 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |

### Question 32/50

**Query:** How can I pay for items from multiple sellers in a single transaction?

**Relevant docs:** `[32]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 32 | How to pay for orders made from multiple sellers | 1.000 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 2 | no | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.522 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 3 | no | 50 | I am buying many products — which delivery method should I choose? | 0.514 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 34 | How to choose a delivery option | 0.478 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 5 | no | 38 | How to split the payment | 0.430 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |

### Question 33/50

**Query:** Can I choose just one delivery address and one set of VAT invoice details for my entire order?

**Relevant docs:** `[33]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 33 | One delivery address | 1.000 | One delivery address Select one delivery address and one set of VAT invoice details for the whole order. |
| 2 | no | 50 | I am buying many products — which delivery method should I choose? | 0.521 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 3 | no | 49 | How to provide shipping details? | 0.455 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |
| 4 | no | 34 | How to choose a delivery option | 0.413 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 5 | no | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.352 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |

### Question 34/50

**Query:** How do I choose a delivery option when buying from one or multiple sellers?

**Relevant docs:** `[34]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 34 | How to choose a delivery option | 0.967 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 2 | no | 50 | I am buying many products — which delivery method should I choose? | 0.964 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 3 | no | 32 | How to pay for orders made from multiple sellers | 0.798 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 4 | no | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.547 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 5 | no | 22 | 4. Select the delivery option and payment method | 0.524 | 4. Select the delivery option and payment method Complete the delivery and payment form — select the payment method and delivery option. If you pay in advance, use HopShop Finan... |

### Question 35/50

**Query:** How is the delivery cost calculated if there are or aren't price lists in the seller's offers?

**Relevant docs:** `[35]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 35 | Determine the delivery cost | 1.000 | Determine the delivery cost If the seller has set price lists in all the offers, we will automatically calculate the delivery cost. If there are no price lists in the offers, co... |
| 2 | no | 48 | How much does delivery cost? | 0.785 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packagin... |
| 3 | no | 50 | I am buying many products — which delivery method should I choose? | 0.559 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 34 | How to choose a delivery option | 0.447 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 5 | no | 60 | How much HopShop Delivery is | 0.442 | How much HopShop Delivery is Delivery within HopShop Smart! is free of charge. See the parcel prices outside HopShop Smart! in the table below: You can pay on delivery if a sell... |

### Question 36/50

**Query:** How can I pay for both auction items and buy now purchases together in a single payment?

**Relevant docs:** `[36]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 1.000 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 2 | no | 37 | Payment methods | 0.660 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 3 | no | 32 | How to pay for orders made from multiple sellers | 0.605 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 4 | no | 24 | How to buy again a single product | 0.509 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: ... |
| 5 | no | 38 | How to split the payment | 0.495 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |

### Question 37/50

**Query:** Can I use installments or HopShop Pay to pay for auction items?

**Relevant docs:** `[37]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 0.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 37 | Payment methods | 0.860 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 2 | no | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.803 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 3 | no | 32 | How to pay for orders made from multiple sellers | 0.580 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 4 | no | 22 | 4. Select the delivery option and payment method | 0.524 | 4. Select the delivery option and payment method Complete the delivery and payment form — select the payment method and delivery option. If you pay in advance, use HopShop Finan... |
| 5 | no | 6 | Can I have more than one HopShop account | 0.517 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allo... |

### Question 38/50

**Query:** Can I split the payment for multiple orders or orders from the same seller?

**Relevant docs:** `[38]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.500 | 0.631 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 32 | How to pay for orders made from multiple sellers | 1.000 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 2 | yes | 38 | How to split the payment | 0.844 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |
| 3 | no | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.678 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one paym... |
| 4 | no | 50 | I am buying many products — which delivery method should I choose? | 0.491 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 5 | no | 37 | Payment methods | 0.484 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |

### Question 39/50

**Query:** How do I pay for my order using PayPal, and how does currency conversion work?

**Relevant docs:** `[39]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 39 | How to pay with PayPal | 1.000 | How to pay with PayPal When you are ready to pay for your order, go to the delivery and payment form. In the Payment method section, select PayPal. Click [buy and pay]. You will... |
| 2 | no | 38 | How to split the payment | 0.552 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to p... |
| 3 | no | 90 | I have been waiting a long time for my order delivery | 0.509 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can descr... |
| 4 | no | 79 | The pick-up code does not work. What should I do? | 0.471 | The pick-up code does not work. What should I do? Firstly, make sure you enter the correct pick-up code. You can find it in the order details in the My Parcels or Purchase Histo... |
| 5 | no | 32 | How to pay for orders made from multiple sellers | 0.466 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |

### Question 40/50

**Query:** How can I use a HopShop gift card to make a purchase on HopShop.pl or the app?

**Relevant docs:** `[40]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.250 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 40 | HopShop gift cards | 0.966 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you... |
| 2 | no | 105 | A gift card | 0.870 | A gift card If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to ma... |
| 3 | yes | 40 | HopShop gift cards | 0.647 | the email notification. How to get an invoice Check in the offer description if the seller issues invoices. If so ― tick the [I want to receive an invoice] box and provide relev... |
| 4 | no | 17 | How to buy on HopShop | 0.560 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purch... |
| 5 | no | 62 | How to check the status of an HopShop Delivery parcel and how to collect it | 0.532 | How to check the status of an HopShop Delivery parcel and how to collect it You can check your parcel status in several places: in the email, SMS, and notifications in the HopSh... |

### Question 41/50

**Query:** Why is my payment marked as pending or canceled?

**Relevant docs:** `[41]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 41 | Why your payment is pending or canceled | 1.000 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 2 | no | 44 | Other reasons why your payment may be pending | 0.742 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 3 | no | 43 | Note | 0.480 | Note Every payment starts with the Pending status. If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it: Open the Purc... |
| 4 | no | 45 | My payment has not gone through. How to retry the payment? | 0.463 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 5 | no | 42 | What to do next | 0.423 | What to do next If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] b... |

### Question 42/50

**Query:** What should I do if my payment was canceled and I want to retry or get a refund?

**Relevant docs:** `[42]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 42 | What to do next | 0.882 | What to do next If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] b... |
| 2 | no | 45 | My payment has not gone through. How to retry the payment? | 0.717 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 3 | no | 41 | Why your payment is pending or canceled | 0.664 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 4 | no | 78 | I want to change the delivery day. What should I do? | 0.659 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 5 | no | 77 | I want to change the pick-up point or parcel locker. What should I do? | 0.601 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |

### Question 43/50

**Query:** What should I do if my payment status is stuck on Pending?

**Relevant docs:** `[43]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 0.333 | 0.500 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | no | 44 | Other reasons why your payment may be pending | 0.817 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 2 | no | 41 | Why your payment is pending or canceled | 0.755 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 3 | yes | 43 | Note | 0.735 | Note Every payment starts with the Pending status. If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it: Open the Purc... |
| 4 | no | 78 | I want to change the delivery day. What should I do? | 0.625 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 5 | no | 45 | My payment has not gone through. How to retry the payment? | 0.611 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |

### Question 44/50

**Query:** Why is my payment still pending, and what should I do if I paid by wire transfer or directly to the seller's bank account?

**Relevant docs:** `[44]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 44 | Other reasons why your payment may be pending | 1.000 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for exa... |
| 2 | no | 41 | Why your payment is pending or canceled | 0.816 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |
| 3 | no | 104 | Wire transfer | 0.646 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email y... |
| 4 | no | 78 | I want to change the delivery day. What should I do? | 0.569 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 5 | no | 102 | Bank transfer | 0.559 | Bank transfer You will get the refund to the bank account you paid from for your purchase. You will be refunded within 3 business days. For the majority of banks, you will see t... |

### Question 45/50

**Query:** How can I retry a payment that didn’t go through?

**Relevant docs:** `[45]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 45 | My payment has not gone through. How to retry the payment? | 1.000 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the followi... |
| 2 | no | 43 | Note | 0.544 | Note Every payment starts with the Pending status. If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it: Open the Purc... |
| 3 | no | 42 | What to do next | 0.541 | What to do next If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] b... |
| 4 | no | 37 | Payment methods | 0.444 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where y... |
| 5 | no | 41 | Why your payment is pending or canceled | 0.384 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payme... |

### Question 46/50

**Query:** How can I find out what delivery options are available for a product on HopShop?

**Relevant docs:** `[46]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 46 | Delivery options on HopShop | 1.000 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Deliv... |
| 2 | no | 58 | The HopShop Delivery program — information for buyers | 0.794 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the progra... |
| 3 | no | 61 | How to order a parcel with HopShop Delivery | 0.643 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 4 | no | 18 | How to buy a product on HopShop | 0.629 | How to buy a product on HopShop |
| 5 | no | 60 | How much HopShop Delivery is | 0.617 | How much HopShop Delivery is Delivery within HopShop Smart! is free of charge. See the parcel prices outside HopShop Smart! in the table below: You can pay on delivery if a sell... |

### Question 47/50

**Query:** How is the delivery time provided for each offer?

**Relevant docs:** `[47]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 47 | What is the delivery time? | 1.000 | What is the delivery time? The estimated delivery time is usually a few days. We provide it separately for each offer as a specific date, a date range, or a number of days in mu... |
| 2 | no | 56 | Where you can see the estimated delivery time | 0.935 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer li... |
| 3 | no | 53 | Estimated delivery time | 0.793 | Estimated delivery time For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your... |
| 4 | no | 54 | How we calculate the estimated delivery time | 0.724 | How we calculate the estimated delivery time A dedicated algorithm calculates it based on the previous parcels of a given seller and carriers' deliveries. |
| 5 | no | 55 | The estimated delivery time may differ from the actual delivery time | 0.724 | The estimated delivery time may differ from the actual delivery time We calculate the estimated delivery time based on the available data. It may differ from the actual delivery... |

### Question 48/50

**Query:** How can I find out the delivery cost for a product?

**Relevant docs:** `[48]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 48 | How much does delivery cost? | 0.998 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packagin... |
| 2 | no | 35 | Determine the delivery cost | 0.821 | Determine the delivery cost If the seller has set price lists in all the offers, we will automatically calculate the delivery cost. If there are no price lists in the offers, co... |
| 3 | no | 50 | I am buying many products — which delivery method should I choose? | 0.717 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 4 | no | 78 | I want to change the delivery day. What should I do? | 0.548 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You ca... |
| 5 | no | 51 | How can I track a parcel? | 0.526 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 49/50

**Query:** How can I add or change my shipping address on HopShop when placing an order?

**Relevant docs:** `[49]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 49 | How to provide shipping details? | 1.000 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without reg... |
| 2 | no | 61 | How to order a parcel with HopShop Delivery | 0.669 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |
| 3 | no | 77 | I want to change the pick-up point or parcel locker. What should I do? | 0.650 | I want to change the pick-up point or parcel locker. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to change the pick-up point or p... |
| 4 | no | 90 | I have been waiting a long time for my order delivery | 0.635 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have... |
| 5 | no | 51 | How can I track a parcel? | 0.623 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in t... |

### Question 50/50

**Query:** How does delivery work if I buy multiple products, possibly from different sellers?

**Relevant docs:** `[50]`

Metrics:

| precision@5 | recall@5 | mrr | ndcg@5 | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | preview |
| --- | --- | --- | --- | --- | --- |
| 1 | yes | 50 | I am buying many products — which delivery method should I choose? | 0.954 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery... |
| 2 | no | 32 | How to pay for orders made from multiple sellers | 0.909 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automat... |
| 3 | no | 34 | How to choose a delivery option | 0.769 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you c... |
| 4 | no | 48 | How much does delivery cost? | 0.610 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packagin... |
| 5 | no | 25 | How to buy again all products from a previous order | 0.595 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the p... |
