# Base Prompting Report

Source notebook: `notebooks/11_base_prompting.ipynb`

## Overview

- Evaluated samples: 14
- Greeting cases: 6
- Non-greeting cases: 8

## Summary Tables

### Final Metrics

| samples | greet_true_cases | greet_false_cases |
| --- | --- | --- |
| 14 | 6 | 8 |

### Sample Results

| query | greet | chat_history | response |
| --- | --- | --- | --- |
| hi there | True |  | Welcome to HopShop! Please ask a question related to the store and its products. |
| hello | True |  | Welcome to HopShop! Please ask a question related to the store and its products. |
| how old are you? | True |  | Welcome to HopShop! Please ask a question related to the store and its products. |
| what weather in Warsaw? | True |  | Welcome to HopShop! Please ask a question related to the store and its products. |
| How do I register on HopShop? | True |  | Welcome to HopShop! Please ask a question related to the store and its products. |
| Thanks | True |  | Welcome to HopShop! You're welcome! |
| hi there | False | user: hi there
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | Welcome to HopShop! Please ask a question related to the store and its products. |
| what weather in Warsaw? | False | user: hi there
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | Please ask a question related to the store and its products. |
| How do I register for a HopShop account using my phone number? | False | user: hello
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | Please ask a question related to the store and its products. |
| Thanks | False | user: hi there
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | You're welcome! |
| thank you for your help | False | user: I need help with my order
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | You're welcome! |
| bye | False | user: hi
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | Please ask a question related to the store and its products. |
| Can you help me with my password? | False | user: hello
assistant: Welcome to HopShop! Please ask a question related to the store and its products.
user: I cannot log in
assistant: Please ask a question related to the store and its products. | Please ask a question related to the store and its products. |
| Thanks, and what is the weather tomorrow? | False | user: hi there
assistant: Welcome to HopShop! Please ask a question related to the store and its products. | You're welcome! Please ask a question related to the store and its products. |
