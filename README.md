# 🛒 E-Commerce Automation Testing Framework

A simple **Selenium + Pytest automation testing project** created to automate testing of the [Automation Exercise](https://automationexercise.com/) e-commerce website.

## 🎯 Project Overview

This project automates important e-commerce scenarios such as:

* Login validation
* Product search
* Add to cart
* Remove from cart
* Checkout
* Negative test cases
* End-to-end checkout flow

The framework uses **Page Object Model (POM)** to keep the automation code simple, reusable, and easy to maintain.

## 🛠️ Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML
* WebDriver Manager
* Page Object Model (POM)
* GitHub Actions

## 📁 Project Structure

```text
auto_exercise/
│
├── base.py
├── conftest.py
├── login_page.py
├── product_page.py
├── checkout_page.py
│
├── test_login.py
├── test_product.py
├── test_cart.py
├── test_checkout_negative.py
├── test_e2e_checkout.py
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
└── requirements.txt
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/murugavelvv/auto_exercise.git
cd auto_exercise
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run tests

```bash
pytest
```

## 📊 HTML Test Report

Generate an HTML report using:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report contains:

* Test results
* Pass/Fail status
* Execution time
* Failure details
* Screenshots for failed tests

## 🔄 CI/CD

GitHub Actions is used to automatically execute the automation tests when changes are pushed to the repository.

## 🧪 Testing Approach

The project follows a simple testing workflow:

**Manual Testing → Test Cases → Automation → Test Execution → HTML Report → CI/CD**

## 🚀 Key Features

* Reusable Page Object Model
* Explicit waits for stable execution
* Data-driven testing with Pytest
* Positive and negative test cases
* Automated HTML reports
* Screenshot capture for failures
* GitHub Actions integration

# 🛒 E-Commerce Automation Testing Framework

A simple **Selenium + Pytest automation testing project** created to automate testing of the [Automation Exercise](https://automationexercise.com/) e-commerce website.

## 🎯 Project Overview

This project automates important e-commerce scenarios such as:

* Login validation
* Product search
* Add to cart
* Remove from cart
* Checkout
* Negative test cases
* End-to-end checkout flow

The framework uses **Page Object Model (POM)** to keep the automation code simple, reusable, and easy to maintain.

## 🛠️ Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML
* WebDriver Manager
* Page Object Model (POM)
* GitHub Actions

## 📁 Project Structure

```text
auto_exercise/
│
├── base.py
├── conftest.py
├── login_page.py
├── product_page.py
├── checkout_page.py
│
├── test_login.py
├── test_product.py
├── test_cart.py
├── test_checkout_negative.py
├── test_e2e_checkout.py
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
└── requirements.txt
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/murugavelvv/auto_exercise.git
cd auto_exercise
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run tests

```bash
pytest
```

## 📊 HTML Test Report

Generate an HTML report using:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report contains:

* Test results
* Pass/Fail status
* Execution time
* Failure details
* Screenshots for failed tests

## 🔄 CI/CD

GitHub Actions is used to automatically execute the automation tests when changes are pushed to the repository.

## 🧪 Testing Approach

The project follows a simple testing workflow:

**Manual Testing → Test Cases → Automation → Test Execution → HTML Report → CI/CD**

## 🚀 Key Features

* Reusable Page Object Model
* Explicit waits for stable execution
* Data-driven testing with Pytest
* Positive and negative test cases
* Automated HTML reports
* Screenshot capture for failures
* GitHub Actions integration
