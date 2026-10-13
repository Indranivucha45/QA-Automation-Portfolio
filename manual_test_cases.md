# 📋 Manual Testing & Defect Tracking Suite

This document outlines sample manual test scenarios, boundary value analysis, and a structured defect report logged during functional testing of an e-commerce login/checkout module.

---

### Part 1: Test Scenario & Boundary Value Analysis (BVA)

* **Module:** User Registration / Age Verification Field
* **Valid Range:** 18 to 60 years old

| Test ID | Test Scenario | Input Value | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TS_001 | Verify valid age input (Middle boundary) | 25 | Access granted, registration proceeds. | **Passed** |
| TS_002 | Verify minimum boundary value | 18 | Access granted (Exact lower limit). | **Passed** |
| TS_003 | Verify maximum boundary value | 60 | Access granted (Exact upper limit). | **Passed** |
| TS_004 | Verify just below minimum (Invalid) | 17 | Error message: "Must be at least 18 years old." | **Passed** |
| TS_005 | Verify just above maximum (Invalid) | 61 | Error message: "Age cannot exceed 60." | **Passed** |

---

### Part 2: Sample Defect Report (Jira Tracking Format)

* **Defect ID:** BUG-101
* **Module:** Checkout / Payment Gateway
* **Severity:** High
* **Priority:** High
* **Title:** Application crashes with 500 Internal Server Error when selecting 'Net Banking' payment option.

#### **Steps to Reproduce:**
1. Log in to the application with valid user credentials.
2. Add a product to the cart and proceed to the Checkout screen.
3. Select **Net Banking** as the payment method.
4. Click on the **Proceed to Pay** button.

* **Expected Result:** The user should be redirected to the secure bank selection gateway page.
* **Actual Result:** The page freezes for 5 seconds and displays a blank screen with a `500 Internal Server Error`.
* **Environment:** Chrome Browser v120 / Staging Environment
