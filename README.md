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
  | View & Navigate | | | |
  | 1 | Site user | View all travel reviews posted by other users | I can browse through all reviews posted by registered users and also select a specific review to read in detail |
  | 2 | Site user | Click on a travel review | I can read the full review which contains more information such as full text, image of the destination and ratings |
  | 3 | Site user | View the ratings of the travel destinations on their corresponding reviews | I can see which is the most popular destinations to visit |
  | 4 | Site user | View comments made by registered users on reviews | I can read the conversation between different users |
  | 5 | Site user | Navigate through different pages | I can view all of the reviews posted on the website |
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
  | Comments Management/Review Management | | | |
  | 1 | Registered user | Enter my full name into the author field when creating a review/posting a comment| Other users can see who is posting the relevant content |
  | Weather Management | | | |
  | 1 | Site user | Click on the weather tab on the navbar | I can divert to the page which contains the weather app |
  | 2 | Site user | Search for a travel destination(city) in the search bar | I can view full details of the weather for that corresponding travel destination |
  | Administration Access | | | |
  | 1 | Site admin | Create, read, update and delete travel reviews posted on my website | I can manage and filter out undesirable travel review content |
  | 2 | Site admin | Create, read, update and delete comments posted on travel reviews | I can manage and filter out undesirable comments |

## Project Structure


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
    