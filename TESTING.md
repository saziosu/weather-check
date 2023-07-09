# Weather Check | Testing

Weather Check is a python app for checking current, past and weather forecast.
This project utilises the OpenWeather API for accurate weather readings from your chosen city.

![Project Overview Image](readme-images/overview.png)

Link for the finished deployed site: [Weather Check](https://weather-check-e66ed6c3dc9b.herokuapp.com/)

# Table of Contents

* [Testing Tools](#testing-tools)
* [Manual Testing](#manual-testing)
    * [User Testing](#user-testing)
    * [Full Testing](#full-testing)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Fixed Bugs](#fixed-bugs)

# Testing Tools

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to test the python code.

Initially the result was the following:

![Pep8 before](readme-images/pep8-before.png)

Updated the code to resolve these errors and it passed through the linter with no further errors found:

![pep8 after](readme-images/pep8-after.png)

# Manual Testing

## User Testing

| **Goal**                                                                                                       | **Achieved**                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a user, I want to immediately understand what the purpose of the program is and easily navigate through it. | A welcome message displays on the initial run of the program, which explains the purpose of the program and the data it can provide, such as current, past and forecasted weather. |
| As a user, I want to receive clear feedback from my interactions with the program.                             | When the user inputs their data, the program gives feedback to the user confirming their choice or providing an error if the input is invalid.                                     |
| As a user, I want to be given the opportunity to correct my input if an error occurs.                          | If an error occurs on user input, the user is asked to try again and provided with the input again.                                                                                |
| As a user, I want to be able to navigate all options of the app without having to re-run the program.          | After each option is run, e.g. the current weather, all options are displayed again so that the user can see the other data for their selected city.                               |
| As a user, I want to be able to enter a new city into the program to check the a different location easily.    | After each option is run, the user has the option to enter a new city into the program to check the data for a different area.                                                     |

## Full Testing

| **Feature**      | **Outcome**                           | **Example**          | **Pass/Fail** |
|------------------|---------------------------------------|----------------------|---------------|
| Welcome Message  | Validate user input                   | ![invalid city input](readme-images/invalid-city.png)   | Pass          |
| Welcome Message  | Confirm Country code to user          | ![valid city input](readme-images/valid-city.png)     | Pass          |
| Navgation        | Validate user input                   | ![invalid navigation](readme-images/invalid_select.png)    | Pass          |
| Navigation       | Show navigation after each selection  | ![Navigation displayed](readme-images/navigation-after-run.png)            | Pass          |
| Current Weather  | Output weather data from API          | ![Current Weather](readme-images/current-weather-test.png)      | Pass          |
| Weather Forecast | Validate user input                   | ![Forecast validation](readme-images/invalid-forecast.png)     | Pass          |
| Weather Forecast | Confirm date selected to user         | ![Confirm forecast date](readme-images/valid-forecast.png)       | Pass          |
| Weather Forecast | Provide forecasted weather to the user for the selected date       | ![weather forecast test](readme-images/weather-forecast-test.png) |  Pass          |
| Weather Forecast | Provide weather alert for the week to the user       | ![Weather alert image](readme-images/weather-alert-test.png) |  Pass          |
| Past Weather     | Validate User Input                   | ![Past weather validation](readme-images/invalid-date.png) | Pass          |
| Past Weather | Provide past weather to the user for the selected date       | ![Past weather testing](readme-images/past-weather-test.png) |  Pass          |
| New City         | Allow user to enter new city          | ![New city input](readme-images/new-input.png)             | Pass          |

# Bugs

## Known Bugs

To my knowledge there are no further bugs remaining on the program.

## Fixed bugs

| **Bug Presented**                                                                                 | **Fix**                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| City validation was continuing to lead to errors through the rest of the functions                | Added a while loop with a try & except to catch these errors before moving to the next function.                                                                                                                                                          |
| In the weather_forecast function, the function would error out if there was not rain on that day. | The API only provided rain data if rain was forecasted for that day, added an if statement to only print the rain variable if rain was expected on the chosen date.                                                                                       |
| Long lines                                                                                        | Some long string lines were giving issues with shortening them. Used a format string to resolve these line errors.                                                                                                                                        |
| The city confirmation message was being printed twice after entering the city.                    | The function was being run twice, once via `city_check(city)` and a second time when converting the return tuple into separate variables. I removed the first run and moved the return conversion into its place `latitude, longitude = city_check(city)` |


[Top](#weather-check--testing)