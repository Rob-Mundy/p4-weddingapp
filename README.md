# Union Wedding App Website

[View the live project here](https://rm-weddingapp.herokuapp.com/)

The Union Wedding App website is designed to be responsive, allowing visitors to view it on a range of devices.

![Union Wedding App Website shown on a range of devices](assets/images/…..)

## CONTENTS

* [User Experience (UX)](#User-Experience-(UX))

* [Design](#Design)

* [Technologies Used](#Technologies-Used)

* [Setup & Deployment](#Setup-&-Deployment)

* [Testing](#Testing)
  
* [Credits](#Credits)

- - -

## User Experience (UX)

### Initial Discussion

Union Wedding App is an online wedding planning application that enables site users to create and manage guestlists and record their attendees’ preferences.  Future developments would include the ability to design and send wedding invitations to guests via email, as well as receive and update results from guests’ RSVPs.

#### Key information for the site

* When is the site user's wedding event
* Who are the potential wedding guests
* What are the wedding attendees' preferences
* How can the site users get in touch via social media

### User Stories

#### First Time Visitor Goals

* USER STORY: Understand the website - As a **First Time Visitor** I can **understand what the site offers** so that **I can decide whether to register**
* USER STORY: Social Links - As a **First Time Visitor** I can **view social media account links** so that **I can get a better appreciation for the company and get in contact**
* USER STORY: Register Account - As a **First Time Visitor** I can **easily register my account** so that **I can access site functionality**

#### Returning User Goals

* USER STORY: Easy Navigation - As a **Site User** I can **easily navigate the site** so that **I don't get stuck**
* USER STORY: Register Account - As a **First Time Visitor** I can **easily register my account** so that **I can access site functionality**
* USER STORY: View user-specific content - As a **Site User** I can **view my user-specific guestlist** so that **I don't accidentally contact people I don't know**
* USER STORY: Create Wedding Event - As a **Site Admin** I can **create an event** so that **I can access site functionality**
* USER STORY: Edit Wedding Event - As a **Site User** I can **edit an event** so that **I can correct mistakes or accommdate changes**
* USER STORY: Add Guests - As a **Site User** I can **add guests** so that **I can build a list of potential attendees**
* USER STORY: Edit Guests - As a **Site User** I can **edit guests** so that **I can make alterations to a list of potential attendees**
* USER STORY: Delete Guests - As a **Site User** I can **delete guests** so that **I can correct mistakes in a list of potential attendees**


#### Incomplete/Future User Goals

* USER STORY: Create invite - As a **Site User** I can **create an invite** so that **I can tailor messages to suit my tastes** 
* USER STORY: RSVP - As a **Guest Recipient User** I can **RSVP** so that **I can accept or decline an invitation and advise as to my preferences**
* USER STORY: View List of Attendees - As a **Site User** I can **view/filter list of attendees** so that **I can make informed  decisions based on criteria**

## Design

### Colour Scheme

![Union Wedding App Website Colour Palette](static/images/lilac_pallette.png)

The color scheme for the website was created via [Coolors](https://coolors.co/), utilizing a pastoral wedding scene photo as the basis for generating the palette. To ensure adequate contrast for various site elements, tonal variations were carefully selected.

### Typography

Two Google Fonts Were used throughout the website:

* Playfair Display is used for headings on the site. It is a serif font that is often seen in high-end, luxury branding and editorial design due to its elegant and sophisticated appearance.

* Figtree is used for the body text on the site. It is a sans-serif font that is characterised by its clean lines and minimalist design that improves readability.  

### Imagery

All images were used with the permission of their owners, all of which have been credited in the [credits](#Credits) section.

### Mockups

A mockup for the desktop was created for the homepage in Excel.

[Home Page Mockup](static/images/homepage_mockup.png)

### Features

The website currently comprises three main pages: the landing page prior to login, the homepage visible to the authenticated user, and the guestlist page. Available pages change according to user actions as explained below.

* All website pages extend the base.html that includes:

  * A header positioned at the top of the page, featuring the website name, Union, along with a responsive nav bar and a tagline offering the user "a helping hand for your big day". The nav bar is located in a familiar place and collapses to a hamburger icon on smaller devices so as not to crowd the screen and enhance the user experience. The nav bar initially displays three links for the unauthenticated user: Home, Sign Up, and Log In. When authenticated this changes to Home and Logout(username), and when the user has created a wedding Event the Guestlist link appears.  

  * A footer containing links to fictitious social media accounts; instagram, facebook and twitter. Icons were chosen to maintain a familiar and uncluttered appearance.

* Home Page.
  * Section 1
  Section 1 content
  * Section 2   
  Section 2 content
  * Section 3
  Section 3 content

* Home Page (authenticated)
  * Section 1
  Section 1 content
  
* Guestlist
  * Section 1
  Content

* Future Implementations.
  * Allow users to create wedding invitations containing uploaded pictures and messages of their choosing.
  * Connect a mail account so that guests can be sent invites via email.
  * Enhance the Attendees card on the homepage to display various statistics such as total guests invited, total guests attending, as well as tallies of various dietary requirements e.g. 10 x vegetarians, 5 x teetotal.

### Accessibility

Throughout the coding process, I have made a conscious effort to prioritize website accessibility. This has been accomplished through several measures, including implementing semantic HTML, adding descriptive alt attributes to images, providing information for screen readers in instances where icons are used instead of text (such as footer icons), maintaining sufficient color contrast across the site, and making sure that menus are easily navigable for users with screen readers by indicating the current page.

- - -

## Technologies Used

### Languages Used

HTML and CSS and Python were used to create this website.

### Frameworks, Libraries & Programs Used

Django==3.2.18 - Framework used to simplify Python programming

    django-allauth==0.52.0 - used for site authentication

    django-crispy-forms==1.14.0 - used for form validation

    python-slugify==8.0.1 - used for creating slugfield values

elephantSQL - To house the postgreSQL database

Heroku - For deployment

Cloudinary - As a cloud image repositary

Git - For version control.

Github - To create issues from user stories and manage via Kanban board.

Bootstrap - Framework code used throughout the website including: Nav bar, Hero image, Guestlist listgroup. Amendments to Bootstrap classess and custom stylings were added via a separate style.css file saved in the static folder.

Google Fonts - To select and import the fonts used throughout the website.

Font Awesome - To select and import the iconography for the Social footer links.

Google Dev Tools - For testing, troubleshooting, and improving accessibility and responsivenes.

- - -

## Setup-&-Deployment

### Setup Django and supporting libraries

This project was created using the Django framework, which was installed as follows:

+ In the Terminal:

    + Install Django and gunicorn: pip3 install 'django<4' gunicorn

    + Install supporting libraries: pip3 install dj_database_url psycopg2

    + Install Cloudinary Libraries: pip3 install dj3-cloudinary-storage

    + Create requirements file:	pip3 freeze --local > requirements.txt

    + Create Project: django-admin startproject union . 

    + Create App: python3 manage.py startapp weddingapp

+ In settings.py:

    + Add to installed apps: INSTALLED_APPS = [
    …
    'weddingapp']

    + save file

+ In the Terminal:

    + Migrate Changes: python3 manage.py migrate

    + Run Server to Test: python3 manage.py runserver


### Setup external database

elephantSQL.com was used to create the postgreSQL database via the following process:

+ Log in to elephantSQL account

+ Click “Create New Instance”

+ Name the plan and select the Tiny Turtle (Free) plan

+ Click “Select Region” and select a nearby datacenter

+ Click “Review”, check the details are correct, and click “Create instance” 

+ Click on the database instance name for this project on the dashboard and make a note of the  ElephantSQL database URL to add to env.py and Heroku

Return to Gitpod to attach the database as follows:

+ Create env.py file on top level directory and while inside:

    + Import os library: import os

    + Set environment variables: os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"

    + Add a secret key that has been generated via [Djecrety](https://djecrety.ir/): os.environ["SECRET_KEY"] = "Paste in Djecrety secret key"


### Deployment

This project was deployed to Heroku via the following process:

+ From the homepage click "New" then "Create new app"

+ Give the project an appropriate name, rm-weddingapp in this case, select "Europe" as the region then click "Create app"

+ In the "Settings" tab, click Reveal Config Vars

+ Add the following Config Vars:
    + DATABASE_URL = Paste in ElephantSQL database url. 

    + SECRET_KEY = Paste in Djecrety secret key. 

    + CLOUDINARY_URL = Paste in Cloudinary URL 

    + DISABLE_COLLECTSTATIC = 1 (temporary step, disable before deployment)

+ In the "Deployment" tab, select "GitHub - Connect to GitHub" as the Deployment method

+ Search for the GitHub project name, "Rob-Mundy/p4-weddingapp", in the "Search for a repository to connect to" search box

+ Click the "Connect" button at the bottom of the page

+ When connected, scroll to the bottom of the page and in the "Manual deploy" section, select "main" as the chosen branch to deploy and click "Deploy Branch"

+ Following a short build process, a link to the project becomes available

+ Click "View" to [open the project in a new window](https://rm-weddingapp.herokuapp.com/)

- - -

## Testing

The following considerations were highlighted during a tutoring session:

* Given the time constraints, the initial project scope would be overly ambitious. Therefore, it will be crucial to employ an Agile approach to prioritize feature implementation in a logical sequence.
* The OneToOne replationship between the User and the Event model may be unsuitable.

### W3C Validator



### Solved Bugs

1. I twice attempted to implement AJAX to update the guestlist page without requiring a page refresh.  The first occasion was with HTMX, which required a change to my model.  Unfortunately, the changes created issues with the database which meant that it had to be dropped. In order to do this, the following process was observed: 
    + Remove Django migrations:
      Remove all migrations files within the project. Go through each of the project apps' migration folders and remove everything inside except the __init__.py file.
    + Drop the database:
      Navigate to the Elephant SQL dashboard, select the correct database, and click the reset button.
    + Re-configure project:
      In the GitPod Terminal, run the commands ""python3 manage.py makemigrations"" and ""python3 manage.py migrate"" to remake migrations and setup the new database.
      Create a new superuser by running: "python manage.py createsuperuser".

2. "I faced a challenge in preventing the entry of duplicate guests due to the slug field that's added within the post method of the Guest object. Since the guest_name field is not unique, it was important to differentiate between multiple individuals with the same name in order to access the edit_guest page via the slug field. I ultimately decided to allow only a single instance of each guest name per user, with variations created as necessary. However, implementing guest_name validation prior to the slugfield validation proved difficult. To address this issue, I pre-populated the user on the AddGuestForm as a hidden field and incorporated the following constraints to the Guest model, which were then validated by Crispy Forms.:
constraints = [models.UniqueConstraint(fields=['user', 'guest_name'],  name='unique guest for each user')]"

### Known Bugs

1. 

### Testing User Stories

* First Time Visitors
  * 

  ![website]()

  * 

  *

* Returning Users
  *



  * 
 

### Lighthouse

To assess the website's performance, accessibility, adherence to best practices, and search engine optimization, I utilized Lighthouse, a tool available within the Chrome Developer Tools.

#### Index Page

![Lighthouse desktop score for index.html](/static/images/lighthouse_home_page_desktop.png)

### Full Testing

In order to conduct a thorough examination of my website, I utilized a variety of browsers, including Google Chrome, Microsoft Edge, and Mozilla Firefox, as well as different devices such as the Lenovo ideapad 330S 14 inch laptop inch and Xiaomi Pocophone.  I was unable to test with the Safari browser as I do not have access to any Apple devices.

Furthermore, I employed Google Chrome's developer tools to scrutinize each page and guarantee that they exhibited proper responsiveness across all screen sizes.

Links.

1. I conducted a comprehensive evaluation of every link featured on the index page, including nav elements and buttons, and found that all links performed as anticipated. Social links open to the correct websites in new windows.
2. I conducted a comprehensive evaluation of every link featured on the guestlist page, including nav elements and buttons, and found that all links performed as anticipated.

Forms

I opted to utilize Crispy Forms for its powerful form validation features. I thoroughly tested the forms to ensure they functioned correctly and effectively alerted users when incomplete or inaccurate information was provided. Here are the results of the tests:

1. Sign-up form

    + [sign up form validation: username not unique](/static/images/sign_up_form_validation_duplicate_username.png)
    + [sign up form validation: email doesn't conform](/static/images/form_validation_email_prompt.png)
    + [sign up form validation: password too common](/static/images/sign_up_form_validation_common_password.png)
    + [sign up form validation: password mismatch](/static/images/sign_up_form_validation_password_mismatch.png)

2. Create event form

    + [create event form validation: invalid date](/static/images/create_event_date_validation_prompt.png) 
    + [create event form validation: invalid time](/static/images/create_event_form_validation_time.png)

3. Edit event form

    + [edit event form validation: empty event name](/static/images/edit_event_form_validation_empty_event_name.png)

4. Add guest form

    + [add guest form validation: empty guest name](/static/images/add_guest_form_validation_empty_guest_name.png)

    + [add guest form validation: duplicate guest name](/static/images/add_guest_form_guest_duplication_prompt.png)

5. Edit guest form

    + [edit guest form validation: email doesn't conform](/static/images/edit_guest_form_validation_email.png)

    + [edit guest form validation: dietary requirements missing](/static/images/edit_guest_form_validation_dietary_requirements.png)

- - -

## Credits

### Code Used


### Content

All content for the website was written by Robert Mundy.

### Media

#### Hero Image 

### Acknowledgments
