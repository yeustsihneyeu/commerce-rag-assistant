# FAQ Answer Relevance Evaluation Report

Source notebook: `notebooks/13_faq_answer_relevance_evaluating.ipynb`

## Summary

- Evaluated questions: 50
- Mean answer relevance: 0.823

## Final Metrics

| row | answer_relevance |
| --- | --- |
| mean | 0.823 |

## Per-question Results

### Question 1/50

**Query:** How do I register for a HopShop account using my email address?

**Answer relevance:** 0.946

**Relevant docs:** `[1]`

**Retrieved docs:** `[1, 2, 49]`

**Reference answer:**

Open the registration page. Choose whether you want to hold a regular account or a business account.
Enter your email address and create a password.
Determine whether you are over 18 years old. If not, provide your exact date of birth. You will hold a Junior account which will be transformed into a regular account once you turn 18.
Accept the HopShop Terms & Conditions and click [register].
You will receive a confirmation email. Open your mailbox and click (confirm registration) to complete the registration process.
Once you complete the registration, we will redirect you to your new HopShop account. We will give you a default username ― you can change it in the Account details tab.

**Generated answer:**

To register for a HopShop account using your email address, open the registration page, enter your email and create a password. Indicate if you are over 18 (if not, provide your birth date). Accept the HopShop Terms & Conditions and click [register]. You will receive a confirmation email—open it and click (confirm registration) to complete the process.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 1 | How to register with an email | 8.545 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password. Determine whether you are over 18 year... |
| 2 | 2 | How to register with Google or Facebook account | 5.631 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will automatically redirect you to the registra... |
| 3 | 49 | How to provide shipping details? | 5.224 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without registering an HopShop account or you want ... |

### Question 2/50

**Query:** How can I sign up using my Google or Facebook account?

**Answer relevance:** 0.688

**Relevant docs:** `[2]`

**Retrieved docs:** `[2, 3, 1]`

**Reference answer:**

Open the sign in page.
Select signing in through Facebook or Google.
Sign in to your Facebook or Google account. Then, we will automatically redirect you to the registration page.
Determine whether you are over 18 years old. If not, provide your exact date of birth. You will hold a Junior account which will be transformed into a regular account once you turn 18.
Accept the HopShop Terms & Conditions and click [register].
Done! We will give you a default username― you can change it in the Account details tab.

**Generated answer:**

Open the sign in page and select signing in through Facebook or Google. Sign in to your Facebook or Google account, and you’ll be automatically redirected to the registration page. Confirm if you are over 18 years old (if not, provide your date of birth). Accept the HopShop Terms & Conditions and click [register]. You’ll get a default username that you can change later in the Account details tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 2 | How to register with Google or Facebook account | 7.531 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will automatically redirect you to the registra... |
| 2 | 3 | Signing in with a password and email address | -6.356 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Password tab. |
| 3 | 1 | How to register with an email | -8.537 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password. Determine whether you are over 18 year... |

### Question 3/50

**Query:** How can I enable signing in with my email address and password?

**Answer relevance:** 0.971

**Relevant docs:** `[3]`

**Retrieved docs:** `[3, 1, 2]`

**Reference answer:**

If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Password tab.

**Generated answer:**

To enable signing in with your email address and password, set a password in the Sign-in and Password tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 3 | Signing in with a password and email address | 6.654 | Signing in with a password and email address If you want to be able to sign in to your account with an email address and password, too ― set a password in the Sign-in and Password tab. |
| 2 | 1 | How to register with an email | 0.188 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password. Determine whether you are over 18 year... |
| 3 | 2 | How to register with Google or Facebook account | -5.282 | How to register with Google or Facebook account Open the sign in page. Select signing in through Facebook or Google. Sign in to your Facebook or Google account. Then, we will automatically redirect you to the registra... |

### Question 4/50

**Query:** How do I register for a HopShop account using my phone number?

**Answer relevance:** 0.959

**Relevant docs:** `[4]`

**Retrieved docs:** `[4, 4, 1]`

**Reference answer:**

Open the registration page. Select whether you want to create a regular or business account.
Select Contact number and enter your phone number.
Declare if you have turned 18 years old.
If you have yet to turn 18 years old, provide us with your date of birth. We will create a Junior account for you – it will be transformed into a regular account when you are 18 years old.
Check relevant consents and click [register].
Enter the activation code we have sent you by text message and click [finish registration]. We will redirect you to your brand new HopShop account with a default username. You can change it in the Account details tab.

**Generated answer:**

To register with your phone number, open the registration page and select whether you want a regular or business account. Enter your phone number and declare if you are over 18; if not, provide your date of birth for a Junior account. Check the relevant consents and click [register]. Enter the activation code sent to you by text message and click [finish registration]. You'll be redirected to your new HopShop account.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 4 | How to register with your phone number | 6.788 | your account within 3 business days, and return a bank transfer amount entirely to your bank account. Bank transfer - if your bank is not on the list of available banks, select the (Transfer from another bank) option.... |
| 2 | 4 | How to register with your phone number | 6.786 | How to register with your phone number Open the registration page. Select whether you want to create a regular or business account. Select Contact number and enter your phone number. Declare if you have turned 18 year... |
| 3 | 1 | How to register with an email | 6.161 | How to register with an email Open the registration page. Choose whether you want to hold a regular account or a business account. Enter your email address and create a password. Determine whether you are over 18 year... |

### Question 5/50

**Query:** How can I download my personal data from my HopShop account under GDPR?

**Answer relevance:** 1.000

**Relevant docs:** `[5]`

**Retrieved docs:** `[5, 11, 6]`

**Reference answer:**

On the Copies of your data page, you can download the personal data gathered throughout your activity on HopShop. This way, we make it possible for you to exercise two of your rights arising from the GDPR:
the right of access to your data
the right to data portability.
How you can download your data
Sign in to the HopShop account whose data you want to download.
Go to the Copies of your data page. You can also reach the page from the Account details tab.
Click [create a data copy].
Select the datasets that you want to download.
Select the format of the file with your data:
HTML ― recommended if you want to get the data in a clear, legible format
CSV ― recommended if you want to analyze the data or transfer it to another administrator.
Click [create a copy].
Depending on the amount, creating the data copy can last from several minutes to several days. We will let you know by email when the files are ready to be downloaded.
You will find the link for download in the email. You can do it within 7 days of receiving the email. After that time, you will need to create a report again.
What you can find in the specific datasets

**Generated answer:**

To download your personal data from your HopShop account under GDPR, sign in to your account, go to the Copies of your data page (found in the Account details tab), click [create a data copy], select the datasets and file format (HTML or CSV), and click [create a copy]. You’ll get an email when the files are ready to download.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 5 | GDPR — how you can download your personal data from the HopShop account. | 10.347 | GDPR — how you can download your personal data from the HopShop account. On the Copies of your data page, you can download the personal data gathered throughout your activity on HopShop. This way, we make it possible ... |
| 2 | 11 | What happens next | 0.338 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will completely and irreversibly delete your pe... |
| 3 | 6 | Can I have more than one HopShop account | 0.156 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allowed to use these accounts to violate the... |

### Question 6/50

**Query:** Am I allowed to have multiple HopShop accounts, and are there any restrictions?

**Answer relevance:** 0.912

**Relevant docs:** `[6]`

**Retrieved docs:** `[6, 40, 46]`

**Reference answer:**

Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allowed to use these accounts to violate the rules governing HopShop. It includes among others: making purchase offers in your own transactions outbidding your purchase offers made in transactions of other HopShop customers rating your own offers using additional accounts to bypass the HopShop fees and commissions system, and to avoid paying. These rules apply also to the accounts of people living together, working together, or using the same computer (especially family members, coworkers, and friends). In order to avoid confusion, transactions between these people should take place outside HopShop. If you use any of your accounts against the rules governing HopShop, all of your accounts (including your main account) may be suspended. If your account is suspended, you cannot create a new one unless we allow you to register again. Before that, you need to sort out the issue of your account suspension.

**Generated answer:**

Yes, you can have multiple HopShop accounts if you provide correct and valid personal information during registration. However, you must not use these accounts to violate HopShop rules, such as making purchase offers in your own transactions, outbidding your own offers, rating your own offers, or using extra accounts to avoid fees. Also, these rules apply to people living or working together or using the same computer. If you misuse accounts, all your accounts may be suspended.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 6 | Can I have more than one HopShop account | 6.827 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allowed to use these accounts to violate the... |
| 2 | 40 | HopShop gift cards | -5.000 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you have an HopShop gift card, you can use ... |
| 3 | 46 | Delivery options on HopShop | -6.807 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Delivery and payment section to check what de... |

### Question 7/50

**Query:** How do I close my HopShop account?

**Answer relevance:** 0.994

**Relevant docs:** `[7]`

**Retrieved docs:** `[7, 16, 14]`

**Reference answer:**

You can end your activity on HopShop by:
withdrawing from the agreement
terminating the agreement.

**Generated answer:**

You can close your HopShop account by submitting a termination application. Before the notice period ends, make sure to pay any arrears, settle and close your invoice account in the Invoices tab, and unsubscribe from any subscription in the Subscriptions tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 7 | How to close your HopShop account | 8.637 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 2 | 16 | What you should do before the notice period ends | 5.798 | What you should do before the notice period ends Pay any arrears to HopShop. If you have an open invoice account ― settle the balance on the HopShop account, and close it in the Invoices tab, or use the [contact us] b... |
| 3 | 14 | How to terminate the agreement | 3.528 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |

### Question 8/50

**Query:** How can I withdraw from my agreement with HopShop?

**Answer relevance:** 0.917

**Relevant docs:** `[8]`

**Retrieved docs:** `[9, 7, 8]`

**Reference answer:**


  Section_Id: 8

**Generated answer:**

You can withdraw from your agreement with HopShop if 14 days have not passed since you registered your account and you have no financial liabilities towards HopShop, such as sales fees.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 9 | When you can withdraw from the agreement | 7.624 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account was registered you have no financial li... |
| 2 | 7 | How to close your HopShop account | 6.424 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 3 | 8 | Withdrawing from the agreement with HopShop | 6.220 | Withdrawing from the agreement with HopShop |

### Question 9/50

**Query:** Under what conditions can I withdraw from my agreement with HopShop?

**Answer relevance:** 0.985

**Relevant docs:** `[9]`

**Retrieved docs:** `[9, 8, 12]`

**Reference answer:**

You can easily withdraw from the agreement with us ― without providing a reason ― if:
14 days have not passed since your HopShop account was registered
you have no financial liabilities towards us (for example, sales fees).

**Generated answer:**

You can withdraw from your agreement with HopShop if 14 days have not passed since your account was registered and you have no financial liabilities towards HopShop, such as sales fees.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 9 | When you can withdraw from the agreement | 7.023 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account was registered you have no financial li... |
| 2 | 8 | Withdrawing from the agreement with HopShop | 5.087 | Withdrawing from the agreement with HopShop |
| 3 | 12 | Termination of the agreement with HopShop | 1.631 | Termination of the agreement with HopShop |

### Question 10/50

**Query:** How can I withdraw from my agreement and what happens to my account after I do?

**Answer relevance:** 0.834

**Relevant docs:** `[10]`

**Retrieved docs:** `[10, 9, 11]`

**Reference answer:**

To withdraw from the agreement, submit this application. You will then get a confirmation email from us.
You will not be able to submit the application for an account older than 14 days or submit multiple applications for the same account. If you try to do it, we will display a message with a hint.
You will lose access to your account immediately after submitting the application. We will log you out and you will not sign in again.

**Generated answer:**

To withdraw from the agreement, submit the application. You will get a confirmation email, and you will immediately lose access to your account, being logged out. If there were no sales or purchases, your personal details will be deleted. If there were, your data will be stored until the purchase or sale is processed.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 10 | How to withdraw from the agreement | 6.271 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the application for an account older than 14 d... |
| 2 | 9 | When you can withdraw from the agreement | 3.931 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account was registered you have no financial li... |
| 3 | 11 | What happens next | 0.940 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will completely and irreversibly delete your pe... |

### Question 11/50

**Query:** What are the possible outcomes after I submit an account deletion request?

**Answer relevance:** 0.670

**Relevant docs:** `[11]`

**Retrieved docs:** `[11, 10, 15]`

**Reference answer:**

Usually, we consider the application right away ― within minutes. It may take us up to 7 days.
If there were no sales or purchases on your account ― we will completely and irreversibly delete your personal details from our systems.
If you have made a purchase or listed an offer on that account ― we will store your data until that purchase or sale has been processed. In that case, you may use the second option: termination of agreement with HopShop.
If we find that you do not meet the conditions above (for example, you made a purchase or listed an offer on that account) ― we will reject your application and you will regain access to your account. We will inform you about it by email. If that is the case, you can use the other option ― terminating the agreement.

**Generated answer:**

After you submit an account deletion request, your application is usually considered within minutes, but it may take up to 7 days. If there were no sales or purchases on your account, your personal details will be completely and irreversibly deleted. If you have made a purchase or listed an offer, your data will be stored until the transaction is processed, or you can choose to terminate the agreement. If you don't meet the conditions (e.g., you made a purchase), your application will be rejected and you will regain account access. You will be informed by email.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 11 | What happens next | -5.082 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will completely and irreversibly delete your pe... |
| 2 | 10 | How to withdraw from the agreement | -5.160 | How to withdraw from the agreement To withdraw from the agreement, submit this application. You will then get a confirmation email from us. You will not be able to submit the application for an account older than 14 d... |
| 3 | 15 | What happens next | -5.824 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your account and finalize the open purchases, aucti... |

### Question 12/50

**Query:** How can I terminate my agreement with HopShop?

**Answer relevance:** 0.999

**Relevant docs:** `[12]`

**Retrieved docs:** `[14, 7, 12]`

**Reference answer:**

Section_Id: 12

**Generated answer:**

To terminate your agreement with HopShop, submit the termination application. That will end the agreement you entered when you created the account.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 14 | How to terminate the agreement | 7.528 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 2 | 7 | How to close your HopShop account | 7.484 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 3 | 12 | Termination of the agreement with HopShop | 5.250 | Termination of the agreement with HopShop |

### Question 13/50

**Query:** When am I allowed to terminate the agreement?

**Answer relevance:** 0.841

**Relevant docs:** `[13]`

**Retrieved docs:** `[13, 14, 9]`

**Reference answer:**

You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement.

**Generated answer:**

You can terminate the agreement at any time, even if you no longer meet the conditions for withdrawing from the agreement.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 13 | When you can terminate the agreement | 6.762 | When you can terminate the agreement You can terminate the agreement any time ― also if you no longer meet the conditions of withdrawing from the agreement. |
| 2 | 14 | How to terminate the agreement | 1.896 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 3 | 9 | When you can withdraw from the agreement | -0.332 | When you can withdraw from the agreement You can easily withdraw from the agreement with us ― without providing a reason ― if: 14 days have not passed since your HopShop account was registered you have no financial li... |

### Question 14/50

**Query:** How can I terminate my agreement with HopShop?

**Answer relevance:** 1.000

**Relevant docs:** `[14]`

**Retrieved docs:** `[14, 7, 12]`

**Reference answer:**

To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account.

**Generated answer:**

To terminate your agreement with HopShop, submit the termination application. That will end the agreement you entered when creating your account.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 14 | How to terminate the agreement | 7.528 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |
| 2 | 7 | How to close your HopShop account | 7.484 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |
| 3 | 12 | Termination of the agreement with HopShop | 5.250 | Termination of the agreement with HopShop |

### Question 15/50

**Query:** What happens after I submit my account termination application on HopShop?

**Answer relevance:** 0.578

**Relevant docs:** `[15]`

**Retrieved docs:** `[15, 11, 14]`

**Reference answer:**

From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your account and finalize the open purchases, auctions or Discussions. However, you will not be able to use most of the features on HopShop, such as making purchases or listing offers, among others. Within the first 7 days of the notice period, we will remove all offers you listed. We will also stop sending you email notifications, for example, about replies in Discussions. After 60 days, your agreement will be terminated. We will remove your personal details after the time indicated in the Privacy protection policy.

**Generated answer:**

From the moment you submit the application, a 60-day notice period begins. During this time, you can sign in to your account and finalize open purchases, auctions, or Discussions, but you cannot use most features like making new purchases or listing offers. All your offers will be removed within the first 7 days, and you will stop receiving email notifications. After 60 days, your agreement will be terminated and your personal details will be removed after the period stated in the Privacy protection policy.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 15 | What happens next | 7.290 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your account and finalize the open purchases, aucti... |
| 2 | 11 | What happens next | 5.593 | What happens next Usually, we consider the application right away ― within minutes. It may take us up to 7 days. If there were no sales or purchases on your account ― we will completely and irreversibly delete your pe... |
| 3 | 14 | How to terminate the agreement | 4.610 | How to terminate the agreement To terminate the agreement with HopShop, submit this application. That will terminate the agreement you entered with us when you created the account. |

### Question 16/50

**Query:** What steps do I need to take before my notice period with HopShop ends?

**Answer relevance:** 0.712

**Relevant docs:** `[16]`

**Retrieved docs:** `[16, 15, 7]`

**Reference answer:**

Pay any arrears to HopShop.
If you have an open invoice account ― settle the balance on the HopShop account, and close it in the Invoices tab, or use the [contact us] button below this article.
If you have a Subscription ― unsubscribe in the Subscriptions tab.

**Generated answer:**

Before your notice period ends, you should pay any arrears to HopShop, settle and close any open invoice accounts in the Invoices tab, and unsubscribe from any Subscriptions in the Subscriptions tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 16 | What you should do before the notice period ends | 6.069 | What you should do before the notice period ends Pay any arrears to HopShop. If you have an open invoice account ― settle the balance on the HopShop account, and close it in the Invoices tab, or use the [contact us] b... |
| 2 | 15 | What happens next | 3.038 | What happens next From the moment you submit the application, we will start counting the notice period of 60 days. During that period, you will be able to sign in to your account and finalize the open purchases, aucti... |
| 3 | 7 | How to close your HopShop account | -1.861 | How to close your HopShop account You can end your activity on HopShop by: withdrawing from the agreement terminating the agreement. |

### Question 17/50

**Query:** How do I buy products or make recurring purchases on HopShop?

**Answer relevance:** 0.856

**Relevant docs:** `[17]`

**Retrieved docs:** `[17, 26, 40]`

**Reference answer:**

In this article, you will learn
how to buy a product on HopShop
how to buy the same product or all products from an order again
how to make recurring purchases.
Buying on HopShop is simple and you can do it in several ways — depending on your needs.

**Generated answer:**

To buy products on HopShop, add the items to your cart and follow the steps to provide delivery and payment details, then click [buy and pay]. For recurring purchases, use the "Buy Again" tab in the menu—select your preferred products and add them to your cart for quick re-ordering.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 17 | How to buy on HopShop | 6.800 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purchases. Buying on HopShop is simple and yo... |
| 2 | 26 | How to make recurring purchases | 6.774 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the homepage. The Buy Again tab features pro... |
| 3 | 40 | HopShop gift cards | 3.419 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you have an HopShop gift card, you can use ... |

### Question 18/50

**Query:** How can I purchase a product on HopShop?

**Answer relevance:** 0.000

**Relevant docs:** `[18]`

**Retrieved docs:** `[17, 18, 6]`

**Reference answer:**

How to buy a product on HopShop

**Generated answer:**

Buying on HopShop is simple and you can do it in several ways, depending on your needs.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 17 | How to buy on HopShop | 6.937 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purchases. Buying on HopShop is simple and yo... |
| 2 | 18 | How to buy a product on HopShop | 5.612 | How to buy a product on HopShop |
| 3 | 6 | Can I have more than one HopShop account | 3.077 | Can I have more than one HopShop account Yes, you can have a few accounts, as long as you provide correct and valid personal information at registration. However, it is not allowed to use these accounts to violate the... |

### Question 19/50

**Query:** How can I search for a specific product and filter the results?

**Answer relevance:** 0.720

**Relevant docs:** `[19]`

**Retrieved docs:** `[19, 57, 23]`

**Reference answer:**

Use the search engine to find the product you are looking for. You can use sorting options and filters to better match your search results.

**Generated answer:**

Use the search engine to find the product you are looking for. You can use sorting options and filters, including filtering by estimated delivery time, to better match your search results.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 19 | 1. Find the product you need | 4.871 | 1. Find the product you need Use the search engine to find the product you are looking for. You can use sorting options and filters to better match your search results. |
| 2 | 57 | Additional information | -0.209 | Additional information You can filter search results by the estimated delivery time. In exceptional situations, such as Christmas or extreme weather conditions, the estimated delivery time might be longer. The estimat... |
| 3 | 23 | 5. Rate the seller and the product | -7.191 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the transaction and leave a comment. Apart fr... |

### Question 20/50

**Query:** How can I check a seller’s ratings and read the product description before buying?

**Answer relevance:** 0.624

**Relevant docs:** `[20]`

**Retrieved docs:** `[20, 23, 29]`

**Reference answer:**

Go to the selected offer — read the product description and check its parameters. Check the information about delivery options. If you want, you can also check information about warranties, complaints, and return options. If you have any doubts, you can ask the seller a question through the Ask a question option
You can also read product reviews if other buyers have already left any.
Check the seller’s reviews — read the ratings and comments from their customers.

**Generated answer:**

Go to the selected offer — read the product description and check its parameters. You can also check the seller’s ratings and read the ratings and comments from their customers.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 20 | 2. Read the product description and seller’s ratings | 8.230 | 2. Read the product description and seller’s ratings Go to the selected offer — read the product description and check its parameters. Check the information about delivery options. If you want, you can also check info... |
| 2 | 23 | 5. Rate the seller and the product | 4.802 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the transaction and leave a comment. Apart fr... |
| 3 | 29 | The seller's contact information | 1.751 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After signing in, you can also check that informa... |

### Question 21/50

**Query:** What are the different ways I can buy a product?

**Answer relevance:** 0.928

**Relevant docs:** `[21]`

**Retrieved docs:** `[21, 50, 24]`

**Reference answer:**

Make an instant purchase — click [buy and pay] and skip the delivery and payment form because we automatically complete delivery details and payment method for you — based on your purchase history.
Add the product to cart — you can add different products, select your favorite delivery option and payment method, and pay for all products simultaneously.
Win an auction — if a given offer comes in that format — enter the maximum amount you are willing to pay and click [place a bid]. You will buy the product if your suggested price is the highest when the auction ends.

**Generated answer:**

You can buy a product in three ways:
1. Make an instant purchase by clicking [buy and pay].
2. Add the product to your cart and pay for all selected products at once.
3. Win an auction by entering your bid and clicking [place a bid].

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 21 | 3. Select the way of purchasing the product | 5.679 | 3. Select the way of purchasing the product Make an instant purchase — click [buy and pay] and skip the delivery and payment form because we automatically complete delivery details and payment method for you — based o... |
| 2 | 50 | I am buying many products — which delivery method should I choose? | 2.594 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |
| 3 | 24 | How to buy again a single product | 0.475 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: [to cart] — click to add the product to ... |

### Question 22/50

**Query:** How do I choose my delivery and payment options when placing an order?

**Answer relevance:** 0.617

**Relevant docs:** `[22]`

**Retrieved docs:** `[22, 34, 50]`

**Reference answer:**

Complete the delivery and payment form — select the payment method and delivery option.
If you pay in advance, use HopShop Finance. You can pay with a card or select one of the banks. If your bank is not on the list, you can pay with a card or a bank transfer. We will confirm the payment with an email sent to you and the seller or sellers.

**Generated answer:**

Complete the delivery and payment form by selecting your preferred payment method and delivery option. You can pay with a card or via bank transfer using HopShop Finance. For delivery, choose among the available options for each order. If buying from multiple sellers, select a delivery method for each order separately.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 22 | 4. Select the delivery option and payment method | 6.273 | 4. Select the delivery option and payment method Complete the delivery and payment form — select the payment method and delivery option. If you pay in advance, use HopShop Finance. You can pay with a card or select on... |
| 2 | 34 | How to choose a delivery option | 5.750 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you can choose different delivery options for... |
| 3 | 50 | I am buying many products — which delivery method should I choose? | 2.689 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |

### Question 23/50

**Query:** How do I rate the seller and the product after making a purchase?

**Answer relevance:** 0.831

**Relevant docs:** `[23]`

**Retrieved docs:** `[23, 29, 94]`

**Reference answer:**

You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the transaction and leave a comment. Apart from rating the seller, you can also rate the product you bought.

**Generated answer:**

You can leave a rating after purchasing the product by clicking [rate the seller] next to your order. You can rate particular elements of the transaction and leave a comment. You can also rate the product you bought.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 23 | 5. Rate the seller and the product | 8.672 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the transaction and leave a comment. Apart fr... |
| 2 | 29 | The seller's contact information | 1.952 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After signing in, you can also check that informa... |
| 3 | 94 | How to open a Discussion | 0.596 | How to open a Discussion In the Purchase History tab, select the order for which you want to open a Discussion. Go to purchase details and click [report purchase problems]. In the next step, select the Discussion reas... |

### Question 24/50

**Query:** How can I repurchase an individual product from a previous order?

**Answer relevance:** 1.000

**Relevant docs:** `[24]`

**Retrieved docs:** `[25, 23, 24]`

**Reference answer:**

Go to the Purchase History tab.
Click [purchase details] next to the selected order.
Under each product in that order, you will see 2 buttons:
[to cart] — click to add the product to cart
[buy now] — click to go to the form where you can select the delivery option and payment method.
If the offer with the product you selected is already inactive, we will show you other offers with the same product.

**Generated answer:**

To repurchase an individual product from a previous order, go to the Purchase History tab, click [purchase details] next to the selected order, and under each product you'll see [to cart] and [buy now] buttons. Use one of these to repurchase the product.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 25 | How to buy again all products from a previous order | 0.641 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the product list. We will redirect you to the... |
| 2 | 23 | 5. Rate the seller and the product | -3.827 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the transaction and leave a comment. Apart fr... |
| 3 | 24 | How to buy again a single product | -6.375 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: [to cart] — click to add the product to ... |

### Question 25/50

**Query:** How can I reorder all items from a previous purchase?

**Answer relevance:** 0.706

**Relevant docs:** `[25]`

**Retrieved docs:** `[25, 23, 24]`

**Reference answer:**

Go to the Purchase History tab.
Click [purchase details] next to the selected order.
Click [buy everything again] under the product list.
We will redirect you to the delivery and payment form so that you can finalize the purchase.
You can also buy those products again from the list of purchases:
Go to the Purchase History tab.
Click three dots next to a given product and select [buy again].
We will redirect you to the delivery and payment form where you can select the preferred payment method and delivery option.

**Generated answer:**

Go to the Purchase History tab, click [purchase details] next to the selected order, then click [buy everything again] under the product list. You will be redirected to the delivery and payment form to finalize your purchase.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 25 | How to buy again all products from a previous order | 5.453 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the product list. We will redirect you to the... |
| 2 | 23 | 5. Rate the seller and the product | -1.978 | 5. Rate the seller and the product You can leave a rating after purchasing the product. Click [rate the seller] next to a given order — you can rate particular elements of the transaction and leave a comment. Apart fr... |
| 3 | 24 | How to buy again a single product | -4.944 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: [to cart] — click to add the product to ... |

### Question 26/50

**Query:** How can I quickly reorder products I buy regularly?

**Answer relevance:** 1.000

**Relevant docs:** `[26]`

**Retrieved docs:** `[26, 25, 24]`

**Reference answer:**

If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the homepage.
The Buy Again tab features products we selected based on your purchase history. You can always reach them easily and quickly buy again. All you need to do is click [add to cart] next to the product you want to buy. If you click [All offers from PLN xx], you will go to all offers linked to a given product. Select the one you like the most.

**Generated answer:**

You can quickly reorder products you buy regularly by going to the Buy Again tab in the menu on the homepage. There you'll find products based on your purchase history and can easily add them to your cart for fast reordering.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 26 | How to make recurring purchases | 6.055 | How to make recurring purchases If you buy a particular product regularly, you can do it even more easily — through the Buy Again tab. To get to the tab, expand the menu on the homepage. The Buy Again tab features pro... |
| 2 | 25 | How to buy again all products from a previous order | -1.729 | How to buy again all products from a previous order Go to the Purchase History tab. Click [purchase details] next to the selected order. Click [buy everything again] under the product list. We will redirect you to the... |
| 3 | 24 | How to buy again a single product | -3.257 | How to buy again a single product Go to the Purchase History tab. Click [purchase details] next to the selected order. Under each product in that order, you will see 2 buttons: [to cart] — click to add the product to ... |

### Question 27/50

**Query:** What are the ways I can contact a seller on HopShop?

**Answer relevance:** 0.975

**Relevant docs:** `[27]`

**Retrieved docs:** `[27, 28, 29]`

**Reference answer:**

You can contact the seller on HopShop in a few ways:
by clicking [Ask a question] on the offer page
directly, with their contact information
through the Message Center
by opening a Discussion.

**Generated answer:**

You can contact a seller on HopShop by:

1. Clicking "Ask a question" on the offer page (you need to sign in, except for classified ads).
2. Using the Message Center.
3. Opening a Discussion.
4. Using the seller's contact information provided after your purchase or on the offer page if available.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 27 | How to contact the seller | 8.864 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through the Message Center by opening a Discussion. |
| 2 | 28 | Ask a question | 5.983 | Ask a question If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, you need to sign in to your HopShop account. Classi... |
| 3 | 29 | The seller's contact information | -0.576 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After signing in, you can also check that informa... |

### Question 28/50

**Query:** How can I contact a seller with a question about an item on HopShop?

**Answer relevance:** 0.618

**Relevant docs:** `[28]`

**Retrieved docs:** `[28, 27, 40]`

**Reference answer:**

If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, you need to sign in to your HopShop account.
Classified ads are an exception ― in this case, you can find the seller's phone number and the Ask a question feature to the right of the photo. You do not need to sign in to your HopShop account to contact the seller in this way.

**Generated answer:**

You can contact the seller by clicking [Ask a question] on the offer page. To send a question, you need to sign in to your HopShop account. For classified ads, you can also use the seller's phone number or the Ask a question feature without signing in.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 28 | Ask a question | 8.392 | Ask a question If you want to ask the seller about an item or offer before placing an order, use the Ask a question feature on the offer page. To send in a question, you need to sign in to your HopShop account. Classi... |
| 2 | 27 | How to contact the seller | 7.624 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through the Message Center by opening a Discussion. |
| 3 | 40 | HopShop gift cards | 3.182 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you have an HopShop gift card, you can use ... |

### Question 29/50

**Query:** How can I find the seller's contact information after making a purchase?

**Answer relevance:** 1.000

**Relevant docs:** `[29]`

**Retrieved docs:** `[29, 27, 78]`

**Reference answer:**

After completing each transaction, we will email you the seller's contact information, including their email address and phone number.
After signing in, you can also check that information:
before making the purchase — on the offer page, in the Contact sub-section of the About Seller section (if the seller provided contact details)
after making the purchase — when you click [purchase details] next to a given order in the Purchase History tab.

**Generated answer:**

After making a purchase, you can find the seller's contact information by clicking [purchase details] next to your order in the Purchase History tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 29 | The seller's contact information | 9.413 | The seller's contact information After completing each transaction, we will email you the seller's contact information, including their email address and phone number. After signing in, you can also check that informa... |
| 2 | 27 | How to contact the seller | 3.743 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through the Message Center by opening a Discussion. |
| 3 | 78 | I want to change the delivery day. What should I do? | 3.040 | I want to change the delivery day. What should I do? If the seller has yet to dispatch your parcel — contact them and ask them to dispatch the parcel on a different date. You can find the seller's contact information ... |

### Question 30/50

**Query:** How can I contact a seller on HopShop without leaving the website or app?

**Answer relevance:** 0.895

**Relevant docs:** `[30]`

**Retrieved docs:** `[30, 27, 51]`

**Reference answer:**

If you do not want to exit the HopShop website or app, contact the seller through the Message Center.
It is really easy to use, as it combines the convenience of the chat and the possibilities of the email. You will be notified of the new messages, and you will be able to access them for 6 months after contacting the seller.

**Generated answer:**

You can contact the seller through the Message Center on HopShop without leaving the website or app.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 30 | The Message Center | 8.194 | The Message Center If you do not want to exit the HopShop website or app, contact the seller through the Message Center. It is really easy to use, as it combines the convenience of the chat and the possibilities of th... |
| 2 | 27 | How to contact the seller | 5.730 | How to contact the seller You can contact the seller on HopShop in a few ways: by clicking [Ask a question] on the offer page directly, with their contact information through the Message Center by opening a Discussion. |
| 3 | 51 | How can I track a parcel? | 0.035 | How can I track a parcel? You can track your parcel if: you complete the delivery and payment form when paying via HopShop Finance the seller has provided a tracking number in the payment card. If those conditions are... |

### Question 31/50

**Query:** What should I do if I have an issue with my order, like not receiving it or problems with returning it?

**Answer relevance:** 0.919

**Relevant docs:** `[31]`

**Retrieved docs:** `[87, 90, 90]`

**Reference answer:**

If the product you ordered does not conform with the contract, you have not received the parcel, or you have problems with returning your order — open a Discussion in which you can solve your problem with the seller.
Provide all information and attach all files necessary to explain the situation in the Discussion. The seller has 24 hours (excluding Saturdays, Sundays, and bank holidays) to reply to you. You can also ask us to enter the Discussion and help you solve the problem.

**Generated answer:**

If you have not received your order or have another issue (like problems with returning it), open a Discussion. There, you can describe your issue and attach all necessary documents, receipts, and photos. This will help resolve your problem faster. If needed, you can ask for further assistance during the Discussion.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 87 | What you should do if you do not receive your order | 5.319 | What you should do if you do not receive your order If you do not receive your order, firstly, make sure that the seller has received your payment the deadline for delivery declared in the offer has not been met. Cont... |
| 2 | 90 | I have been waiting a long time for my order delivery | 1.302 | are and how they work If you have not received your order, the item does not match the description, or the delivery cost does not add up - open a Discussion. There you can describe the issue, and attach all necessary ... |
| 3 | 90 | I have been waiting a long time for my order delivery | -0.706 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have provided in the form ― find the relevan... |

### Question 32/50

**Query:** How can I pay for items from multiple sellers in a single transaction?

**Answer relevance:** 1.000

**Relevant docs:** `[32]`

**Retrieved docs:** `[32, 36, 38]`

**Reference answer:**

In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers.

**Generated answer:**

To pay for items from multiple sellers in a single transaction, buy them through a cart. The payment will be automatically divided among the sellers.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 32 | How to pay for orders made from multiple sellers | 6.742 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |
| 2 | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 1.910 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one payment if: you can see them in the Purchase... |
| 3 | 38 | How to split the payment | 0.267 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to pay for your order ― information for buye... |

### Question 33/50

**Query:** Can I choose just one delivery address and one set of VAT invoice details for my entire order?

**Answer relevance:** 0.959

**Relevant docs:** `[33]`

**Retrieved docs:** `[33, 34, 49]`

**Reference answer:**

Select one delivery address and one set of VAT invoice details for the whole order.

**Generated answer:**

Yes, you can select one delivery address and one set of VAT invoice details for the whole order.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 33 | One delivery address | 8.102 | One delivery address Select one delivery address and one set of VAT invoice details for the whole order. |
| 2 | 34 | How to choose a delivery option | -2.621 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you can choose different delivery options for... |
| 3 | 49 | How to provide shipping details? | -3.960 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without registering an HopShop account or you want ... |

### Question 34/50

**Query:** How do I choose a delivery option when buying from one or multiple sellers?

**Answer relevance:** 0.868

**Relevant docs:** `[34]`

**Retrieved docs:** `[34, 50, 32]`

**Reference answer:**

If you buy at least two items:
from the same seller ― select a delivery option that is available for all the offers
from multiple sellers ― you can choose different delivery options for each order.

**Generated answer:**

If you buy from the same seller, select a delivery option that is available for all the offers. If you buy from multiple sellers, you can choose different delivery options for each order.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 34 | How to choose a delivery option | 8.100 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you can choose different delivery options for... |
| 2 | 50 | I am buying many products — which delivery method should I choose? | 5.080 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |
| 3 | 32 | How to pay for orders made from multiple sellers | 2.293 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |

### Question 35/50

**Query:** How is the delivery cost calculated if there are or aren't price lists in the seller's offers?

**Answer relevance:** 0.902

**Relevant docs:** `[35]`

**Retrieved docs:** `[35, 48, 50]`

**Reference answer:**

If the seller has set price lists in all the offers, we will automatically calculate the delivery cost. If there are no price lists in the offers, contact the seller and negotiate the total delivery cost.

**Generated answer:**

If the seller has set price lists in all the offers, the delivery cost is calculated automatically. If there are no price lists, you need to contact the seller and negotiate the total delivery cost.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 35 | Determine the delivery cost | 8.150 | Determine the delivery cost If the seller has set price lists in all the offers, we will automatically calculate the delivery cost. If there are no price lists in the offers, contact the seller and negotiate the total... |
| 2 | 48 | How much does delivery cost? | 2.639 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packaging costs are included in the product pric... |
| 3 | 50 | I am buying many products — which delivery method should I choose? | 1.319 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |

### Question 36/50

**Query:** How can I pay for both auction items and buy now purchases together in a single payment?

**Answer relevance:** 0.978

**Relevant docs:** `[36]`

**Retrieved docs:** `[36, 37, 32]`

**Reference answer:**

You can pay for items from an auction or an offer with the buy now option in one payment if:
you can see them in the Purchase History tab
their status is unpaid.
If you win an auction, you will find the item you bid in the Purchase History tab. There, the item will have the unpaid status until you pay for it.
If you buy with the buy now option, we will ask you to pay after you choose the delivery and payment method. To do it, click [buy and pay]. We will redirect you to the payment page. Once you confirm your payment, we will mark your purchase as paid in the Purchase History tab. Then, you will not be able to link this payment with the payment for an item bought from auction.
If you want to pay for all orders in one payment, do not finalize the payment for the buy now purchase. You can pay for all orders in the following way:
Select an item you want to buy and click [buy now].
Enter the delivery address and choose the delivery option.
Choose the payment method: a wire transfer, a payment card or a BLIK code.

**Generated answer:**

To pay for both auction items and buy now purchases together in a single payment, make sure both orders are visible as unpaid in your Purchase History. Do not finalize payment for the buy now purchase right away. Once both orders are marked as unpaid, select them in the Purchase History tab and click [retry the payment] to pay for them together.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 6.440 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one payment if: you can see them in the Purchase... |
| 2 | 37 | Payment methods | 4.999 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where you can confirm your payment. Close it. T... |
| 3 | 32 | How to pay for orders made from multiple sellers | -1.608 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |

### Question 37/50

**Query:** Can I use installments or HopShop Pay to pay for auction items?

**Answer relevance:** 0.922

**Relevant docs:** `[37]`

**Retrieved docs:** `[37, 36, 22]`

**Reference answer:**

You cannot link payment with installments or HopShop Pay to the payment for items from an auction.
Click [buy and pay].
We will redirect you to a website where you can confirm your payment. Close it. This way, you will not pay for your order.
You will see the following note in the Purchase History tab.
After a few minutes you will see your payment status. If the order is not paid for, you will see the cancel payment option. Click it.
We will move this order to the Purchase History tab and mark it as unpaid.
In the Purchase History tab, select the orders you want to pay for with one payment. You can then select items purchased in an auction and with the buy now option.
Click [retry the payment].
Select the payment method and pay for your purchase.

**Generated answer:**

You cannot link payment with installments or HopShop Pay to the payment for items from an auction.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 37 | Payment methods | 8.052 | Payment methods You cannot link payment with installments or HopShop Pay to the payment for items from an auction. Click [buy and pay]. We will redirect you to a website where you can confirm your payment. Close it. T... |
| 2 | 36 | How to pay with one payment for orders from an auction and an offer with the buy now option | 0.612 | How to pay with one payment for orders from an auction and an offer with the buy now option You can pay for items from an auction or an offer with the buy now option in one payment if: you can see them in the Purchase... |
| 3 | 22 | 4. Select the delivery option and payment method | 0.514 | 4. Select the delivery option and payment method Complete the delivery and payment form — select the payment method and delivery option. If you pay in advance, use HopShop Finance. You can pay with a card or select on... |

### Question 38/50

**Query:** Can I split the payment for multiple orders or orders from the same seller?

**Answer relevance:** 0.867

**Relevant docs:** `[38]`

**Retrieved docs:** `[32, 38, 50]`

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

You can split the payment for multiple orders by selecting only the orders you want to pay for in the Purchase History tab and clicking [pay]. However, you cannot split payment for an order from the same seller.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 32 | How to pay for orders made from multiple sellers | 6.577 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |
| 2 | 38 | How to split the payment | 5.861 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to pay for your order ― information for buye... |
| 3 | 50 | I am buying many products — which delivery method should I choose? | -0.377 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |

### Question 39/50

**Query:** How do I pay for my order using PayPal, and how does currency conversion work?

**Answer relevance:** 0.691

**Relevant docs:** `[39]`

**Retrieved docs:** `[39, 38, 32]`

**Reference answer:**

When you are ready to pay for your order, go to the delivery and payment form.
In the Payment method section, select PayPal.
Click [buy and pay].
You will be redirected to the PayPal website. Follow the instructions there to pay. Done!
How currency conversion works
Depending on the currency you choose to pay in and the currency of the funds on your bank account:
if the payment currency and your bank account currency are the same ― you are charged the price in this currency
if the payment currency and your bank account currency are different ― the card issuer converts the payment into your bank account currency.
Examples
You want to pay in EUR. The currency of money on your card is EUR. When you pay, you will pay in EUR ― with no currency conversion needed.
You want to pay in PLN. The currency of the funds on your card is EUR. When you pay, the bank will convert the payment currency from PLN into EUR.
The conversion rate is calculated by PayU ― the payment service provider ― and updated daily.

**Generated answer:**

To pay with PayPal, select PayPal as your payment method in the delivery and payment form, then click [buy and pay]. You will be redirected to the PayPal website to complete the payment.

For currency conversion: 
- If your bank account currency matches the payment currency, you pay in that currency with no conversion.
- If they are different, your card issuer will convert the payment currency to your bank account currency using a daily-updated rate calculated by PayU.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 39 | How to pay with PayPal | 7.778 | How to pay with PayPal When you are ready to pay for your order, go to the delivery and payment form. In the Payment method section, select PayPal. Click [buy and pay]. You will be redirected to the PayPal website. Fo... |
| 2 | 38 | How to split the payment | 0.207 | How to split the payment In the Purchase History tab, tick only those orders you want to pay for and click [pay]. You cannot split payment for an order from one seller. How to pay for your order ― information for buye... |
| 3 | 32 | How to pay for orders made from multiple sellers | -3.986 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |

### Question 40/50

**Query:** How can I use a HopShop gift card to make a purchase on HopShop.pl or the app?

**Answer relevance:** 0.763

**Relevant docs:** `[40]`

**Retrieved docs:** `[40, 105, 17]`

**Reference answer:**

If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you have an HopShop gift card, you can use it on HopShop.pl or in the HopShop mobile app.

**Generated answer:**

You can use your HopShop gift card to make a purchase on HopShop.pl or in the HopShop mobile app. Just select it as your payment method during the transaction.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 40 | HopShop gift cards | 7.175 | HopShop gift cards If you are not sure what to buy someone as a gift, choose the HopShop gift card. The recipient will decide by themselves what they want to buy with it. If you have an HopShop gift card, you can use ... |
| 2 | 105 | A gift card | 4.087 | A gift card If you return an order for which you have paid with a gift card, we will increase its value by the refund amount. We will assign it to the HopShop account used to make the purchase. The terms of use and ex... |
| 3 | 17 | How to buy on HopShop | 1.623 | How to buy on HopShop In this article, you will learn how to buy a product on HopShop how to buy the same product or all products from an order again how to make recurring purchases. Buying on HopShop is simple and yo... |

### Question 41/50

**Query:** Why is my payment marked as pending or canceled?

**Answer relevance:** 0.808

**Relevant docs:** `[41]`

**Retrieved docs:** `[41, 44, 43]`

**Reference answer:**

Your payment may have the Canceled status if:
the payment has not been made through HopShop Finance within 10 days of selecting the payment method
you have canceled your payment (in this case, we will refund you to the bank account you paid from)
the bank has not accepted your payment
a PayU S.A. or PayPro S.A. employee has canceled your payment (it may happen if the payment is suspected to be incorrect).
If you cancel your payment, the seller will not get funds. Remember that the seller may still expect you to finalize the transaction.

**Generated answer:**

Your payment may be pending or canceled for several reasons:

- Payment not made through HopShop Finance within 10 days.
- You canceled your payment.
- The bank did not accept your payment.
- A PayU S.A. or PayPro S.A. employee canceled your payment due to suspected issues.
- If you paid by wire transfer, transfer time depends on the third party and is settled within 3 days.
- Direct payment to the seller's account stays pending for 10 days, then is canceled if not processed via HopShop.
- Your payment method may be temporarily unavailable.
- Technical issues may have occurred.

If the status does not change, check if your bank account was charged and retry the payment from your Purchase History.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 41 | Why your payment is pending or canceled | 8.517 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payment method you have canceled your payment... |
| 2 | 44 | Other reasons why your payment may be pending | 7.335 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time ... |
| 3 | 43 | Note | 0.172 | Note Every payment starts with the Pending status. If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it: Open the Purchase History tab. Click [retry payment] ... |

### Question 42/50

**Query:** What should I do if my payment was canceled and I want to retry or get a refund?

**Answer relevance:** 0.855

**Relevant docs:** `[42]`

**Retrieved docs:** `[42, 41, 45]`

**Reference answer:**

If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] by the unpaid order.
If the payment is Canceled and your bank account has been charged, you will get a refund to the same bank account.

**Generated answer:**

If your payment was canceled and your bank account was not charged, you can retry payment in the Purchase History tab by clicking [retry payment] next to the unpaid order. If your bank account was charged, you will get a refund to the same bank account.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 42 | What to do next | 8.061 | What to do next If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] by the unpaid order. If the payment is Ca... |
| 2 | 41 | Why your payment is pending or canceled | 3.105 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payment method you have canceled your payment... |
| 3 | 45 | My payment has not gone through. How to retry the payment? | 2.590 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the following statuses: If the seller has refunded ... |

### Question 43/50

**Query:** What should I do if my payment status is stuck on Pending?

**Answer relevance:** 1.000

**Relevant docs:** `[43]`

**Retrieved docs:** `[44, 43, 41]`

**Reference answer:**

Every payment starts with the Pending status.
If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it:
Open the Purchase History tab.
Click [retry payment] by the unpaid order.
Select the delivery and payment method ― you can choose different methods than before.

**Generated answer:**

If your payment status is stuck on Pending, check if your bank account has been charged. If not, retry the payment in the Purchase History tab, and select your preferred delivery and payment method.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 44 | Other reasons why your payment may be pending | 5.740 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time ... |
| 2 | 43 | Note | 5.336 | Note Every payment starts with the Pending status. If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it: Open the Purchase History tab. Click [retry payment] ... |
| 3 | 41 | Why your payment is pending or canceled | 5.307 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payment method you have canceled your payment... |

### Question 44/50

**Query:** Why is my payment still pending, and what should I do if I paid by wire transfer or directly to the seller's bank account?

**Answer relevance:** 0.539

**Relevant docs:** `[44]`

**Retrieved docs:** `[44, 41, 104]`

**Reference answer:**

If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time depends on that party. Such payment is settled within 3 days ― do not retry the payment earlier. If you do, you will cancel your previous payment and it will be transferred back to the institution which made the transfer. If that is the case, and the institution does not have your funds, contact us.
If you pay for your order directly to the seller's bank account ― your payment will have the Pending status for 10 days. After this time, the payment will be canceled automatically, because it has not been made through HopShop.
Your payment method may be unavailable in a given moment - check the time your bank makes online transfers on the bank's website.
There have been technical issues with your payment.
If you have chosen to pay by a wire transfer in the delivery and payment form, and you want to issue an online transfer ― we will generate details on which you should make the transfer.

**Generated answer:**

If you paid by wire transfer, the payment can take up to 3 days to settle. Do not retry the payment earlier, as it may cancel the previous one.  
If you paid directly to the seller’s bank account, the payment will have the Pending status for 10 days. After this time, it will be canceled automatically.

If you need further help, please call the support center at +48 123123123.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 44 | Other reasons why your payment may be pending | 7.905 | Other reasons why your payment may be pending If you have chosen to pay by a wire transfer in the delivery and payment form, and you order the transfer by a third party (for example, Poczta Polska), the transfer time ... |
| 2 | 41 | Why your payment is pending or canceled | 4.813 | Why your payment is pending or canceled Your payment may have the Canceled status if: the payment has not been made through HopShop Finance within 10 days of selecting the payment method you have canceled your payment... |
| 3 | 104 | Wire transfer | -3.325 | Wire transfer You will get the refund within 3 business days to the bank account you provided. If you have issued the transfer in a post office or at the bank, PayU will email you and ask you to provide details necess... |

### Question 45/50

**Query:** How can I retry a payment that didn’t go through?

**Answer relevance:** 0.973

**Relevant docs:** `[45]`

**Retrieved docs:** `[45, 42, 43]`

**Reference answer:**

Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the following statuses:
If the seller has refunded you, you cannot pay again through HopShop Finance in the Purchase History tab.

**Generated answer:**

To retry a payment that didn’t go through, go to the Purchase History tab, find the unpaid order, and click [retry payment]. Then, select your delivery and payment method. If your bank account hasn’t been charged, you can try again.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 45 | My payment has not gone through. How to retry the payment? | 8.245 | My payment has not gone through. How to retry the payment? Go to the Purchase History tab and find a relevant order. You can only pay again if the payment has one of the following statuses: If the seller has refunded ... |
| 2 | 42 | What to do next | 7.096 | What to do next If the payment is Canceled and your bank account has not been charged, you can retry payment. To do it, open the Purchase History tab and click [retry payment] by the unpaid order. If the payment is Ca... |
| 3 | 43 | Note | 6.055 | Note Every payment starts with the Pending status. If the status does not change, check if your bank account has been charged. If not, retry the payment. To do it: Open the Purchase History tab. Click [retry payment] ... |

### Question 46/50

**Query:** How can I find out what delivery options are available for a product on HopShop?

**Answer relevance:** 0.955

**Relevant docs:** `[46]`

**Retrieved docs:** `[46, 58, 61]`

**Reference answer:**

When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Delivery and payment section to check what delivery options are available for the offer you are interested in.

**Generated answer:**

To find out what delivery options are available for a product on HopShop, go to the Delivery and payment section for the offer you are interested in.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 46 | Delivery options on HopShop | 7.692 | Delivery options on HopShop When buying on HopShop, you have a wide range of delivery options. The seller specifies delivery options available for a given offer. Go to the Delivery and payment section to check what de... |
| 2 | 58 | The HopShop Delivery program — information for buyers | 5.685 | The HopShop Delivery program — information for buyers We will launch the HopShop Delivery program on June 26, however, you can already use the delivery options within the program in some offers since June 4. HopShop D... |
| 3 | 61 | How to order a parcel with HopShop Delivery | 3.910 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |

### Question 47/50

**Query:** How is the delivery time provided for each offer?

**Answer relevance:** 0.603

**Relevant docs:** `[47]`

**Retrieved docs:** `[47, 56, 53]`

**Reference answer:**

The estimated delivery time is usually a few days. We provide it separately for each offer as a specific date, a date range, or a number of days in multiple places on different purchase stages.

**Generated answer:**

The estimated delivery time is displayed individually for each offer in several places during the purchase process, such as on the offer list, the offer page, when you click [delivery] on the offer page, in the payment and delivery form, on the thank you page, in order details in Purchase History, in selected recommended offers, and in the Buy and Pay section if available.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 47 | What is the delivery time? | 6.810 | What is the delivery time? The estimated delivery time is usually a few days. We provide it separately for each offer as a specific date, a date range, or a number of days in multiple places on different purchase stages. |
| 2 | 56 | Where you can see the estimated delivery time | 6.526 | Where you can see the estimated delivery time We display the estimated delivery time individually for each offer in a few locations on different purchase stages: on the offer list on the offer page if you click [deliv... |
| 3 | 53 | Estimated delivery time | 4.363 | Estimated delivery time For every offer on HopShop and on selected purchase steps, we display estimated time of delivery. Thanks to that, you can check when, most probably, your parcel will reach you or the pick-up po... |

### Question 48/50

**Query:** How can I find out the delivery cost for a product?

**Answer relevance:** 0.777

**Relevant docs:** `[48]`

**Retrieved docs:** `[48, 35, 50]`

**Reference answer:**

The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packaging costs are included in the product price.
You can check the delivery costs during transaction completion and in an offer page in the Delivery and payment section.
Some sellers offer free delivery. You can find their offers by filtering them by the free delivery:

**Generated answer:**

You can check the delivery costs during transaction completion and on the offer page in the Delivery and payment section.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 48 | How much does delivery cost? | 6.224 | How much does delivery cost? The cost of delivery is always set by the seller. For select delivery options, we specify the maximum prices the seller can set. Additional packaging costs are included in the product pric... |
| 2 | 35 | Determine the delivery cost | 5.427 | Determine the delivery cost If the seller has set price lists in all the offers, we will automatically calculate the delivery cost. If there are no price lists in the offers, contact the seller and negotiate the total... |
| 3 | 50 | I am buying many products — which delivery method should I choose? | 2.923 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |

### Question 49/50

**Query:** How can I add or change my shipping address on HopShop when placing an order?

**Answer relevance:** 0.979

**Relevant docs:** `[49]`

**Retrieved docs:** `[49, 90, 61]`

**Reference answer:**

If you have a registered HopShop account, you can set a default delivery address in the Account Details tab.
If you want to purchase without registering an HopShop account or you want to provide a different delivery address than the one in your account settings, you can do it:
after clicking [buy now] on the offer page, or
after clicking [delivery and payment] in the cart.

**Generated answer:**

You can add or change your shipping address on HopShop when placing an order by providing the address after clicking [buy now] on the offer page, or after clicking [delivery and payment] in the cart. If you have a registered account, you can also set a default address in the Account Details tab.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 49 | How to provide shipping details? | 4.662 | How to provide shipping details? If you have a registered HopShop account, you can set a default delivery address in the Account Details tab. If you want to purchase without registering an HopShop account or you want ... |
| 2 | 90 | I have been waiting a long time for my order delivery | -0.052 | I have been waiting a long time for my order delivery Dispatching your order may be delayed if you incorrectly complete the delivery and payment form. Check the details you have provided in the form ― find the relevan... |
| 3 | 61 | How to order a parcel with HopShop Delivery | -0.275 | How to order a parcel with HopShop Delivery While making a purchase, in the delivery and payment form, select a delivery option marked as HopShop Delivery. |

### Question 50/50

**Query:** How does delivery work if I buy multiple products, possibly from different sellers?

**Answer relevance:** 0.000

**Relevant docs:** `[50]`

**Retrieved docs:** `[50, 34, 32]`

**Reference answer:**

You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those available in each offer.
You can merge delivery costs if you buy from one seller provided that the seller enables you to do so. Depending on the seller’s settings, you will pay:
the cost of the most expensive delivery method among the offers you buy in
the cost of the cheapest delivery method among the offers you buy in
the total cost of delivery from all the offers — the parcels will be dispatched separately.

**Generated answer:**

If you buy from multiple sellers, you cannot merge delivery costs and need to choose and pay for a separate delivery method for each order. If you buy from one seller, you may be able to merge delivery costs depending on the seller’s settings.

Retrieved documents:

| rank | section_id | title | rerank_score | preview |
| --- | --- | --- | --- | --- |
| 1 | 50 | I am buying many products — which delivery method should I choose? | 5.768 | I am buying many products — which delivery method should I choose? You cannot merge delivery costs if you buy from different sellers. You choose and pay for a different delivery method for each order among those avail... |
| 2 | 34 | How to choose a delivery option | 5.587 | How to choose a delivery option If you buy at least two items: from the same seller ― select a delivery option that is available for all the offers from multiple sellers ― you can choose different delivery options for... |
| 3 | 32 | How to pay for orders made from multiple sellers | 2.548 | How to pay for orders made from multiple sellers In order to pay for items from one or more sellers with one payment, buy them through a cart. We will divide the payment automatically among the sellers. |
