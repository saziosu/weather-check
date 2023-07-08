# PROJECT-NAME | Testing

Weather Check is a python app for checking current, past and weather forecast.
This project utilises the OpenWeather API for accurate weather readings from your chosen city.

![Project Overview Image](readme-images/overview.png)

Link for the finished deployed site: [Weather Check](https://weather-check-e66ed6c3dc9b.herokuapp.com/)

# Table of Contents

* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
    * [User Testing](#user-testing)
        * [First Time User](#first-time-user)
        * [Returning User](#returning-user)
        * [Frequent User](#frequent-user)
* [Full Testing](#full-testing)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Fixed Bugs](#fixed-bugs)

# Automated Testing

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to test the python code.

Initially the result was the following:

![Pep8 before](readme-images/pep8-before.png)

Updated the code to resolve these errors and it passed through the linter with no further errors found:

![pep8 after](readme-images/pep8-after.png)

# Manual Testing

## User Testing

| Goal                                                                                                           | Achieved                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a user, I want to immediately understand what the purpose of the program is and easily navigate through it. | A welcome message displays on the initial run of the program, which explains the purpose of the program and the data it can provide, such as current, past and forecasted weather. |
| As a user, I want to receive clear feedback from my interactions with the program.                             | When the user inputs their data, the program gives feedback to the user confirming their choice or providing an error if the input is invalid.                                     |
| As a user, I want to be given the opportunity to correct my input if an error occurs.                          | If an error occurs on user input, the user is asked to try again and provided with the input again.                                                                                |
| As a user, I want to be able to navigate all options of the app without having to re-run the program.          | After each option is run, e.g. the current weather, all options are displayed again so that the user can see the other data for their selected city.                               |
| As a user, I want to be able to enter a new city into the program to check the a different location easily.    | After each option is run, the user has the option to enter a new city into the program to check the data for a different area.                                                     |

# Full Testing

A range of devices were used to test the site.

* OnePlus 7T Pro (Firefox, chrome, opera)
* MAC: MacBook Pro 14-inch 2021 (Mac OS Ventura 13.4) (Chrome, Safari, Firefox)
* LENOVO Tab P11 11.5" Tablet (Chrome, Firefox)

[Browserstack](https://www.browserstack.com/) was also used to test on the following devices:

* iPhone 14 (Chrome, Safari)
* iPhone 12 mini (Chrome, Safari)
* Samsung s23 (Chrome, Firefox)
* iPad 10th (Chrome, Safari)

MANUAL TESTING DETAILS

# Bugs

## Known Bugs

KNOWN BUGS TABLE

## Fixed bugs

FIXED BUGS TABLE