# Workout Buddy
An app to help motivate **women and afab non-binary individuals** to keep fit and healthy as well as to find like-minded
friends who are willing to help achieve that goal.

## Summary
This application allows users to sign-up, match and message other users on the app in a *BumbleBFF* style of matching system to help users find new people to interact with. The main aim of our web application is to make fitness more accessible regardless of your current fitness level or experience. Drawing on our own experiences, we wanted to include motivational quotes, randomly generated exercises and healthy smoothie recipes to everyone who visits the site. Then for the signed in user, we wanted to include a way to find and match with other users and send and recieve messages to motivate and inspire.

## Installation Guide

**Open the terminal and install the following python packages:**
- **`pip install flask`**
- **`pip install flask_login`**
- **`pip install mysql-connector-python`**
- **`pip install requests`**
- **`pip install bcrypt`**

The workout buddy database has seperate folders for all sections to include:

 - api - for the smoothie and workout api connections.

 - database - this directory includes the connection, match-ups, messages, quotes, sample_data for sql testing and sql schema for the main database and the users file.

 - static - includes bootsrap file and home page images.

 - templates - html files for about, base, buddies, disclaimer, home, login, messages, profile, publicprofile, signup, smoothies and workouts.

 - tests - users, workout and smoothies test files.

 - utils - app and config files - The edamam api app_ids and app_keys are also included in the config.py file. Or user can sign up at https://developer.edamam.com/edamam-recipe-api and create their own app_id and app_key to work with the app- remember to update the config file.

## SQL Database setup

database.schema.sql should be run in SQL to create the database and tables required.

database.sample_data,sql can also be used to create test users, but is not essential and can be ignored.

utils.config.py - user will have to make sure their chosen SQL database user id and password matches the id and password in this file, or change the config page to match their user information.

 - Once all steps above are followed, run **`utils.app.py`** from your python IDE and click on the link that appears in the terminal.

## Documentation

Wger api documentation: https://wger.de/en/software/api

Edamam api documentation: https://developer.edamam.com/edamam-docs-recipe-api

## Navigation in App

Navigation within the app is via the top menu bar. The app is scaleable, so when the width is compressed, the menu condenses into a CSS hamburger menu at the top right. The main Workout Buddy icon at the top left always returns the user to the home page. 

The aim is to give any person access to the home page, the about page, the workout ideas/exercises and Smoothie Recipes page using the respective api connections. We also created a SQL database to have motivational quotes randomly generated on every page visited. The user can also select to join Workout Buddy, or try to find a match, which will automatically bring them to the sign in page, with a join up option.

Home Page:

![image](https://user-images.githubusercontent.com/104861528/200134768-74868116-8c04-4ff8-9426-bd029e0121c7.png)

Sign-up Page:

![image](https://user-images.githubusercontent.com/104861528/200134774-af063b6b-c342-4da6-a565-360cad8e41b6.png)

Disclaimer Page:

![image](https://user-images.githubusercontent.com/104861528/200134794-aebed5c6-83b3-4732-b5fe-a9e59af4c419.png)

About Us Page:

![image](https://user-images.githubusercontent.com/104861528/200134808-2ac85ba8-c766-440e-b437-99839b8c0f8f.png)

Workout Page:

![image](https://user-images.githubusercontent.com/104861528/200134820-3f19761e-945c-4269-9dab-515e22ab48fa.png)

Smoothie Page:

![image](https://user-images.githubusercontent.com/104861528/200134833-8c552d2a-312c-41b3-b42a-c24cae354c2b.png)

Log-in Page:

![image](https://user-images.githubusercontent.com/104861528/200134849-f13348d9-4762-47ae-8fc5-6edbea713f0c.png)

Once the user has joined and signed in, they then have access to the restricted users only pages. These pages include the Find a Buddy matching page, where they can get a random match with a fellow user, check the matched users public profile page and send them a message if they want to connect. The users only section also has a personal profile page for the user to update their profile information, a messages page where the user can check past messages and send new ones and a sign out page.

Private Profile Page:

![image](https://user-images.githubusercontent.com/104861528/200134867-2043d305-3f0d-45c1-91f2-f0851b713cc1.png)

Find a Buddy Page:

![image](https://user-images.githubusercontent.com/104861528/200134879-4b3f7f9c-5fd0-424b-8fdc-00403581f79c.png)

Public Profile Page from Match:

![image](https://user-images.githubusercontent.com/104861528/200134896-f47e6ea7-d294-4c86-9ecf-d3d26b84182e.png)

Send a Message to New Match:

![image](https://user-images.githubusercontent.com/104861528/200134923-d87958c8-66b9-4caa-a222-edc52ad95f4e.png)

Messages Page:

![image](https://user-images.githubusercontent.com/104861528/200137470-dfe633f3-8929-4224-b5b3-cacd53dc89a9.png)

Home Page Showing Scalability with CSS Hamburger Menu tab:

![image](https://user-images.githubusercontent.com/104861528/200140739-fd0ec34d-d53b-4ba3-abb2-0c238cbca21f.png)

CSS Hamberger Menu Tab Expanded:

![image](https://user-images.githubusercontent.com/104861528/200140774-181ec72b-7504-427d-a3f6-be851a0ceb51.png)
