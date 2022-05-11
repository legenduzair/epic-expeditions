# <div align="center">Epic Expeditions</div>

## Project Overview
Epic Expeditions is a web application that allows the target audience to browse & create reviews of global destinations and engage in conversations with other users who are also authenticated on the website. Epic Expeditions also offers a mini weather application that allows users to search for current weather conditions of any city worldwide.

This project was implemented with the purpose of developing a full-stack Django application with use of Bootstrap, HTML, CSS, JavaScript & Python as the programming tools used. It utilises CRUD functionality that allows authenticated users to create, browse, update and delete expedition reviews to the website. The weather application is implemented using [OpenWeatherMap API](https://openweathermap.org/). The allauth Django library is used to implement registration and signing in of users.

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
All images used for developing the website are acquired from [Unsplash](https://unsplash.com/images/stock/royalty-free). Images used to add test expedition reviews were acquired from my file explorer on my personal computer.

### Icons
The main logo of the website and two weather icons (humidity and wind speed) were acquired from [Font Awesome](https://fontawesome.com/). The pressure weather icon was acquired from [Flat Icon](https://www.flaticon.com/).

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

## Testing

## Technologies Used

## Deployment

## Credits


    