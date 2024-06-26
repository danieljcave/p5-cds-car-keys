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


# Future Features

* A feature that would be good to impliment would be a wishlist/like option, to allow user to be able to save their favroute products to come back to later date or just to save for later.
* Leave reviews on products and see what they bought with. A way for user to get feedback on what they are looking to buy and see what else people bought with it for stats and trends.
* Add a DOB option to user profiles to then allow user to get a discount code on their birthday or even deals on holiday such as christmas and easter. To entice user to create an account for discounts.

# Design
## Data Model

The project is hosted on Heroku and currntly using CI Database. Amazon S3 is used for all of the static file and stripe is primary source for financial payments, along with incorpiration of webhooks to allow for email confirmtaion. 
There are Custom models used to think our the website and the furture expantion of website and the business. Data Models used bellow.

The Models are created to be able to be updated or to serve a expantion process to limit amount of hard coding needed. For explample, with services and employees model. The company may increase in size and offere more services. So having the option for a Admin or staff memeber to add more employees or to add more services they offer without the need of a developer to hard code into the html.

![Order](/readME-assets/features/order.png)
![OrderLineItem](/readME-assets/features/orderlineitem.png)
![Product&Brand](/readME-assets/features/Product-brand.png)
![Profile](/readME-assets/features/profile-model.png)
![Services](/readME-assets/features/services-model.png)
![Employee](/readME-assets/features/email.png)

## Typography

Montserrat is the primary font-family used, with Sans-Ferif as a backup.

# Technologies Used
* HTML5
* CSS3
* JavaScript
* Python

### Frameworks and Libraries Used:

  - [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework is used for styling and building responsive web pages.
  - [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images.
  - [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used for measuring code coverage of Python test files.
  - [Django:](https://www.djangoproject.com/) Main Python framework used in the development.
  - [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration.
  - [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
  - [dj_database_url:](https://pypi.org/project/dj-database-url/) Used to allow database URLs to connect to the Postgres database.
  - [Django Countries:](https://pypi.org/project/django-countries/) Used for country selection drop-down
  - [Gunicorn:](https://gunicorn.org/) Green Unicorn, used as the Web Server to run Django on Heroku.
  - [Pillow:](https://pillow.readthedocs.io/en/stable/index.html) Python Imaging Library used for image handling
  - [Stripe:](https://js.stripe.com/v3/) used for secure payments
  - [Amazon S3:](https://aws.amazon.com/s3/) used to store static files and images.
  - [Boto3:](https://pypi.org/project/boto3/) the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.
  - [Django-Storages:](https://django-storages.readthedocs.io/en/latest/) used to connect django to S3.

### Software and Web Applications Used:

  - [Google Fonts:](https://fonts.google.com/) To import font family Roboto
  - [Font Awesome:](https://fontawesome.com/) Used for style icons for nav and footer and other links
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) To test inside of different screen sizes
  - [GitHub:](https://github.com/) GitHub is used to store the project's code and update and pull from. As well as host user stories
  - [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
  - [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
  - [CI Python Linter](https://pep8ci.herokuapp.com/) Used to validate python code
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
  - [Codeanywhere](https://codeanywhere.com/signin) Used as virtual environment for coding
  - [Code Institute Postgres Database:](https://codeinstitute.net/) Used CI to host PostgreSQL Service
  - [Stack Overflow](https://stackoverflow.com/) Used for help when hit bumps or errors

# Testing
* Validator Testing
  * HTML Validator
    - <a href="/readME-assets/testing/htmlhome.png" target="_blank">Home Page</a>
    - <a href="/readME-assets/testing/htmlemployee.png" target="_blank">Employee Page</a>
    - <a href="/readME-assets/testing/htmlservices.png" target="_blank">Services Page</a>
    - <a href="/readME-assets/testing/htmlproducts.png" target="_blank">Products Page</a>
    - <a href="/readME-assets/testing/product_detail.png" target="_blank">Product View Page</a>
    - <a href="/readME-assets/testing/htmlprofile.png" target="_blank">Profile Page</a>
    - <a href="/readME-assets/testing/htmlbag.png" target="_blank">Bag Page</a>
      - HTML Bag has a quantity error but cannot change due to duplicate product has multiple same id causing html error.
    - <a href="/readME-assets/testing/htmlcheckout.png" target="_blank">Checkout Page</a>

  * CSS Validator
    - <a href="/readME-assets/testing/base-css.png" target="_blank">Results for Base css</a>
    - <a href="/readME-assets/testing/checkout-cs.png" target="_blank">Results for Checkout css</a>
    - <a href="/readME-assets/testing/profilecss.png" target="_blank">Results for profile css</a> 

  * Python Testing
  - Python Validation was performed using the command : python3 -m flake8.  No serious errors reported. Messages relevant to the project py files are as follows:

  <details>
    <summary>Python Validation Results</summary>

  - .\cds_car_keys\settings.py:18:5: F401 'env' imported but unused
  - .\cds_car_keys\settings.py:128:5: E122 continuation line missing indentation or outdented
  - .\cds_car_keys\settings.py:132:1: E122 continuation line missing indentation or outdented
  - .\checkout\apps.py:8:9: F401 'checkout.signals' imported but unused
  - .\checkout\migrations\0001_initial.py:19:80: E501 line too long (117 > 79 characters)
  - .\checkout\migrations\0001_initial.py:20:80: E501 line too long (82 > 79 characters)
  - .\checkout\migrations\0001_initial.py:25:80: E501 line too long (85 > 79 characters)
  - .\checkout\migrations\0001_initial.py:28:80: E501 line too long (92 > 79 characters)
  - .\checkout\migrations\0001_initial.py:29:80: E501 line too long (83 > 79 characters)
  - .\checkout\migrations\0001_initial.py:31:80: E501 line too long (98 > 79 characters)
  - .\checkout\migrations\0001_initial.py:32:80: E501 line too long (97 > 79 characters)
  - .\checkout\migrations\0001_initial.py:33:80: E501 line too long (97 > 79 characters)
  - .\checkout\migrations\0001_initial.py:39:80: E501 line too long (117 > 79 characters)
  - .\checkout\migrations\0001_initial.py:40:80: E501 line too long (90 > 79 characters)
  - .\checkout\migrations\0001_initial.py:42:80: E501 line too long (104 > 79 characters)
  - .\checkout\migrations\0001_initial.py:43:80: E501 line too long (137 > 79 characters)
  - .\checkout\migrations\0001_initial.py:44:80: E501 line too long (115 > 79 characters)
  - .\checkout\migrations\0004_order_user_profile.py:18:80: E501 line too long (155 > 79 characters)
  - .\employees\migrations\0001_initial.py:17:80: E501 line too long (117 > 79 characters)
  - .\employees\migrations\0001_initial.py:18:80: E501 line too long (81 > 79 characters)
  - .\products\migrations\0001_initial.py:18:80: E501 line too long (117 > 79 characters)
  - .\products\migrations\0001_initial.py:20:80: E501 line too long (91 > 79 characters)
  - .\products\migrations\0001_initial.py:29:80: E501 line too long (117 > 79 characters)
  - .\products\migrations\0001_initial.py:30:80: E501 line too long (81 > 79 characters)
  - .\products\migrations\0001_initial.py:34:80: E501 line too long (103 > 79 characters)
  - .\products\migrations\0001_initial.py:35:80: E501 line too long (87 > 79 characters)
  - .\products\migrations\0001_initial.py:36:80: E501 line too long (82 > 79 characters)
  - .\products\migrations\0001_initial.py:37:80: E501 line too long (135 > 79 characters)
  - .\profiles\migrations\0001_initial.py:21:80: E501 line too long (117 > 79 characters)
  - .\profiles\migrations\0001_initial.py:22:80: E501 line too long (94 > 79 characters)
  - .\profiles\migrations\0001_initial.py:23:80: E501 line too long (97 > 79 characters)
  - .\profiles\migrations\0001_initial.py:24:80: E501 line too long (100 > 79 characters)
  - .\profiles\migrations\0001_initial.py:25:80: E501 line too long (100 > 79 characters)
  - .\profiles\migrations\0001_initial.py:26:80: E501 line too long (97 > 79 characters)
  - .\profiles\migrations\0001_initial.py:27:80: E501 line too long (91 > 79 characters)
  - .\profiles\migrations\0001_initial.py:28:80: E501 line too long (93 > 79 characters)
  - .\profiles\migrations\0001_initial.py:29:80: E501 line too long (111 > 79 characters)
  - .\profiles\migrations\0001_initial.py:30:80: E501 line too long (121 > 79 characters)
  - .\services\migrations\0001_initial.py:17:80: E501 line too long (117 > 79 characters)

  </details>

* Manual Testing
  - US101 - Register an account
    - As a **site user** I can **register an account** so that **i am able to view my purchase history and proflie details**
    - Testing Complete:
      - Created an account with multiple emails to confirm account creation successfull.
  - US102 - Confirm registration via email
    - As a **site user** I can **receive email confirmation upon registering** so that **i can verify account registration was successfull**
    - Testing Complete:
      - Recived and email to confirm account create. Opened link to confirm working link. Account created and registered.
  - US103 - Able to reset password
    - As a **site user** I can **easily reset my password if i forget it** so that **I can regain access to my account**
    - Testing Complete:
      - Clicked reset password and able to enter an email. Email was sent with instructions to reset password.
  - US104 - Access Profile
    - As a **site user** I can **access personalized user profile** so that **I can view my personal saved information and the order history and confirmations**
    - Testing Complete:
      - Logged into account and able to access profile from the navigation bar
  - US105 - Login & Logout
    - As a **site user** I can **easilly login or logout** so that **I can access my information on my account**
    - Testing Complete:
      - Able to successfully loging and logout of multiple accounts.
<br>

  - US301 - Sort a list of avalible keys
      - As a **site user** I can **sort through a list of keys** so that **I can choose the best rated and sorted products**
      - Testing Complete:
        - Was able to click on sort option in the products page and go through multiple links
    - US302 - Sort a specific category
      - As a **site user** I can **sort a specific category or keys** so that **I can find the best-rated key in a specific category or to sort in a range or keys**
      - Testing Complete:
        - Able to select category such as audi and only audi keys came up
    - US303 - Sort a specific Manufacturer
      - As a **site user** I can **sort by specific manufacturer** so that **I can find the right key brand and choose a specific key from the manufacture**
      - Testing Complete:
        - Sorted by Manufactutre and only that manufacturer showed so successful
    - US304 - Search for a specific key or maufacturer
      - As a **site user** I can **search by name, description or manufacture** so that **I can find a specific key to purchase**
      - Testing Complete:
        - Search for hyundia word and a hyundia key came up.
    - US305 - View a results of searching and amount of prodcuts found
      - As a **site user** I can **easily see results of my searches** so that **I can decide what key i want to purchase**
      - Testing Complete:
        - Searched for word transponder and all keys that had transponder in name or description came up.
<br>

- US401 - Add an key to shopping bag
      - As a **site user** I can **add keys to the shopping bag** so that **I can what i want or more items to purchase**
      - Testing Complete:
        - Went to products page and selected multiple keys and all successfully went into bag.
    - US402 - Edit shopping bag and remove items from bag
      - As a **site user** I can **modify my shopping bag even after putting keys in my bag** so that **I can manage the shopping bag even if erros have been made or have any changes**
      - Testing Complete:
        - Was able to update product quantity and remove items from bag.
    - US403 - See user notification on actions
      - As a **site user** I can **get a notification on the screen of my actions** so that **I can easily confirm that my interaction with the website too place**
      - Testing Complete:
        - When add a product or remove a product notification message is displayed.
    - US404 - Finalise an order via checkout page
      - As a **site user** I can **complete an order on the checkout page** so that **I can see my final total, a list of items and sumarry and specify a delivery adress and payment option**
      - Testing Complete:
        - Able to select secure checkout and taken to the checkout page.
    - US405 - Have a secure payment option
      - As a **site user** I can **enter payment details** so that **I can payment informtaion is secure and action is secure**
      - Testing Complete:
        - Entered card details into payment method and secure transaction went through
    - US406 - View an order confirmation after checkout
      - As a **site user** I can **view an order confirmation after checkout** so that **I can see what was ordered and the final cost**
      - Testing Complete:
        - Was able to see order confirmation and a notification of email sent to email entered upon checkout.
    - US407 - Recive email confirmation of order after checkout
      - As a **site user** I can **recive and email confirmation after checkout completion** so that **I can have a record of all my purchase as a backup**
      - Testing Complete:
        - Recieved and email with details of my order.
<br>

- US501 - Add a product
      - As a **site admin** I can **add a product** so that **I can sell a new product on the store**
      - Testing Complete:
        - Logged into admin account and was able to create a test key to add to products page.
    - US502 - Add a employee
      - As a **site admin** I can **add a new employee** so that **I can update our team roster on the website**
      - Testing Complete:
        - Logged into admin account and enter a new employee to the site.
    - US503 - Add a service
      - As a **site admin** I can **add new services** so that **I can offer more services along with products**
      - Testing Complete:
        - Logged into admin account and able to create and new service that is displayed on the services page.
    - US504 - Edit or update product, employee or service
      - As a **site admin** I can **change and details to uploaded inforion or update** so that **I can keep store information up to date fresh**
      - Testing Complete:
        - Edited updated both test employee and the test service and the test key
    - US505 - Delete a product, employee or service
      - As a **site admin** I can **remove a product, employee or server** so that **I can remove a product, and employee or service from the database**
      - Testing Complete:
        - Was able to delete both the test employee and the test service and the key aswell
<br>

- US601 - View company facebook page
      - As a **site admin** I can **find the company on facebook** so that **I can view and keep up to date with company posts**
      - Testing Complete:
        - Checked facebook links and the active Facebook page to show working.
    - US602 - Subscribe to newsletter
      - As a **site admin** I can **subscribe to company newsletter** so that **I can get company news and offers**
      - Testing Complete:
        - Subscribed to newsletter and checked inside of MailChimp and email was added to mailing list
    - US603 - SEO
      - As a **site admin** I can **find the site through web searches** so that **I can easily acces the site**
      - Testing Complete:
        - Checked all pages to include, Descriptions, Keywords and alt tags to any avalible options.

# Deployment
I used the following steps to deply to Heroku:

## Deploying by connecting Githun to heroku
1. Top right corner in heroku select Create New App
2. I call the app P5-CDS-Car-Keys and set region to "Europe"
3. Once the app is created i choose deployment method for "Connect to github"
4. After logging in and authenticating GitHub, i typed in and selected my repo that i was using for my project.
5. When the repo appeared, I clicked Connect Button.
6. Once connected i had the option to deploy.
7. I went to my setting in heroku and added all the Enviroment varibles to config vars
8. Once i was ready, i went to my virtual enviroment and did `pip3 freeze --local > requirements.txt`
9. Once completed i created a Procfile that ran the command, `web gunicorn cds_car_keys.wsgi` 
10. Once all completed i ran `git add .`, `git commit -m 'final deploy`, `git push`
11. Then i went back to heroku dashboard and selected deploy.
12. Waited for heroku to deploy my app and then finished.

## Credits
- CodeInstitue Boutique Ado - Project was used as a base and then fully expanded, gave the groundwork and idea to build up from.
- [Codemy.com](https://www.youtube.com/@Codemycom) Some very helpful advice and able to see how others do it and make my own or use advices.

### Acknowledgements
Would like to thank my mentor Brian Macharia who has helped very much all throught this assignment.
Along with CodeInstitute Tutors have been a great asistance.