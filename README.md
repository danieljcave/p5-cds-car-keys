# **CDS Car Keys**

## **A Full Stack E-Commerce Car Key Store For Code Institue Project 5**
### Author - Daniel Cave

CDS Car Keys is a B2C & B2B E-Commerce application which sells Car keys blanks and keys directly to the end customers and business. The site aims to present using with an attractive and seamless online shopping experiance and encourage users to return to purchse multiple times, including newsletters, social media information and a user profile to save customers details. 

The site is implimented as a retail store where the users can view, search and filter through products that are avalivle. To then select either a single or range of products to add to their shopping cart and pay through a single secure payment.

Customers can view the detail pages and view a range of products for purchasing, including product description and information, Manufacture, price and a rating. They are able to make purchases and view order history and save details for future purchases.

Admin/Staff users are able to manage a range of products. Employee's and services that CDS Car Keys offer. This includes Additon, Updates and Deletion of all mentioned.

Marketing is a usefull tool in business and the Newsletter using Mailchimp and addition of Facebook social media to gain new customers and exposure to the site.

The structure and key coding was based on the Code Institute Boutique Ado walkthrough example application, Credits where required.

Live Version of the website - <a href="https://p5-cds-car-keys-da11dff7570e.herokuapp.com/" target="_blank">Click Here!</a>

## Table Of Contents
- [**User Experience**](#user-experience)
- [**Features**](#features)
- [**Future Features**](#future-features) 
- [**Design**](#design)
- [**Design**](#design)
- [**Technologies Used**](#technologies-used)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  
## **User Experience**
### **Target Audience**
- Customers looking for car related services
- Businesses/Customers looking for key blanks
- Customers looking for spare keys

### **User Goals**
- To be able to purchase products on the website.
- View a range of products matching the car and key that user is looking for.
- Easy navigation through the site.
- Able to save information for seamless revisit purchases.

### **User Stories**
* EPIC 1 : Registration and Account Management
  <details>
      <summary>User Stories for EPIC 01:</summary>
    
    - US101 - Register an account
      - As a **site user** I can **register an account** so that **i am able to view my purchase history and proflie details**
    - US102 - Confirm registration via email
      - As a **site user** I can **receive email confirmation upon registering** so that **i can verify account registration was successfull**
    - US103 - Able to reset password
      - As a **site user** I can **easily reset my password if i forget it** so that **I can regain access to my account**
    - US104 - Access Profile
      - As a **site user** I can **access personalized user profile** so that **I can view my personal saved information and the order history and confirmations**
    - US105 - Login & Logout
      - As a **site user** I can **easilly login or logout** so that **I can access my information on my account**
  </details>

* EPIC 2 : Navigation
  <details>
      <summary>User Stories for EPIC 2:</summary>

    - US201 - View a list of all avalible products
      - As a **site user** I can **view a list of all keys** so that **I can select one or more to purchase.**
    - US202 - Vieww a detail page of each product
      - As a **site user** I can **view the details of a specific product** so that **I can see the description, image, avalibility, rating and pricing.**
    - US203 - View shopping bag total
      - As a **site user** I can **easily view the total of my purchase** so that **I can decide on purchase options.**
    - US204 - Able to navigate the page and understand directions
      - As a **site user** I can **quickly identify what the website is and how to get to pages** so that **I can find the information and the ability to use the site for.**
    - US205 - View keys by manufacturer
      - As a **site user** I can **see which keys i am looking for** so that **I can purchase the correct key for my car**
    - US206 - View keys by category/rating
      - As a **site user** I can **view specific catergory or taing of key** so that **I can easily choose what keys i am interested in**
    - US207 - Handle 403, 404, 405 and 500 errors
      - As a **site user** I can **return back to homepage after encountering a 403, 404, 405 and 500 response** so that **I can still manuver the website without any issues and navigate easily**
  </details>

* EPIC 3 : Sorting & Searching
  <details>
      <summary>User Stories for EPIC 3:</summary>

    - US301 - Sort a list of avalible keys
      - As a **site user** I can **sort through a list of keys** so that **I can choose the best rated and sorted products**
    - US302 - Sort a specific category
      - As a **site user** I can **sort a specific category or keys** so that **I can find the best-rated key in a specific category or to sort in a range or keys**
    - US303 - Sort a specific Manufacturer
      - As a **site user** I can **sort by specific manufacturer** so that **I can find the right key brand and choose a specific key from the manufacture**
    - US304 - Search for a specific key or maufacturer
      - As a **site user** I can **search by name, description or manufacture** so that **I can find a specific key to purchase**
    - US305 - View a results of searching and amount of prodcuts found
      - As a **site user** I can **easily see results of my searches** so that **I can decide what key i want to purchase**
  </details>

* EPIC 4 : Purchasing & Checkout
  <details>
      <summary>User Stories for EPIC 4:</summary>

    - US401 - Add an key to shopping bag
      - As a **site user** I can **add keys to the shopping bag** so that **I can what i want or more items to purchase**
    - US402 - Edit shopping bag and remove items from bag
      - As a **site user** I can **modify my shopping bag even after putting keys in my bag** so that **I can manage the shopping bag even if erros have been made or have any changes**
    - US403 - See user notification on actions
      - As a **site user** I can **get a notification on the screen of my actions** so that **I can easily confirm that my interaction with the website too place**
    - US404 - Finalise an order via checkout page
      - As a **site user** I can **complete an order on the checkout page** so that **I can see my final total, a list of items and sumarry and specify a delivery adress and payment option**
    - US405 - Have a secure payment option
      - As a **site user** I can **enter payment details** so that **I can payment informtaion is secure and action is secure**
    - US406 - View an order confirmation after checkout
      - As a **site user** I can **view an order confirmation after checkout** so that **I can see what was ordered and the final cost**
    - US407 - Recive email confirmation of order after checkout
      - As a **site user** I can **recive and email confirmation after checkout completion** so that **I can have a record of all my purchase as a backup**
  </details>

* EPIC 5 : Admin and Store Management
  <details>
      <summary>User Stories for EPIC 5:</summary>

    - US501 - Add a product
      - As a **site admin** I can **add a product** so that **I can sell a new product on the store**
    - US502 - Add a employee
      - As a **site admin** I can **add a new employee** so that **I can update our team roster on the website**
    - US503 - Add a service
      - As a **site admin** I can **add new services** so that **I can offer more services along with products**
    - US504 - Edit or update product, employee or service
      - As a **site admin** I can **change and details to uploaded inforion or update** so that **I can keep store information up to date fresh**
    - US505 - Delete a product, employee or service
      - As a **site admin** I can **remove a product, employee or server** so that **I can remove a product, and employee or service from the database**
  </details>

* EPIC 6 : SEO and Web Marketing
  <details>
      <summary>User Stories for EPIC 5:</summary>

    - US601 - View company facebook page
      - As a **site admin** I can **find the company on facebook** so that **I can view and keep up to date with company posts**
    - US602 - Subscribe to newsletter
      - As a **site admin** I can **subscribe to company newsletter** so that **I can get company news and offers**
    - US603 - SEO
      - As a **site admin** I can **find the site through web searches** so that **I can easily acces the site**
  </details>

## Features
Bellow are a list of features avalible on the site along with a decription. Many of the feature that are based of the Boutique Ado walkthrough project, SEO and Web Marketing modules from the course.

CDS Car Key uses a B2C e-commerce model, selling directly to customers with single online payments.

The page focuses on a black, white and grey theme to stay consistant throught the site.

- F-01
  - The homepage and shop homepage Desktop View
![F01 Desktop View](/readME-assets/features/homepage.png)
![F01 Shop View](/readME-assets/features/shop.png)

- F-02
  - The Homepage and shop on tablet view
![F-02](/readME-assets/features/homepage-tab.png)
![F-02](/readME-assets/features/shop-tab.png)

- F-03
  - The homepage and shop on mobile view

![F-03](/readME-assets/features/homepage-phone.png)
![F-03](/readME-assets/features/shop-phone.png)

- F-04
  - View Avalible Key Products
  ![F-04](/readME-assets/features/keys.png)

- F-05
  - Filter and Sort options avalible
![F-05](/readME-assets/features/filter-prod.png)

- F-06
  - Manufacturer filter options (Audi)
![F-06](/readME-assets/features/category.png)

- F-07
  - Product View for details
![F-07](/readME-assets/features/key-detail.png)

- F-08
  - About Us and Services Links
![F-09](/readME-assets/features/about-serv.png)

- F-09
  - About Us Section
![F-09](/readME-assets/features/about.png)

- F-10
  - Services Section
![F-10](/readME-assets/features/services.png)

- F11
  - Bag Notification
![F-11](/readME-assets/features/notification.png)

- F12
  - Newsletter Popup
![F-12](/readME-assets/features/newsletter-popup.png)

## Account and Registration

- F13
  - Registration Form
![F-13](/readME-assets/features/signup.png)

- F14
  - Sign in Form
![F-14](/readME-assets/features/signin.png)

- F15
  - Email Confirmation
![F15](/readME-assets/features/verify.png)

- F16
  - Logout Form
![F16](/readME-assets/features/logout.png)

- F17
  - Admin Account View
![f17](/readME-assets/features/admin-view.png)

- F18
  - Profile View
![f18](/readME-assets/features/profile.png)

## E-Commerce Features

- F19
  - Shopping Bag
![f19](/readME-assets/features/bag.png)

- F20
  - Checkout Page
![f20](/readME-assets/features/checkout.png)

- F21
  - Checkout Complete
![f21](/readME-assets/features/order-confirm.png)

- F22
  - Stripe Events
![f22](/readME-assets/features/events.png)

- F23 
  - Stripe Webhooks
![f23](/readME-assets/features/wh.png)

- F24
  - Email Confirmation
![f24](/readME-assets/features/email.png)

## Admin Features

- F25
  - Add Product
[!f25](/readME-assets/features/add-prod.png)

- F26
  - Add employee
![f26](/readME-assets/features/add_employee.png)

- F27
  - Add Service
![f27](/readME-assets/features/add_service.png)

- F28
  - Edit Product
![f28](/readME-assets/features/edit-prod.png)

- F29 
  - Edit Employee
![29](/readME-assets/features/edit-emp.png)

- F30
  - Edit Services
![f30](/readME-assets/features/edit-serv.png)

## SEO and Marketing

- F31
  - SEO 
    - Added Meta tags along with description and keywords
    - Appropriate site title and home page content
    - Informative site heading slogan on home page

- F32
  - Facebook Page
![f32](/readME-assets/features/fb.png)

- F33
  - Newsletter
![f33](/readME-assets/features/newsletter.png)

