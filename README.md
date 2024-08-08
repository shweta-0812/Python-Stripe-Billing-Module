# Python-Stripe-Billing-Module [WIP]

**Requirement**

**WHY: Build a billing module which can be deployed as a separate micro-service and can be used to execute product related customer billing activities.**

The  module integrates with Stripe  ( Stripe UI + Backend ) to perform the tasks because:

1. Stripe is secure, hence no security overhead needed for maintaining the card details and transaction details of the customer.
2. Stripe meets compliance guidelines so it is easy to trust
3. Stripe provides admin interface to perform admin activities incase of fraud transactions and other edge cases.
4. Stripe provides APIs and web hooks which can be easily integrated with the backend services to perform system originated task and also keep the system in sync with Stripe dashboard.
5. Stripe provides powerful combination of various types of billing activities which can help build a solid suite of custom products and prices.
6. 

**WHAT: Build a user billing system which has the following functionalities:**

1. WHEN a user signs-up for the first time

THEN 

1. user will get a trial period of x days
2. user will not be charged any fee during trial period
3. at the end of the trial period user will either have to setup a credit card to use the service or will not be able to access any features
1. WHEN the user trial period ends and wants to continue using the service

THEN

1. user enters the card detail on Stripe UI and then details get stored in the Stripe backend
2. redacted user card details and confirmation of card setup are shown in user account settings page 
    
    (Tech)
    
    The card details and setup information is fetched from Stripe using webhook and stored/updated in the application DB for all the future use.
    

1. WHEN user card has been successfully setup in Stripe and application system checks verify that the card has been setup 

THEN

1. user can access the service
2. user is billed at the end of month based on units of usage.

**HOW: Billing calculation is done:**

HOW: Billing calculation is done:

1. Products for customer:
    
    
    | Tier | Product  |
    | --- | --- |
    | 1 | Basic |
    | 2 | Premium |
    | 3 | Silver |
    | 4 | Gold |

2. Pricing for the customer:
    1. Pricing is tiered based on user membership type and usage demands
        
        
        | Tier | Product | Usage Range | Fixed Base Charge | Charge per unit above the usage limit |
        | --- | --- | --- | --- | --- |
        | 1 | Basic | 0-100 | $50 | $2.25 |
        | 2 | Premium | 100-400 | $180 | $1.80 |
        | 3 | Silver | 400-900 | $350 | $1.50 |
        | 4 | Gold | 900-1500 | $600 | $1.25 |
3. Billing Cycle:
    1. The first x days trial period is not counted in the billing cycle
    2. The billing cycle starts from the day of card setup
    3. For the first month the billing cycle ends on the last day of the month, doing a pro-rated charge for the used days in the first month. 
    4. From the next month onwards the billing happens at the end of each month
4. Monthly Allowable Usage calculation: 
    1. The allowed usage for the first month is pro-rated for the number of days in the given calendar month for the first month:
    
    first month allowed usage = (total allowed usage / number of day in calendar month) * diff ( end of month - current day )
