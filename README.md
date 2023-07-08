# Weather Check
Weather Check is a python app for checking current, past and weather forecast.
This project utilises the OpenWeather API for accurate weather readings from your chosen city.

[image here]

Link for the finished deployed site: [Weather Check](https://weather-check-e66ed6c3dc9b.herokuapp.com/)

# Table of Contents

* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
* [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
    * [Accessibility](#accessibility)
* [Technology Used](#technology-used)
    * [Languages](#languages)
    * [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
* [Deployment](#deployment)
* [Testing](#testing)
* [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

# User Experience

The aim of this project is to provide the user with accurate weather information based on the user's selection of the city.
It provides information on current, past and forecasted weather.

## User Stories

* As a first time User, we want to understand immediately what information is required from us to run the app effectively.
  
* As a returning User, we want to be able to input a new city to check the weather for any location we wish to see weather information for.

## Planning

[Miro](https://miro.com/) was used for planning the project

![Miro flowchart image 1](readme-images/miro.png)
![Miro flowchart image 2](readme-images/miro-2.png)

## Colors

[Termcolor](https://pypi.org/project/termcolor/) was used to introduce colors into the terminal project to add better readability.

* Green was used for informational messages, such as the welcome message and date requirements or past weather
* Yellow was used on text confirming the date.
* Red was used on errors and weather alert warnings to promote a sense of urgency.

# Features 

## Current Features

### Welcome Message

![welcome message](readme-images/welcome-message.png)

The welcome message uses ascii art to personalise the app.
It uses a title and an umbrella ascii image.
The welcome message allows the user to understand the purpose of the app, and asks them to enter their city.
If an invalid city is added, the user is asked to enter a valid city.

### App options

![city confirmation](readme-images/weather-options.png)

The app will confirm the user's city and print the corresponding country code. 
This gives the user confirmation that the app is checking the correct city.
The app then provides four options; current weather, forecasted weather, past weather and enter a new city.
The options also give a key on how to select them.
After each selection is chosen, the user will see the options again to choose a new request or start the process with a new city.

### Current Weather

![current weather image](readme-images/current-weather.png)

The current weather is selected by entering 1 into the options.
This provides current weather information to the user, including sunrise and sunset times based on the city's local time.

### Weather Forecast

![weather forecast](readme-images/weather-forecast.png)

The weather forecast is selected by entering 2 into the options.
The user is then asked to enter how many days in the future they would like to see the forecast for.
The app will then confirm the date that it is showing the forecast for.
If there is a weather alert, this will display on this page:

![weather alert](readme-images/weather-alert.png)

### Past Weather

![Past weather](readme-images/past-weather.png)

The past weather is selected by entering 3 into the options.
The user is then asked to enter the date they would like to check the weather for.
The user can choose a date from 01/01/1979.
The date must be the format of DD/MM/YYYY, if the user enters an incorrect format or date and error will be shown.

### New City

![New City](readme-images/new-city.png)

A new city can be checked by entering 4 into the options.
The app will confirm that the service is restarting and they are asked to enter a new city to run through the app.

## Future Features

* A few
* Future
* Features

## Accessibility

* Accessibility
* Considerations
* Here

# Technology Used

## Languages

* Python

## Frameworks, Libraries & Programs 

* [Python Requests](https://pypi.org/project/requests/)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)
* [Python Termcolor](https://pypi.org/project/termcolor/)

# Deployment & Development

## Forking the Repository

1. Log in or Sign up to [GitHub](https://github.com/)
2. Navigate to https://github.com/saziosu/weather-check.
3. Click the 'fork' button in the top right corner.
4. Feel free to customize your repo name, this is not required.
5. Click the Create Fork button.

## Deploy to Heroku
Heroku was used to deploy this site:

1. Login (or signup) to Heroku with GitHub
2. Navigate to the [apps page](https://dashboard.heroku.com/apps)
3. Click the 'new' button in the top right corner and create new app.
4. Choose an app name and select your region.
4. Navigate to the settings page for the app.
5. Under Buildpacks add NodeJS and Python
6. Reveal config vars and add your API key credentials
7. Navigate to the deploys section of the app.
8. Select deploy with github and connect the appropriate repo.
9. Click deploy, or select automatic deployment.

# Testing

[TESTING.md](TESTING.md)

# Credits

## Code

* [NeuralNine](https://www.youtube.com/watch?v=9P5MY_2i7K8), I used this tutorial to help me with starting up and utilising the OpenWeather API.
* [GeeksForGeeks](https://www.geeksforgeeks.org/convert-date-string-to-timestamp-in-python/), I used this resource to help convert date strings into timestamps to use in the API calls
* [Programiz](https://www.programiz.com/python-programming/datetime/timestamp-datetime), also used this resource to help convert dates into timestamps.
* [StackOverflow](https://stackoverflow.com/questions/69757549/how-do-i-make-a-function-execute-when-a-certain-key-is-pressed), used this resource to help the user select which function they want to run.

## Media

* Media
* Credits
* Here

# Acknowledgements

* Thanks y'all!