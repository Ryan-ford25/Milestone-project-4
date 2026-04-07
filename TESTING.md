# Testing

![MathRise](assets/documentation/am-i-responsive.png)

Visit the deployed site here: [MathRise](https://mathrise-bd6d69167130.herokuapp.com/)

> [!NOTE]  
> Return back to the [README.md](README.md) file.

This document outlines the testing processes and results for the **MathRise** web application. It ensures that all features function as expected, meet accessibility standards, and provide an optimal user experience.

---

<a id=contents></a>

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [Code Validation](#code-validation)
  - [HTML Validation Results](#html)
  - [CSS Validation Results](#css)
  - [JavaScript Validation Results](#javascript)
  - [Python Validation Results](#python)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Full Testing](#full-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness](#responsiveness)
  - [Defensive Programming](#defensive-programming)
  - [User Story Testing](#user-story-testing)
  - [Bugs](#bugs)

<br>
<hr>

Testing was an **integral part of the development process**, ensuring the website remained both **functional and user-friendly** at every stage. By conducting **continuous testing**, potential issues were identified early, allowing for swift resolution and a more efficient workflow.

**Chrome Developer Tools** played a crucial role throughout development, providing real-time insights into performance, responsiveness, and debugging. This proactive approach helped streamline development and ensure the final product adhered to high-quality standards.

Additionally, **ChatGPT** served as a key resource for refining ideas, optimizing content, and overcoming technical challenges. By offering structured guidance, best practices, and alternative solutions, it contributed to improving both the efficiency of development and the overall quality of the final product.

To guarantee **cross-device compatibility**, every screen was rigorously tested across various **screen sizes and devices** using Chrome Developer Tools. This process ensured that MathRise was fully responsive, providing a seamless user experience across **desktops, tablets, and mobile devices**.

---

## Testing Overview

Testing was conducted using a combination of automated tools and manual testing to ensure functionality, responsiveness, accessibility, and overall user experience across all devices.

---

<a id=automated-testing></a>

## AUTOMATED TESTING

A series of **automated testing** tools were used on the site to check the code for web standard compliance and errors. These tools ensured repeatable, scalable, and performance-driven results throughout the site’s development.

---

<a id=code-validation></a>

## Code Validation

<a id=html></a>

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Pass/Fail | Notes |
| --- | --- | --- | --- | 
| Home | <img src="assets/documentation/home_html_validator.png" width=750 alt="Html Validator Screenshot"> | Pass: Error | Initial test failed as I had placed a div element within a button element for the question cards however I then changed this to have a button at the bottom of the cards for answering the questions with updated text when answered, which then passed the HTML validation test.
| Profile | <img src="assets/documentation/profile_html_validator.png" width=750 alt="Html Validator Screenshot">  | Pass: No Errors. |
| Dashboard | <img src="assets/documentation/dashboard_html_validator.png" width=750 alt="Html Validator Screenshot"> | Pass: No Errors |
| Upgrade |  <img src="assets/documentation/upgrade_html_validator.png" width=750 alt="Html Validator Screenshot">   | Pass: No Errors |
| Sign In | <img src="assets/documentation/login_html_validator.png" width=750 alt="Html Validator Screenshot">  | Pass: No Errors |
| Sign Up | <img src="assets/documentation/signup_html_validator.png" width=750 alt="Html Validator Screenshot">  | Pass: No Errors |
| Sign Out |  <img src="assets/documentation/logout_html_validator.png" width=750 alt="Html Validator Screenshot">   | Pass: No Errors |


<a id=css></a>

---

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file. Which passed with no errors.

<img src="assets/documentation/css_validation.png" alt="CSS validator screenshot" width=750>

---
<a id=javascript></a>

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| question_modal.js | <img src="assets/documentation/jshint_validation.png" width=750 alt="JShint validation screenshot"> | Pass: No Errors or Warnings |


---

<a id=python></a>

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation For MathRise Project
| File | Screenshot | Notes |
| --- | --- | --- |
| asgi.py | <img src="assets/documentation/project_asgi_python_validator.png" alt="Asgi.py validator screenshot"> | Pass: No Errors |
| settings.py | <img src="assets/documentation/project_settings_python_validation.png" alt="Settings.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/project_url_python_validation.png" alt="Urls.py validator screenshot"> | Pass: No Errors |
| wsgi.py | <img src="assets/documentation/project_wsgi_python_validation.png" alt="Wsgi.py validator screenshot"> | Pass: No Errors |

#### Validation For User App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | <img src="assets/documentation/user_app_python_validation.png" alt="App.py validator screenshot">  | Pass: No Errors |
| forms.py | <img src="assets/documentation/user_forms_python_validation.png" alt="Forms.py validator screenshot"> | Pass: No Errors |
| models.py | <img src="assets/documentation/user_models_python_validation.png" alt="Models.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/user_urls_python_validation.png" alt="Urls.py validator screenshot">  | Pass: No Errors |
| views.py | <img src="assets/documentation/user_views_python_validation.png" alt="Views.py validator screenshot"> | Pass: No Errors |

#### Validation For Payment App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | <img src="assets/documentation/payment_app_python_validation.png" alt="App.py validator screenshot"> | Pass: No Errors |
| models.py | <img src="assets/documentation/payment_models_python_validation.png" alt="Models.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/payment_url_python_validation.png" alt="Urls.py validator screenshot"> | Pass: No Errors |
| views.py | <img src="assets/documentation/payment_views_python_validation.png" alt="Views.py validator screenshot"> | Pass: No Errors |

#### Validation For Quiz App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | <img src="assets/documentation/quiz_app_python_validation.png" alt="App.py validator screenshot"> | Pass: No Errors |
| models.py | <img src="assets/documentation/quiz_models_python_validation.png" alt="Models.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/quiz_url_python_validation.png" alt="Urls.py validator screenshot"> | Pass: No Errors |
| views.py | <img src="assets/documentation/quiz_views_python_validation.png" alt="Views.py validator screenshot"> | Pass: No Errors |

---

<a id=lighthouse></a>

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues, the tool tests the websites Performance, Accessibility, Best Practices and SEO(Search Engine Optimization). The login page had a slightly lower accessibility score (70–80) due to contrast. These were reviewed and partially improved, but minor limitations remain.

### MathRise App - Mobile Testing
| Page | Size | Screenshot | 
| --- | --- | --- | 
| Home | Mobile | <img src="assets/documentation/home_lighthouse_mobile.png" alt="Home screen Lighthouse report for Mobile"> | 
| Sign In | Mobile | <img src="assets/documentation/login_lighthouse_mobile.png" alt="Login screen Lighthouse report for Mobile"> |
| Sign Up | Mobile | <img src="assets/documentation/signup_lighthouse_mobile.png" alt="Signup screen Lighthouse report for Mobile"> |
| Logout | Mobile | <img src="assets/documentation/logout_lighthouse_mobile.png" alt="Logout screen Lighthouse report for Mobile"> |
| Dashboard | Mobile | <img src="assets/documentation/dashboard_lighthouse_mobile.png" alt="Dashboard screen Lighthouse report for Mobile"> | 
| Profile | Mobile | <img src="assets/documentation/profile_lighthouse_mobile.png" alt="Profile screen Lighthouse report for Mobile"> | 

### MathRise - Desktop Testing
| Page | Size | Screenshot | 
| --- | --- | --- | 
| Home | Desktop | <img src="assets/documentation/home_lighthouse_desktop.png" alt="Home screen Lighthouse report for Desktop"> | 
| Sign In | Desktop | <img src="assets/documentation/login_lighthouse_desktop.png" alt="Home screen Lighthouse report for Desktop"> |
| Sign Up | Desktop | <img src="assets/documentation/signup_lighthouse_desktop.png" alt="Home screen Lighthouse report for Desktop"> |
| Sign Out | Desktop | <img src="assets/documentation/logout_lighthouse_desktop.png" alt="Home screen Lighthouse report for Desktop"> |
| Dashboard | Desktop | <img src="assets/documentation/dashboard_lighthouse_desktop.png" alt="Home screen Lighthouse report for Desktop"> | 
| Profile | Desktop | <img src="assets/documentation/profile_lighthouse_desktop.png" alt="Home screen Lighthouse report for Desktop"> | 

---

<a id=manual-testing></a>

## Manual Testing

<a id=full-testing></a>

### Full Testing

This section outlines the **manual testing** process conducted to ensure the website functions correctly across different devices, screen sizes, and user interactions. Each test was performed methodically to identify potential issues with responsiveness, usability, and accessibility, with results documented for further improvements. Additional testing was carried out by friends and family on a variety of devices and screen sizes.

---

<a id=browser-compatibility></a>

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | <img src=""> | Works as expected |
| Firefox | <img src="">   | Works as expected |
| Edge | <img src="">   | Works as expected |
| Opera | <img src="">   | Works as expected |

---

<a id=responsiveness></a>

## Responsiveness

In addition to testing my deployed site on different devices, I thoroughly tested its responsiveness using Chrome Developer Tools.
I researched the narrowest width of modern devices on Stack Exchange and based my testing on 320px as a standard minimum width.
Additionally, I used the Mobile First Plugin, a Chrome extension designed to test site responsiveness across different devices.

---

### Home Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_home.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_home.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_home.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_home.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_home.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_home.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_home.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_home.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_home.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_home.png" height=500>    | 2048 | 1142 |


---

### Login Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_login.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_login.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_login.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_login.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_login.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_login.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_login.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_login.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_login.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_login.png" height=500>    | 2048 | 1142 |

---

### Logout Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_logout.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_logout.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_logout.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_logout.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_logout.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_logout.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_logout.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_logout.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_logout.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_logout.png" height=500>    | 2048 | 1142 |

---

### SignUp Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_register.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_register.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_register.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_register.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_register.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_register.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_register.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_register.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_register.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_register.png" height=500>    | 2048 | 1142 |

---

### Dashboard Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_dashboard.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_dashboard.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_dashboard.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_dashboard.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_dashboard.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_dashboard.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_dashboard.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_dashboard.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_dashboard.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_dashboard.png" height=500>    | 2048 | 1142 |
---

### Profile Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_profile.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_profile.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_profile.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_profile.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_profile.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_profile.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_profile.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_profile.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_profile.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_profile.png" height=500>    | 2048 | 1142 |
---

### Upgrade Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5_upgrade.png" height=500>  | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13_upgrade.png" height=500>   | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsungs20_upgrade.png" height=500>   | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus_upgrade.png" height=500>  | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini_upgrade.png" height=500>   | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab_upgrade.png" height=500>   | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro_upgrade.png" height=500>  | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbookair_upgrade.png" height=500>   | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell_upgrade.png" height=500>   | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac_upgrade.png" height=500>    | 2048 | 1142 |

---

<a id=defensive-programming></a>

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Screen Clip |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Register Link | Redirects user to Register Page | Pass | <img src="assets/documentation/register_link.gif" height=300 alt="Selecting the Register Link from Navigation bar"> |
| | Click on Login Link | Redirects user to Login Page | Pass | <img src="assets/documentation/login_link.gif" height=300 alt="Selecting the Login Link from Navigation bar"> |
| | Click on Dashboard Link | Redirects user to Dashboard Page | Pass | <img src="assets/documentation/dashboard_link.gif" height=300 alt="Selecting the Dashboard Link from Navigation bar"> |
| | Click on Profile Link | Redirects user to Profile Page | Pass | <img src="assets/documentation/profile_link.gif" height=300 alt="Selecting the Profile Link from Navigation bar"> |
| | Click on Logout Link | Redirects user to Logout Page | Pass | <img src="assets/documentation/logout_link.gif" height=300 alt="Selecting the Logout Link from Navigation bar"> |
| | Click on MathRise Link | Redirects user to Home page Page | Pass | <img src="assets/documentation/mathrise_link.gif" height=300 alt="Selecting the MathRise Link from Navigation bar"> |
| | | | | |
| Home Page | | | | |
| | Click on Solve button (logged in) | Modal pops up with the question and list of four answers | Pass | <img src="assets/documentation/loggedin_solve_button.gif" height=300 alt="Selecting the solve button whilst loggedin"> |
| | Click on Solve button (not logged in)| Modal pops up prompting user to login | Pass | <img src="assets/documentation/loggedout_solve_button.gif" height=300 alt="Selecting the solve button whilst logged out"> |
| | Click on Solve button for a premium question | If user is not a premium member, modal pops up prompting user to become a premium member | Pass | <img src="assets/documentation/premium_question.gif" height=300 alt="Selecting a premium question as a non-premium user"> |
| | Click on 'Upgrade Now'(If user is not a premium member)| Redirects user to upgrade page | Pass | <img src="assets/documentation/upgrade_button.gif" height=300 alt="Selecting 'Upgrade now' button"> |
| Dashboard | | | | |
| | Click on 'Upgrade Now'(If user is not a premium member)| Redirects user to upgrade page | Pass | <img src="assets/documentation/upgrade_dashboard.gif" height=300 alt="Selecting 'Upgrade now' button"> |
| | | | | |
| Question Modal | | | | |
| | Click on Radio button | Fills the selected radio button. Only one can be sleected at a time | Pass | <img src="assets/documentation/radio_button.gif" height=300 alt="Selecting A radio button"> |
| | Click on "Submit Answer" button | Button's text is changed to "Submitting" and button is disbaled | Pass | <img src="assets/documentation/submit_button.gif" height=300 alt="Selecting 'Submit' Button"> |
| | After Submit button is pressed | Correct answer is highlighted green and if answer chosen by the user is incorrect it is highlighted red | Pass | <img src="assets/documentation/highlighted_answers.gif" height=300 alt="Showing that answers are highlighted">|
| | After Submit button is pressed | Modal closes after 1 second and the question's button is disabled and inner text is changed to "Answered" | Pass | <img src="assets/documentation/closing_modal.gif" height=300 alt="Showing that the question modals close after one second">|
| | Click on 'X' button | Modal closes and the question can still be selected by the user | Pass | <img src="assets/documentation/exit_question.gif" height=300 alt="Selecting the 'X' button on modal"> |
| | | | | |
| Upgrade Page | | | | |
| | Click on 'Upgrade Now' button (Monthly offer) | Redirects user to stripe payment page for monthly amount | Pass | <img src="assets/documentation/monthly_plan.gif" height=300 alt="Selecting Monthly upgrade plan Button"> |
| | Click on 'Upgrade Now' button (Annual offer) | Redirects user to stripe payment page for Annual amount | Pass | <img src="assets/documentation/annual_plan.gif" height=300 alt="Selecting Annual upgrade plan Button">|
| | | | | |
| Login Page | | | | |
| | Enter valid Username | Field will only accept registered users | Pass | <img src="assets/documentation/username_login.gif" height=300 alt="Logging in with Username"> |
| | Enter valid Email | If the user chooses to use email instead field will only accept registered emails | Pass | <img src="assets/documentation/email_login.gif" height=300 alt="Logging in with Email">|
| | Enter valid password | Field will only accept password format | Pass | <img src="assets/documentation/username_login.gif" height=300 alt="Logging in with correct password"> |
| | Click on Login button | Redirects user to Home Page| Pass | <img src="assets/documentation/login_button.gif" height=300 alt="pressing Login button"> |
| | Click on Sign Up link | Redirects user to Sign Up page | Pass | <img src="assets/documentation/signup_link.gif" height=300 alt="Pressing the 'signup' link">|
| | | | | |
| Sign Up Page | | | | |
| | Enter valid Username | Field will only accept username format | Pass | <img src="assets/documentation/registering_form.gif" height=300 alt="Filling out Username field"> |
| | Enter valid password | Field will only accept password format | Pass | <img src="assets/documentation/registering_form.gif" height=300 alt="Filling out password field"> |
| | Enter valid email (twice) | Field will only accept email format | Pass | <img src="assets/documentation/registering_form.gif" height=300 alt="Filling out Email field"> |
| | Click on 'Register' button | Redirects user to Verification sent page | Pass |  <img src="assets/documentation/registering_form.gif" height=300 alt="Pressing the 'Register' button after filling out the form">| |
| | Click on Login Link | Redirects user to Log in Page | Pass |  <img src="assets/documentation/register_to_login.gif" height=300 alt="Pressing the 'login' link"> |
| | | | | |
| Log Out Page | | | | |
| | Click Logout button | Logs out user, Redirects user to Home page | Pass | <img src="assets/documentation/logout_button.gif" height=300 alt="Pressing the 'Logout' button">|


---

<a id=user-story-testing></a>

## User Story Testing

| User Stories | How were they achieved? |
| ------ | -------------------------- |
| As a registered user, I would like to log into my account so that I can access my saved progress and personalised features. |This has been achieved by adding a signup form that users can create an account with and a login page which the user can enter their new username and password into in order to access the sites features and navigation.|
| As a new user, I would like to register an account so that I can access personalised features on the platform. | This is achieved by filling out the signup form mentioned in the previous user story.|
| As a logged-in user, I would like to log out of my account so that I can keep my account secure. | A clearly labelled navigation link 'Logout' can be used to access the logout page where the user can end their session and prevent other people from accessing their account. |
| As a user, I would like to attempt maths questions so that I can practise and improve my skills. | On the home page are multiple cards with math questions on, by pressing the 'Solve' button on one of these cards the user can answer the given question using the radio buttons presented on a modal.|
| As a user, I would like to submit my answer and receive immediate feedback so that I can understand my mistakes.| The user can select the 'Submit' button on the question modal which will submit their chosen answer and give immediate feedback by changing the inner text of the button to 'Submitting..' and highlighting the correct answer green. If the user selected the wrong answer their chosen answer will be highlighted red at the same time. |
| As a user, I would like to track my progress so that I can see my improvement over time. | The dashboard has 'stat-cards' with the amount of points they have recieved today, this week and this month. Premium users are given an accuracy chart to see how many correct to incorrect answers they have given. |
| As a user, I would like to view my profile so that I can see my account details and activity. | Users can select the 'Profile' link from the navigation bar to be redirected to their profile page which displays the name and email given upon signing up to the site aswell as the subscription type they currently have ('Free' or 'Premium'). |
| As a user, I would like to have a daily question limit counter so that I know how many questions I can answer. | Although a visible counter is not yet displayed in the homepage, once free users have hit their daily limit of 5 questions a modal pops up to tell them they have no more attempts remaining today. |
| As a user, I would like to navigate between pages easily so that I can access different parts of the platform. | A Navigation bar with links to all pages is located at the top of the site. The navigation bar will changed depending on whether the user is currently signed in or not. |

<a id=bugs></a>

## Key Issues Identified & Fixes

- Invalid HTML structure (div inside button) → resolved by restructuring card layout
- Modal interaction bugs → fixed with improved event handling
- Accessibility issues on login form → improved contrast

Other than these minor issues no major bugs were found during testing.