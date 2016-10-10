# Welcome

In this test you'll be building a very basic, very simple, twitter clone.

The basic functionality is outlined below, the focus is mostly on the python/django code and not so much about user friendliness. So feel free to use basic html form submits for the mandatory requirements, refresh the pages after actions etc.

This test should not take longer than 20-30 minutes to complete using libraries already provided - you are however free to use any additional libraries as you see fit.

The project already comes with all the html templates in place, you will need to update them in few places. The view classes and URLs are set up, you can change these if you think it's necessary.

The optional tasks list is, as the name says, optional - you can chose not to do any of the tasks, or you can pick some of them. Generally speaking, specification and frontend/backend code do not exist for any of the items there - you are free to implement them any way you want to.

Good luck!

If you have any feedback and/or questions regarding this test feel free to email me at: david.suilea@3megawatt.com

# Getting Started

First fork the repository from Github, clone it, and switch to the new directory:

    $ git clone https://github.com/USERNAME/testapp_django.git
    $ cd testapp_django
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server which will give you more details:

    $ python manage.py runserver


# Task Requirements


## Registration

The registration should be handled in the `users` app `RegisterView` class. 
The whole process should be simple (no email confirmations etc) and should use the built-in auth system.

Template `/users/templates/users/register.html` exists with all the functionality that's required from the frontend side, it only needs coresponding form.

`GET` should return the registration page if the user is not already logged in, otherwise redirect to `home`.

`POST` should create a new user, and save it in the databse, if the form is valid. Otherwise it should render the errors on the page. Once the registration is done redirect to the `home` view.

## Logging in

Logging in should be done in the `users` app `LoginView` class. Template with all the functionality from the frontend is written in `/users/templates/users/login.html`

`GET` should return the login page if the user is not logged in, otherwise it should redirect to `home`

`POST` should accept the form parameters either from the homepage (top right) or the login page, if the user credentials are valid it should redirect to `home`

## Logging out

Logging out should be done via `POST` request to the `users` app `LogoutView` class. The form submit will be called from the `/templates/_items/navbar.html` template.

Log out the user and redirect to the `home` view if the user is already logged in, otherwise redirec to the `login` page.

## (Un)following users / Profile view

Every username in the timeline view on the home page is hyperlink to the profile at the url `http://localhost:8000/profile/<ID>` where ID is same as user `pk` in the database.

Visit the url `http://localhost:8000/profile/1/` before changing the templates to see how it should look like. Show the last 10 tweets from the user, and have one button where the currently logged in user can either follow or unfollow the user profile. 

The `POST` request is already made by the frontend. Feel free to change this if you want a different approach. After unfollowing the user is redirected back to the same page.

## (Logged in) Homepage view

The homepage should be just a list of latest 15 tweets from the users the currently logged in user is following. If the user is not following anybody, he should see the latest tweets posted by any user. 

For an example of how the page should look like visit `http://localhost:8000/?example=true`. The times should be humanized, and the usernames should link to their profile pages, same as above.

## (Logged out) Homepage view

If the user is not logged in then he sees the last 10 tweets posted by any user. The form for posting new tweets is hidden.

## Posting new tweets

Logged in users should be able to post new tweets by simply filling in the text area and clicking "Post" button. This should make a simple HTML form post to the backend, which should then refresh the page by redirecting the user back to the home page. Users can see their own tweets. 

## Sample data

Create a few accounts and tweets for testing purposes. Preferably use django fixtures.

# Optional tasks

* Ajax requests instead of HTML form POSTs

* Editing existing tweets

* Profile bio and edit page

* Gravatar user icons

* markdown support for messages
