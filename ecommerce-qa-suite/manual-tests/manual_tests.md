# Manual Tests

## Login Page
| Test Case ID | Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --- | --- | --- | --- | --- |
| TC-001 | Verify successful login with valid credentials | 1. Navigate to login page<br>2. Enter valid username and password<br>3. Click login button | User is redirected to the dashboard | |
| TC-002 | Verify unsuccessful login with invalid credentials | 1. Navigate to login page<br>2. Enter invalid username and password<br>3. Click login button | Error message is displayed | |

## Product Page
| Test Case ID | Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --- | --- | --- | --- | --- |
| TC-003 | Verify that product details are displayed correctly | 1. Navigate to a product page | Product name, price, and description are displayed | |
| TC-004 | Verify that a product can be added to the cart | 1. Navigate to a product page<br>2. Click "Add to Cart" button | Product is added to the cart | |

## Cart Page
| Test Case ID | Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --- | --- | --- | --- | --- |
| TC-005 | Verify that the cart can be updated | 1. Navigate to the cart page<br>2. Change the quantity of a product | The cart total is updated | |
| TC-006 | Verify that a product can be removed from the cart | 1. Navigate to the cart page<br>2. Click the "Remove" button for a product | The product is removed from the cart | |

## Checkout Page
| Test Case ID | Test Case Description | Steps to Reproduce | Expected Result | Actual Result |
| --- | --- | --- | --- | --- |
| TC-007 | Verify that the checkout process can be completed | 1. Navigate to the checkout page<br>2. Fill in all the required fields<br>3. Click the "Place Order" button | The order is placed successfully | |
