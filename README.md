# <div align="center">Epic Expeditions</div>

## Project Overview
Epic Expeditions is a web application that allows the target audience to browse & create reviews of global destinations and engage in conversations with other users who are also authenticated on the website. Epic Expeditions also offers a mini weather application that allows users to search for current weather conditions of any city worldwide.

This project was implemented with the purpose of developing a full-stack Django application with use of Bootstrap, HTML, CSS, JavaScript & Python as the programming tools used. It utilises CRUD functionality that allows authenticated users to create, browse, update and delete expedition reviews to the website. The weather application is implemented using [OpenWeatherMap API](https://openweathermap.org/). The allauth Django library is used to implement registration and signing in of users.

![Website Image](/media/screenshots/website-image.png)

[View the live website on Heroku.](https://epic-expeditions.herokuapp.com/)

## Table of Contents
- [UX & Planning](https://github.com/legenduzair/epic-expeditions#ux--planning)
  - [Project Strategy](https://github.com/legenduzair/epic-expeditions#project-strategy)
    - [Project Goal](https://github.com/legenduzair/epic-expeditions#project-goal)
    - [Target Audience](https://github.com/legenduzair/epic-expeditions#target-audience)
  - [Project Scope](https://github.com/legenduzair/epic-expeditions#project-scope)
    - [Site Owner Goals](https://github.com/legenduzair/epic-expeditions#site-owner-goals)
    - [Entity Relationship Diagram](https://github.com/legenduzair/epic-expeditions#entity-relationship-diagram)
    - [Agile Methodology - User Stories](https://github.com/legenduzair/epic-expeditions#agile-methodology---user-stories)
  - [Project Structure](https://github.com/legenduzair/epic-expeditions#project-structure)
  - [Project Skeleton](https://github.com/legenduzair/epic-expeditions#project-skeleton)
   - [Wireframes](https://github.com/legenduzair/epic-expeditions#wireframes)
  - [Surface Design](https://github.com/legenduzair/epic-expeditions#surface-design)
    - [Colour Scheme](https://github.com/legenduzair/epic-expeditions#colour-scheme)
    - [Typography](https://github.com/legenduzair/epic-expeditions#typography)
    - [Images](https://github.com/legenduzair/epic-expeditions#images)
    - [Icons](https://github.com/legenduzair/epic-expeditions#icons)
- [Features](https://github.com/legenduzair/epic-expeditions#features)
  - [Home Page](https://github.com/legenduzair/epic-expeditions#home-page)
  - [Navigation Header](https://github.com/legenduzair/epic-expeditions#navigation-header)
  - [Footer](https://github.com/legenduzair/epic-expeditions#footer)
  - [Expedition Reviews List](https://github.com/legenduzair/epic-expeditions#expedition-reviews-list)
  - [Expedition Review Detail](https://github.com/legenduzair/epic-expeditions#expedition-review-detail)
    - [Comments](https://github.com/legenduzair/epic-expeditions#comments)
    - [Edit or Delete Review](https://github.com/legenduzair/epic-expeditions#edit-or-delete-review)
  - [Add a Review](https://github.com/legenduzair/epic-expeditions#add-a-review)
  - [Authentication](https://github.com/legenduzair/epic-expeditions#authentication)
    - [Register Page](https://github.com/legenduzair/epic-expeditions#register-page)
    - [Sign In Page](https://github.com/legenduzair/epic-expeditions#sign-in-page)
    - [Sign Out Page](https://github.com/legenduzair/epic-expeditions#sign-out-page)
  - [Weather App](https://github.com/legenduzair/epic-expeditions#weather-app)
- [Future Improvements](https://github.com/legenduzair/epic-expeditions#future-improvements)
- [Testing](https://github.com/legenduzair/epic-expeditions#testing)
- [Technologies Used](https://github.com/legenduzair/epic-expeditions#technologies-used)
  - [Languages & Frameworks](https://github.com/legenduzair/epic-expeditions#languages--frameworks)
  - [Packages](https://github.com/legenduzair/epic-expeditions#packages)
  - [Resources](https://github.com/legenduzair/epic-expeditions#resources)
- [Deployment](https://github.com/legenduzair/epic-expeditions#deployment)
- [Credits](https://github.com/legenduzair/epic-expeditions#credits)

## UX & Planning

## Project Strategy
  
### Project Goal
  - The goal of this project is to create a platform that allows users to share their experiences of expeditions they have been on around the world and evaluating them. A secondary goal for the project is that users can have the ability to check live weather updates of their favourite expeditions they have been on by searching for a city.

### Target Audience
  - Users who love to go travelling.
  - Users who love to share their thoughts on places they have visited with others.
  - Users who want to gain an insight of places around the world before they go themselves.

## Project Scope

### Site Owner Goals
  - Build a platform that is easy to navigate and has an intuitive user interface.
  - Website developed must be visually appealing on all screen sizes.
  - Build a platform that is user-friendly and is accessible to all.

### Entity Relationship Diagram
  - As this project utilises Django which is a MVT(Model, View & Template) framework, a connection to database tabels or 'Models' is required. An entity relationship diagram was created to visually map out the structure of the databases & models. The entity relationship diagram is mapped out below. 

  #### Reviews App
  | **Reviews Models** | **PK** |
  | ----- | ----- |
  | Review Title | CharField |
  | Slug | SlugField |
  | Author | ForeignKey |
  | Content | TextField |
  | Travel Image | Cloudinary Field |
  | Excerpt | TextField |
  | Published | DateField |
  | Ratings | IntegerField |
  | Likes | ManyToManyField |

   | **Comments Models** | **PK** |
  | ----- | ----- |
  | Review Post | ForeignKey |
  | Name | CharField |
  | Body | TextField |
  | Created On | DateTimeField |

### Agile Methodology - User Stories
  - All forms of agile methodology were managed using GitHub Issues through implementing user stories gaining potential perspectives of a target user.

  | **User Story Label** | **As a:** | **I can:** | **So that:** |
  | ----- | ----- | ----- | ----- |
  | Account Registration | | | |
  | 1 | Site user | Register for an account by choosing a username, email address & password | I can have a personal account to post reviews and comments |
  | 2 | Site user | Login and logout | Only I can access my personal account |
  | 3 | Site user | Recover my password if it has been forgotten/stolen/corrupted | I can recover access to my account |
  | View & Navigate | | | |
  | 1 | Site user | View all travel reviews posted by other users | I can browse through all reviews posted by registered users and also select a specific review to read in detail |
  | 2 | Site user | Click on a travel review | I can read the full review which contains more information such as full text, image of the destination and ratings |
  | 3 | Site user | View the ratings of the travel destinations on their corresponding reviews | I can see which is the most popular destinations to visit |
  | 4 | Site user | View comments made by registered users on reviews | I can read the conversation between different users |
  | 5 | Site user | Navigate through different pages | I can view all of the reviews posted on the website |
  | 6 | Site user | Search for travel reviews by entering the place of interest on the navbar | I can easily access a review of a specific destination I would like to view |
  | 7 | Site user | Filter the travel reviews by date (ascending or descending), ratings or alphabetical order | I can select a travel review of a specific destination |
  | Creating a Review/Review Management | | | |
  | 1 | Registered user | Create a review on a travel destination | My review is posted on the website for others to view and comment on |
  | 2 | Registered user | Input an image I have personally taken of the destination in my review | Other users can view the uploaded image on my review |
  | 3 | Registered user | Input full text into my review | Other users including myself can view my full thoughts of the destination I have visited |
  | 4 | Registered user | Input a rating from one to five stars for the destination I have visited in my review | I can rate the place of travel and other users can have the opportunity to view my opinion of the place |
  | Editing a Review/Review Management | | | |
  | 1 | Registered user | Edit my travel review/s that I have posted | I can update images uploaded, edit full text of the review or edit the ratings I have given the travel destination |
  | Deleting a Review/Review Management | | | |
  | 1 | Registered user | delete any uploaded reviews | I can remove this off the website so other users cannot view it |
  | Comments Management | | | |
  | 1 | Registered user | Post a comment on a travel review | Other users can view my comment and engage in a conversation with me |
  | 2 | Registered user | Edit or delete a comment I have posted on a travel review | The comment is updated/removed from the review so that other users cant view it |
  | Comments Management/Review Management | | | |
  | 1 | Registered user | Enter my full name into the author field when creating a review/posting a comment| Other users can see who is posting the relevant content |
  | Weather Management | | | |
  | 1 | Site user | Click on the weather tab on the navbar | I can divert to the page which contains the weather app |
  | 2 | Site user | Search for a travel destination(city) in the search bar | I can view full details of the weather for that corresponding travel destination |
  | Administration Access | | | |
  | 1 | Site admin | Create, read, update and delete travel reviews posted on my website | I can manage and filter out undesirable travel review content |
  | 2 | Site admin | Create, read, update and delete comments posted on travel reviews | I can manage and filter out undesirable comments |

## Project Structure
  - Epic expeditions uses HTML, CSS, JavaScript & Python to create a user-friendly and intuitive web application. This project focuses on using Django/Jinja syntax to structure the code to make it more cleaner and readable during the development stage. This web application is aimed to contain a responsive and user-friendly layout so it can be accessible across different browsers & devices of various screen sizes. 
  - The navbar is placed at the top of the webpage in a fixed position with navigation links displayed to the user to access different pages of the site. On smaller screen sizes, the navbar is converted into a hamburger menu to allow users to access the navigation links with ease.
  - The expedition reviews are structured in card-containers which are all the same height and width to keep consistency. Eight reviews are paginated on one webpage and if more reviews are added, the user will have an option to redirect onto the next page.
  - Each expedition review can be clicked on to access special actions such as liking and commenting, which only authenticated users can perform.
  - Users can be authenticated by click on the 'register' and 'sign in' navigation links which redirects them to a form.
  - The CRUD functionality is also incorporated into the project structure as authenticated users can add, update & delete their expedition reviews.
  - The weather app is implemented into the project, where users can search for weather details of their favourite cities worldwide. Performing a search will result in a weather card with these details stated, structured beneath the search bar.   

## Project Skeleton

### Wireframes
  - Before initiating the project, I planned the general layout and structure of the main content for each page of the website across various screen sizes; desktop, tablet and mobile. The wireframes below were designed using Balsamiq Wireframes:
    - [Landing Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/landingpage-wf.png)
    - [Reviews Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/reviewpage-wf.png)
    - [Full Review Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/fullreview-wf.png)
    - [Add Review Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/addreview-wf.png)
    - [Register Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/registerpage-wf.png)
    - [Login Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/loginpage-wf.png)
    - [Weather App Page](https://github.com/legenduzair/epic-expeditions/blob/main/media/wireframes/weatherpage-wf.png)

## Surface Design

### Colour Scheme
After completing the layout of the wireframes to create a skeleton for the project, I selected the colour scheme by generating a colour palette on [Coolors](https://coolors.co/). The colours from the palette were used as they had high level of colour contrast to maximise user accessibility. The colour palette is shown below. 

![Colour Palette generated on Coolors](/media/screenshots/color_scheme.png)

The colours implemented in the navbar and weather search bar were generated using a gradient on [CSS Gradient](https://cssgradient.io/).

### Typography
When designing the website, I had carefully chosen two complimentary fonts from [Google Fonts](https://fonts.google.com/); 'Quicksand' and 'Source Sans Pro'. It is important that the text on the website is clear & easy for users to read and is not too unappealing to the human eye. The letters are spaced out correctly and the style of the font fits the scheme of the website; Travelling.

### Images
All images used for developing the website are acquired from [Unsplash](https://unsplash.com/images/stock/royalty-free) and were uploaded into my code using [Cloudinary](https://cloudinary.com/). Images used to add test expedition reviews were acquired from my file explorer on my personal computer.

### Icons
The main logo of the website and two weather icons (humidity and wind speed) were acquired from [Font Awesome](https://fontawesome.com/). The pressure weather icon was acquired from [Flat Icon](https://www.flaticon.com/). The favicon was acquired from Font Awesome and was converted into a 32x32 PNG file on [Favicon.io](https://favicon.io/).

## Features

### Home Page
The home page aims to welcome the user to Epic Expeditions with a welcome message and slogan underneath. There is also an interactive button that navigates the user to the expeditions review list page to allow them to browse what is already posted by other users. The background image of the home page is vibrant to provide the user with a happy vibe when first glancing at the website.

![Epic Expeditions Home Page](/media/screenshots/homepage-ss.png)

### Navigation Header
The main navigation bar is located at the top of the webpage, displaying name of the website with a logo and navigation links that the user would require. 

![Main Navbar](/media/screenshots/navbar-ss.png)

If the user is authenticated on the website, a secondary user menu is available that display the 'Add Review' and 'Logout' navigation links instead of 'Register' and 'Sign In'. 

![Secondary Navbar](/media/screenshots/navbartwo-ss.png)

The navigation bar is fully responsive and adapts to devices with medium/smaller screen sizes by adding a hamburger menu. This hamburger icon can be selected to bring up a user menu that drops down below.

![Responsive Navbar](/media/screenshots/navbar-respo-ss.png)

### Footer
A consistent footer is used throughout the website on all pages which encourages the user to visit the social media accounts of the company. When a user clicks on any of the social media icons, the target website is opened in a new tab. The footer also lists copyright information.

![Footer](/media/screenshots/footer-ss.png)

### Expedition Reviews List
The expedition review listing page contains posted reviews of travel destinations by authenticated users. On this page, users can browse through these expedition reviews that are ordered by the published date in descending order.

![Expedition Reviews List](/media/screenshots/expeditionlist-ss.png)

Each expedition review on the listing page is displayed in its own review card. The structure of the card remains consistent across all expedition reviews. Each card contains the review title, an image of the expedition, a small excerpt, star ratings (out of 5), number of likes & comments and the author & published date. The excerpt is truncated if the length of the text is more than one line.

![Expedition Review Card](/media/screenshots/reviewcard-ss.png)

If there are more than eight expedition reviews on the review listing page and another review is posted, an interactive button will display to the user prompting them to navigate to the next review listing page. If the user is on the second page, it will provide them with an interactive button to redirect to the previous & first page.

![First Pagination Screenshot](/media/screenshots/paginationone-ss.png)

![Second Pagination Screenshot](/media/screenshots/paginationtwo-ss.png)

### Expedition Review Detail
When a user clicks on any expedition review card on the listing page, they will be taken to their respective review detail page. On this page, users can view the expedition review in detail. These include title of the review, an enlarged image of the expedition, the author & published date, the excerpt, star ratings and the detailed expedition review text which is located on the right. As well as this, the user also has an option to traverse back to the expedition reviews list page in the form of an interactive button. If the user is not authenticated, there is a line of text which prompts the user to sign in to like the review or leave a comment. The number of likes and comments are also listed.

![Expedition Review Detail](/media/screenshots/expeditiondetail-ss.png)

If the user is authenticated, they will have an option to like the review and post a comment in the comments section.

![Likes & Comments Section](/media/screenshots/likecomment-ss.png)

The user is able to click on the like button (heart) which fills it with a green colour that indicates to the user that they liked the review. The text also changes. 

![Likes Feature](/media/screenshots/likeheart-ss.png)

#### Comments 

The expedition review detail page also includes a comments section that provides the user with an option to engage in conversations with other registered users. The comments section is located at the bottom of each review detail page. If the user is not signed in, the webpage will display a message prompting the user to sign in to leave a comment. Comments posted by other users are visible to anyone. If there are no comments, the webpage will display a message indicating that there are no comments posted.

![Comments Section One](/media/screenshots/commentsone-ss.png)

If the user is authenticated and logged in, a text-box will appear prompting the user to leave a comment. Comments posted on a review will be displayed with the author, the published date & time and the content of the comment.

![Comments Section Two](/media/screenshots/commentstwo-ss.png)

#### Edit or Delete Review
An expedition review that is posted by a specific user has the ability to edit or delete the review. The 'Edit Review' and 'Delete Review' buttons will be displayed to the user on their post on the expedition review detail page. It is important to note that other authenticated users cannot edit or delete other users reviews. 

![Edit & Delete Buttons](/media/screenshots/editdelete-ss.png)

If the user decides to edit the review, they will be navigated to the edit review page where they can edit any details of the review by completing the form.

![Edit Review Form](/media/screenshots/editreview-ss.png)

If the user decides to delete the review, they will be navigated to a webpage that requests to confirm if they want to make this deletion. The details of the review are also listed to make sure the correct post is deleted. This confirmation of deletion was inputted into the project as use of defensive programming. If the user clicks on 'Delete Review', the review is deleted from the database.

![Delete Review Page](/media/screenshots/deletereview-ss.png)

### Add a Review
The Add Review page will be displayed among the navigation links in the header if the user is authenticated and signed in. Clicking on this link will navigate the user to the Add Review page where they will be required to complete the fields in the form. These fields include title of the review, image, exceprt, review content and star ratings (out of 5). Once the form is filled out, the user will be prompted to select the 'Add Review' button where they will be redirected to the expedition reviews list page. The user will see their newly posted review at the top.

![Add Review Page](/media/screenshots/addreview-ss.png)

### Authentication
To access many of the website features, the user will be required to register for an account and sign in using their credentials. To implement authentication in this project, I have used Django's own library; allauth. If the user is not authenticated, the navigation links will contain 'Register' and 'Sign In'.

#### Register Page
The register page contains a registration form that prompts the user to complete it by entering their email address, username and password (twice).

![Register Page](/media/screenshots/registerpage-ss.png)

#### Sign In Page
The sign in page contains a sign in form that prompts the user to fill it in by entering their email address/username and password. If the user doesn't have an account, they can opt to select the 'create new' button.

![Sign In Page](/media/screenshots/signinpage-ss.png)

#### Sign Out Page
If the user is logged in, they will have the option to sign out by clicking on the 'Logout' navigation link. This will navigate them to the sign out page where the website will request to confirm they want to logout. 

![Sign Out Page](/media/screenshots/signoutpage-ss.png)

### Weather App
Epic Expeditions has a mini-weather app which uses [OpenWeatherMap API](https://openweathermap.org/) to pull data of current weather for any city globally. Any user can access this by clicking on the 'Weather' navigation link in the navbar. The user will be prompted to search for any city name by entering it into the search bar and clicking the interactive search button.

![Weather App](/media/screenshots/weatherapp-ss.png)

After searching for a city, the webpage will gather data from the API and display it on a weather card. The weather card has details such as the city name, country code, local time, temperature in degrees (Celsius), small description of the weather, weather icon, wind speed, humdity and pressure. These weather details are all in real-time.

![Weather Card](/media/screenshots/weathercard-ss.png)

## Future Improvements
There are several improvements to functionality that I would like to implement in the future. Some of these improvements have been gathered from the user stories on GitHub Issues project kanban board. These user stories have not been completed and would be implemented as future enhancement opportunities. These include:

  - The ability to recover a user's password if it has been stolen/forgotten/corrupted. This functionality is part of the allauth library which has already been installed in this project but only needs to be setup to make this functional. 
  - The ability for users to search for travel reviews using a search bar implemented in the navigation header. 
  - The ability for users to filter travel reviews by date (ascending or descending), ratings or alphabetical order.
  - The ability for users to edit and delete their posted comments under an expedition review.

## Testing

A full detailed breakdown of all testing strategies and code validation techniques is documented in a separate file called [TESTING.md](https://github.com/legenduzair/epic-expeditions/blob/main/TESTING.md).

## Technologies Used

### Languages & Frameworks

The follow programming languages & frameworks were used in the development of this project:

 - Python 
   - The following python packages were installed and used for this project:

   ![Installed Python Packages](/media/screenshots/requirementstxt-ss.png)

 - Django
   - Django was used as the primary Python framework for this project.
   - Django's authentication library; allauth, was used to implement user account authentication.
  
 - Heroku
   - Heroku is the cloud based platform used to deploy this website and make it public.

 - Heroku PostgreSQL
   - Heroku PostgreSQL was used as the database choice for this project during development.
  
 - JavaScript
   - Custom JavaScript code was added to implement the star ratings feature for expedition reviews and message alerts that appear after a specific action is performed.
  
 - Bootstrap 4.5.0 & MD Bootstrap 4.19.1
   - Bootstrap framework was used to implement the navbar, footer and structure the general content across the project.

 - Font Awesome 5.15.4
   - Font Awesome icons were used in different sections of the project where appropriate.

 - CSS
   - Custom CSS was written to implement my own styling into the project. It was also used to add media queries to provide responsive across different viewport sizes.

 - Jinja/Django Templating
   - Jinja templating was used to insert information from the database into the website. This includes transferring the logic from the app models.py & views.py to the template HTML pages.

 - HTML 
   - HTML was the base language used to code the templates for the project.

### Packages

The following packages were used during development of my project:
  
  - Gitpod - IDE used for the development of the project.
  - VS Code - IDE used for the development of the project.
  - Git - Used for version control and transferring files from VS Code to the repository.
  - GitHub - Used to create respository to store files for this project.

### Resources

The following resources were used during development of my project:

  - Balsamiq Wireframes - Used to design the wireframes for the website.
  - DrawSQL.app - Used to sketch entity relationship diagram before documenting in the README.
  - Cloudinary - Used for hosting project media images and static files.
  - Summernote - Library used to create the WYSIWYG form editor.
  - Django Documentation - Used extensively during the development of the project.
  - Django AllAuth - Used to implement authentication of users to website.
  - OpenWeatherMap API - Used to create the weather app for the project.
  - W3Schools - Used as a general reference to research specific content.
  - StackOverflow - Very helpful reference to research specific content.

All other resources are referenced where appropriate.

## Deployment

Epic Expeditions was deployed via Heroku. The deployed website can be found here - [Epic Expeditions](https://epic-expeditions.herokuapp.com/)

To deploy the website to Heroku, I followed the steps below to initiate it.

### Installing Django & Supporting Libraries

Before intitiating development, I had to install Django and its supporting libraries on Gitpod.

In Gitpod's Terminal:
  1. Install Django & Gunicorn:
    - pip3 install 'django<4' gunicorn
  2. Install database:
    - pip3 install dj_database_url psycopg2
  3. Install Cloudinary libraries:
    - pip3 install dj3-cloudinary-storage
  4. Create requirements file:
    - pip3 freeze --local > requirements.txt
  5. Create project (in this case, epic_expeditions):
    - django-admin startproject epic_expeditions .
  6. Create apps (in this case, review):
    - python3 manage.py startapp review
    - The weather, home & errors were app were created later on during the development of the project.
In settings.py:
  7. Add to installed apps section. 
In Gitpod's Terminal:
  8. Migrate changes:
    - python3 manage.py migrate
  9. Run the server to test:
    - python3 manage.py runserver
  
### Creating Heroku App

The following steps can only be performed if an account is made on [Heroku](https://id.heroku.com/login).

  1. Create new Heroku app:
    - From the Heroku dashboard, select "New" and then select "Create New App".
  2. Name your Heroku app and select the region:
    - Give the project a unique name (in my case, epic-expeditions).
    - Select the region (in my case, Europe).
  3. Add database to the Heroku app:
    - Navigate to the "Resources" tab and in the add-ons section, search for "Heroku Postgres" and select it.
    - Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
  4. Acquire database URL:
    - Navigate to the "Settings" tab and select "Reveal Config Vars". Copy the "DATABASE_URL" for use in the upcoming steps.

### Attaching the Database

  1. Within the Django app respository, create a new file called "env.py".
  2. In the "env.py" file, import the os library:
    - Add "import os"
  3. Set environment variables:
    - Add 'os.environ["DATABASE_URL"] = "(Paste the DATABASE_URL key from Heroku"'
  4. Add in a custom secret key:
    - Add 'os.environ["SECRET_KEY"] = "(Make up your own key)"'
In Heroku.com:
  5. Add secret key to config vars:
    - Add the secret key that has just been created as SECRET_KEY for the KEY and the secret key value as the VALUE.

### Preparing our environment and settings.py file

  1. At the top of the settings.py file, add the following snippet:

    from pathlib import Path
    import os
    import dj_database_url
    if os.path.isfile('env.py'):  
      import env
    SECRET_KEY = os.environ.get('SECRET_KEY')
  
  2. Comment out the old Databases section:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
  
  3. Add new Databases section:

    DATABASES = {
      'default':
    dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
  
  4. In the terminal, make migrations migrate all changes:
    - python3 manage.py makemigrations
    - python3 manage.py migrate
  
### Setup Cloudinary
  
The following steps can only be performed if an account is made on [Cloudinary](https://cloudinary.com/).

  1. In Cloudinary, acquire the Cloudinary URL:
    - From the dashboard, copy the CLOUDINARY_URL
  In env.py:
  2. Add the Cloudinary URL to "env.py" file:
    - os.environ["CLOUDINARY_URL"] = "(Pasted cloudinary URL"
  In Heroku:
  3. Add Cloudinary URL to Heroku config vars:
    - Insert the CLOUDINARY_URL in config vars section as KEY and VALUE.
  4. Add Disable collect static to config vars:
    - Add DISABLE_COLLECTSTATIC as the KEY and 1 as the VALUE.
    - This should be removed before final deployment, otherwise static files will not load.
  In settings.py:
  5. Add Cloudinary libraries to installed apps:
    - Add 'cloudinary_storage' and 'cloudinary' in the INSTALLED_APPS section. The order they are stored is important; 'cloudinary_storage' goes above 'django.contrib.staticfiles'. 'cloudinary' goes below 'django.contrib.staticfiles'.
  6. Allow Django to use Cloudinary as media & static files storage:
    - Place the following snippet under "STATIC_URL = '/static/'":

    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

  7. Link files to the Templates directory inserting the snippet below (Place under the BASE_DIR line):

    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

  8. Change the templates directory to TEMPLATES_DIR (Place within the TEMPLATES array):

          TEMPLATES = [
          {
            …,
            'DIRS': [TEMPLATES_DIR],
            …,
              ],
            },
          },
          ]

  9. Add Heroku Hostname to ALLOWED_HOSTS array:
    - ALLOWED_HOSTS = ['epic-expeditions.herokuapp.com', 'localhost'] (in my case). 

### Setting Up Media & Static Files

  In Gitpod:
  1. Create three new folders at top level directory:
    - These folders are 'media', 'static' and 'templates'.
  2. Create a PROCFILE at top level directory:
    - Procfile
  In Procfile:
  3. Add this code:
    - web: gunicorn PROJ_NAME.wsgi
  4. Save all files.
  In the terminal:
  5. Add, Commit and Push:
    - git add .
    - git commit -m “Deployment Commit”
    - git push
  
In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors. Heroku will now build the app. Once the build is finished, the live site will be deployed with a Heroku link provided and a success message.

### Manual Deployment

When deploying Epic Expeditions, I was advised to use Gitpod's terminal to push any changes to Heroku as heroku & automatic deploys were down due to a breach in security. As a result, any final development changes I had made were pushed to Heroku using the command line interface on Gitpod. The following steps were performed to achieve this:
  
  1. Login Heroku account in the terminal:
    - Type "heroku login -i"
    - Enter email address and password.
  2. After logging into your Heroku account, link your Heroku app to the terminal:
    - Run the following command: "heroku git:remote -a (your_app_name_here)". In my case, my app name is epic-expeditions.
  3. After linking the app to the terminal, push any changes manually via the terminal:
    - Run the following command to push any changes to the deployed Heroku site: "git push heroku main".

### Local Deployment

If you want to clone this repository to make a copy that runs the project on a local machine, this can be achieved by following the steps below:

  1. Navigate to the respository you want to clone: https://github.com/legenduzair/epic-expeditions
  2. Select the "Code" button that is next to the green "Gitpod" button. A menu should dropdown.
  3. On the dropdown menu, select "HTTPS" and copy the URL it provides to the clipboard.
  4. On the code editor you are using, in the terminal change the directory to the location you want to clone the respository to.
  5. Run the command "git clone" and paste in the URL you copied from the clipboard earlier.
  6. Select enter and Git will clone the respository to your local machine.

After cloning the repository, it is important to create a virtual environment before installing any python libraries to the project to start working with it. It allows your device and projects to be secure. To do this, please follow the steps below:

  1. After cloning the repository in the terminal, create a virtual environment by running the command: python3 -m venv venv .
  2. Once complete, add the "venv" file to your ".gitignore" file. Then, run the command venv\Scripts\activate.bat in the terminal to install it. 

After this, you can install all the Python libraries needed to run this project by installing thje "requirements.txt" file.

  1. In the terminal, run the command pip3 install -r requirements.txt to add the Python libraries to this project. I did not need to do this as my project was developed from scratch. This means that I installed the libraries myself and added them to the "requirements.txt" file by running the command pip3 freeze > requirements.txt to generate it.

After this, you can create your own Heroku application, create the environmental variables and update the settings.py file as mentioned [above](https://github.com/legenduzair/epic-expeditions#creating-heroku-app). Finally, run the server in the terminal by entering python3 manage.py runserver .

## Credits

All references that assisted me in developing Epic Expeditions have been mentioned throughout the README file. However I would like to thank:

  - [Richard Wells](https://github.com/D0nni387) - The coding extraordinaire who is my project mentor. Richard was a huge help when developing this project.

    