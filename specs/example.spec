Specification Heading
=====================

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

## Go to Main Page WithoutNotification
tags:mainpage
* Go to Main Page For Koton MobileSite

## test enter date
* Wait "2" seconds
* Go to register page

## Test Scroll
* Click element by "hamburgerMenu" if exist
* Wait "2" seconds
* scroll to the element "lostPasswordPage" be visible
* Wait "2" seconds
* Click to element "lostPasswordPage"

## Register
tags:register
* Wait "5" seconds
* Go to register page
* Sign Up
* Verify that the registration is done
* Verify that the site is proceeded to Login Page

## Login the QA account
* Go to QA Env

## Forgot Password
tags:forgotPassword
* Go to Test Env
* Go to Forgot Password Page


## Change Password
tags:changePassword
* Go to Test Env
* Login with "beliztest" and "password1"
* Go to Change Password Page
* Change Password write "password1" and "Qwerty12345" and "Qwerty12345"
* LogOut
* Wait "2" seconds
* Wrong Password Entry
* Wait "2" seconds
* ReLogin with right "Qwerty12345"
* Go to Change Password Page
* Change Password write "Qwerty12345" and "password1" and "password1"


## Place Bet
tags:placeBet
* Go to Test Env
* Login with "beliztest" and "password1"
* Choose Bet
* Go to The Bet Slip Page
* Accept Bet
* Return to Home Page After Placed Bet
* Bet Detail View
* Go to Home Page With Logo
//* Bet Rearrange

## Test for first placed bet in bets page
* Go to QA Env
* go to bet and check the first bet

## Make Deposite With Accent In Method
tags:makeDepositWithAccentInMethod
* Go to QA Env
* Go to Payment
* Choose to Payment Method with "depositAccentInMethod"
* Genarete Random Deposit Value and Enter that value
* Continue To Transaction
* Enter Credit Card İnformation with "4000000000000077", "Test Test" and "123"
//* Verify the deposit information and continue the main site
//* Go to Booking Page

## Make Deposite With Apco Method
tags:makeDepositWithApcoMethod
* Go to QA Env
* Go to Payment
* Choose to Payment Method with "apcoMethod"
* Genarete Random Deposit Value and Enter that value
* Continue To Transaction
* Enter Credit Card İnformation with "4051 8856 0044 6623", "Test Test" and "123" apco
//* Verify the deposit information and continue the main site
//* Go to Booking Page


## Make Deposite With Monnet Method
tags:makeDepositWithMonnetMethod
* Go to QA Env
* Go to Payment
* Choose to Payment Method with "monnetMethod"
* Genarete Random Deposit Value and Enter that value
* Select the Identity Type and Enter the Identity Number
* Continue To Transaction
* Select to the credit option for deposit method
* Enter Credit Card İnformation with "4051 8856 0044 6623", "123" and "1224" monnet

## Make Withdrawal With Monnet Method
tags:makeWithdrawalWithMonnetMethod
* Go to QA Env
* Go to Payment
* Go to Withdrawal Methods
* Choose to Payment Method with "monnetWithdrawalMethods"
* Genarete Random Transaction Value and Enter that value
* Select the Bank Type and Enter the Account Number
* Select the Identity Type and Enter the Account Number
* Continue To Transaction



## Upload Document
* Go to QA Env
* Go to Document Page
* Select the Type of Identifier
* Upload the File
* Wait "5" seconds

## Change Bet Settings
* Go to Test Env
* Login with "beliztest" and "password1"
* Go to Bet Settings Page
* Set the Odd Values In Bet Settings
* Set the Cashout Amount In Bet Settings
* Enter the Default Stake Value
* Save The Settings
* Verify that the bet settings are saved

## Upload Document on Betweb
* Upload Document on Betweb

## Select Any Value in Dropdown Test
* Select The Value In Dropdown List Test
