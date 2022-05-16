# <div align="center">Testing</div>

During and after the development of Epic Expeditions, the project went through rigorous testing to ensure a fully functional and responsive website was created. I have documented all the testing techniques used in the following sections.

## Automated Testing

## Manual Testing

### User Stories

All user stories were tested during and after development of this project. Below is a summary of the results acquired. The user stories that have not been completed have already been documented in the [Future Improvements](https://github.com/legenduzair/epic-expeditions#future-improvements) section.

| |**User Story**| **Achieved** |
| ----- | ----- | ----- |
| Account Registration | | |
| 1 | As a site user, I can register for an account by choosing a username, email address & password so that I can have a personal account to post reviews and comments. | Yes |
| 2 | As a site user, I can login and logout so that only I can access my personal account | Yes |
| 3 | As a site user, I can recover my password if it has been forgotten/stolen/corrupted so that I can recover access to my account. | No |
| View & Navigate | | |
| 1 | As a site user, I can view all travel reviews posted by other users so that I can browse through all reviews posted by registered users and also select a specific review to read in detail. | Yes |
| 2 | As a site user, I can click on a travel review so that I can read the full review which contains more information such as full text, image of the destination and ratings. | Yes |
| 3 | As a site user, I can view the ratings of the travel destinations on their corresponding reviews so that I can see which is the most popular destinations to visit. | Yes |
| 4 | As a site user, I can view comments made by registered users on reviews so that I can read the conversation between different users. | Yes |
| 5 | As a site user, I can navigate through different pages so that I can view all of the reviews posted on the website. | Yes |
| 6 | As a site user, I can Search for travel reviews by entering the place of interest on the navbar so that I can easily access a review of a specific destination I would like to view. | No |
| 7 | As a site user, I can Filter the travel reviews by date (ascending or descending), ratings or alphabetical order so that I can select a travel review of a specific destination. | No |
| Creating a Review/Review Management | | |
| 1 | As a registered user, I can create a review on a travel destination so that my review is posted on the website for others to view and comment on. | Yes |
| 2 | As a registered user, I can input an image I have personally taken of the destination in my review so that other users can view the uploaded image on my review. | Yes |
| 3 | As a registered user, I can input full text into my review so that other users including myself can view my full thoughts of the destination I have visited. | Yes |
| 4 | As a registered user, I can input a rating from one to five stars for the destination I have visited in my review so that I can rate the place of travel and other users can have the opportunity to view my opinion of the place. | Yes |
| Editing a Review/Review Management | | |
| 1 | As a registered user, I can edit my travel review/s that I have posted so that I can update images uploaded, edit full text of the review or edit the ratings I have given the travel destination. | Yes |
| Deleting a Review/Review Management | | |
| 1 | As a registered user, I can delete any uploaded reviews so that I can remove this off the website so other users cannot view it. | Yes |
| Comments Management | | |
| 1 | As a registered user, I can post a comment on a travel review so that other users can view my comment and engage in a conversation with me. | Yes |
| 2 | As a registered user, I can Edit or delete a comment I have posted on a travel review so that The comment is updated/removed from the review so that other users cant view it. | No |
| Comments Management/Review Management | | |
| *1 | As a registered user, I can enter my full name into the author field when creating a review/posting a comment so that other users can see who is posting the relevant content. | Yes |
| Weather Management | | |
| 1 | As a site user, I can click on the weather tab on the navbar so that I can divert to the page which contains the weather app. | Yes |
| 2 | As a site user, I can search for a travel destination(city) in the search bar so that I can view full details of the weather for that corresponding travel destination. | Yes |
| Administration Access | | |
| 1 | As a site admin, I can create, read, update and delete travel reviews posted on my website so that I can manage and filter out undesirable travel review content. | Yes |
| 2 | As a site admin, I can create, read, update and delete comments posted on travel reviews so that I can manage and filter out undesirable comments. | Yes |

*This user story has been updated during development of the project. The comments section of the blog does not allow you to put your full name but automatically inputs your username, allowing other users to view who is commenting.

### Integration Testing

The integration testing method via test cases was used when developing code for a specific feature of the project. This helped with finding errors and defects early during development to minimise problems with functionality of the website. The test cases were separated into different sections via ID's.

#### Navigation Header

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Select company name & logo | Redirect to Home Page |
| 2 | Select Home link | Redirect to Home Page |
| 3 | Select Expeditions link | Navigate to expeditions review list page where different user-posted reviews are present |
| 4 | Select Weather link | Navigate to weather app |
| 5 | Select Register | Navigate to register page where a register form is present |
| 6 | Select Sign In | Navigate to sign in page where a sign in form is present |
| 7 | If a user is signed in, select Add Review link | Navigate to the add review page where user can access add review form | 
| 8 | If a user is signed in, select Logout link | Navigate to sign out page where user is faced with an option to sign out or go back | 

#### Footer 

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Select Facebook icon | Navigate to Facebook website |
| 2 | Select Twitter icon | Navigate to Twitter website |
| 3 | Select Instagram icon | Navigate to Instagram website |
| 4 | Select LinkedIn icon | Navigate to LinkedIn website |
| 5 | Select GitHub icon | Navigate to GitHub website |
| 6 | Hover over social media icons | Icons change colour | 

#### Home Page 

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Select 'Take a look at some expeditions' button | Navigate to expeditions review list page |

#### Expeditions Review List Page

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Select any expedition review card | Navigate to the review detail page of that expedition |
| 2 | Select Next page | Navigate to second page of expedition reviews |
| 3 | Select Previous/First page | Navigate to previous/first page |

#### Expeditions Review Detail Page

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Select 'Back to Expeditons' button | Redirect to expeditions review list page |
| 2 | Select 'sign in' & 'login' hyperlinks | Navigate to sign in page |
| 3 | If user is signed in, select heart icon | Like the review |
| 4 | If user is on their posted review, select 'Edit Review' button | Navigate to edit review form |
| 5 | If user is on their posted review, select 'Delete Review' button | Navigate to delete review page |

#### Edit & Delete Review Pages

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | On edit review page, select 'Edit Review' button after completing fields | User review is updated |
| 2 | On delete review page, select 'Delete Review' button | User review is deleted from expeditions list |

#### Register & Sign In Pages

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | On register page, complete registration form and select 'Register' | Account created & redirect to home page |
| 2 | On sign in page, complete sign in form and select 'Log In' | Signed in account & redirect to home page | 

#### Add Review Page

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Complete fields as required and select 'Add Review' button | Review posted to expeditions list page |
| 2 | Select 'choose file' to upload image | Image uploaded |
| 3 | Click on star ratings from 1 to 5 | Ratings saved after adding review |

#### Logout Page

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Select 'Sign Out' button | Logged out of account & redirected to expeditions list page |
| 2 | Select 'Cancel' button | Redirected to expeditions list page |

#### Weather Page

| **Test Case ID** | **Description** | **Expected Outcome** |
| ----- | ----- | ----- |
| 1 | Enter city name with and without spaces in search bar & select 'Search' button | Weather card containing details of searched appears |

## Validation Testing

### HTML Validation

To validate the templates written in HTML for this project, I had to copy the code rendered on Google Chrome's page source option and paste it into the validator. This is because Django templates contain Jinja syntax in them which means it is not possible to directly copy the code from the templates. Any following screenshots are of HTML templates validated via [Nu HTML Checker](https://validator.w3.org/nu/), which contained any errors/warnings.

![All Pages HTML Check](/media/testing/htmlcheck-ss.png)

After running the HTML code of all templates of this project, there were no errors found within the actual code. However the validator presented with four warnings. These warnings are related to the type attribute located in the four script tags which are optional to include.

### CSS Validation

My custom CSS stylesheet was validated using [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The report returned with no errors. The warnings found are related to custom vendor prefixes. 

![CSS Validator Check](/media/testing/csscheck-ss.png)

### JavaScript Validation

Both custom JavaScript files were validated using [JS Hint](https://jshint.com/). Both reports returned with no errors. 

![JS Hint check one](/media/testing/jscheckone-ss.png)

![JS Hint check two](/media/testing/jschecktwo-ss.png)

### Python Validation

All Python code developed in this project was validated using [PEP8 Online Check](http://pep8online.com/). Screenshots of all validation reports are listed below:

  - Epic Expeditions Folder
    - [asgi.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/asgi-ss.png)
    - [settings.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/settings-ss.png)
    - [urls.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/urls-ss.png)
    - [wsgi.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/wsgi-ss.png)
  - Errors App
    - [apps.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/errorapps-ss.png)
    - [views.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/errorviews-ss.png)
  - Home App
    - [apps.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/homeapps-ss.png)
    - [urls.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/homeapps-ss.png)
    - [views.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/homeviews-ss.png)
  - Reviews App
    - [admin.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/reviewadmin-ss.png)
    - [apps.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/reviewapps-ss.png)
    - [forms.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/reviewforms-ss.png)
    - [models.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/reviewmodels-ss.png)
    - [urls.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/reviewurls-ss.png)
    - [views.py](https://github.com/legenduzair/epic-expeditions/tree/main/media/testing/reviewviews-ss.png)

## Accessibility Testing

### Lighthouse Evaluation

### WAVE Evaluation

## Bugs and Fixes
