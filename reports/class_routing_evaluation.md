# Class Routing Report

Source notebook: `notebooks/06_class_routing.ipynb`

## Overview

- Total cases: 23
- Accuracy: 1.000
- Average confidence: 0.705

## Summary Tables

### Final Metrics

| total_cases | accuracy | avg_confidence |
| --- | --- | --- |
| 23 | 1.000 | 0.705 |

### Per-class Metrics

| label | precision | recall | f1 | support |
| --- | --- | --- | --- | --- |
| none | 1.000 | 1.000 | 1.000 | 7 |
| faq | 1.000 | 1.000 | 1.000 | 8 |
| product | 1.000 | 1.000 | 1.000 | 8 |

### Confusion Matrix

| expected | none | faq | product |
| --- | --- | --- | --- |
| none | 7 | 0 | 0 |
| faq | 0 | 8 | 0 |
| product | 0 | 0 | 8 |

### Raw Results

| query | expected | predicted | confidence | is_correct |
| --- | --- | --- | --- | --- |
| How old are you? | none | none | 0.100 | True |
| Tell me a joke about online shopping. | none | none | 0.100 | True |
| Translate "blue shirt" into Polish. | none | none | 0.100 | True |
| What is the weather in Warsaw today? | none | none | 0.100 | True |
| Solve 17 * 23 for me. | none | none | 0.100 | True |
| Who won the football World Cup in 2018? | none | none | 0.100 | True |
| Summarize Dune in two sentences. | none | none | 0.100 | True |
| What is your return policy? | faq | faq | 0.980 | True |
| How can I reset my password? | faq | faq | 0.980 | True |
| Can I change the email address connected to my account? | faq | faq | 0.970 | True |
| How do I track my parcel after it is shipped? | faq | faq | 0.980 | True |
| What should I do if my package arrived damaged? | faq | faq | 0.970 | True |
| How long does it usually take to get a refund? | faq | faq | 0.980 | True |
| How can I download an invoice for my order? | faq | faq | 0.970 | True |
| Give me three examples of blue T-shirts you have available. | product | product | 0.980 | True |
| How can I contact the user support? | faq | faq | 0.980 | True |
| Do you have blue Dresses? | product | product | 0.980 | True |
| Show me black ankle boots in size 39. | product | product | 0.970 | True |
| Find a beige trench coat for spring. | product | product | 0.970 | True |
| I need a leather handbag for work meetings. | product | product | 0.950 | True |
| Show me white sneakers for men. | product | product | 0.980 | True |
| Recommend accessories for a navy evening gown. | product | product | 0.950 | True |
| Create a look suitable for a wedding party happening during dawn. | product | product | 0.930 | True |

## Detailed Results

### Case 1

**Query:** How old are you?

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 2

**Query:** Tell me a joke about online shopping.

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 3

**Query:** Translate "blue shirt" into Polish.

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 4

**Query:** What is the weather in Warsaw today?

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 5

**Query:** Solve 17 * 23 for me.

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 6

**Query:** Who won the football World Cup in 2018?

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 7

**Query:** Summarize Dune in two sentences.

**Expected:** none

**Predicted:** none

**Confidence:** 0.100

**Correct:** yes

### Case 8

**Query:** What is your return policy?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.980

**Correct:** yes

### Case 9

**Query:** How can I reset my password?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.980

**Correct:** yes

### Case 10

**Query:** Can I change the email address connected to my account?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.970

**Correct:** yes

### Case 11

**Query:** How do I track my parcel after it is shipped?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.980

**Correct:** yes

### Case 12

**Query:** What should I do if my package arrived damaged?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.970

**Correct:** yes

### Case 13

**Query:** How long does it usually take to get a refund?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.980

**Correct:** yes

### Case 14

**Query:** How can I download an invoice for my order?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.970

**Correct:** yes

### Case 15

**Query:** Give me three examples of blue T-shirts you have available.

**Expected:** product

**Predicted:** product

**Confidence:** 0.980

**Correct:** yes

### Case 16

**Query:** How can I contact the user support?

**Expected:** faq

**Predicted:** faq

**Confidence:** 0.980

**Correct:** yes

### Case 17

**Query:** Do you have blue Dresses?

**Expected:** product

**Predicted:** product

**Confidence:** 0.980

**Correct:** yes

### Case 18

**Query:** Show me black ankle boots in size 39.

**Expected:** product

**Predicted:** product

**Confidence:** 0.970

**Correct:** yes

### Case 19

**Query:** Find a beige trench coat for spring.

**Expected:** product

**Predicted:** product

**Confidence:** 0.970

**Correct:** yes

### Case 20

**Query:** I need a leather handbag for work meetings.

**Expected:** product

**Predicted:** product

**Confidence:** 0.950

**Correct:** yes

### Case 21

**Query:** Show me white sneakers for men.

**Expected:** product

**Predicted:** product

**Confidence:** 0.980

**Correct:** yes

### Case 22

**Query:** Recommend accessories for a navy evening gown.

**Expected:** product

**Predicted:** product

**Confidence:** 0.950

**Correct:** yes

### Case 23

**Query:** Create a look suitable for a wedding party happening during dawn.

**Expected:** product

**Predicted:** product

**Confidence:** 0.930

**Correct:** yes
