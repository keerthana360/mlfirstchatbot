# mlfirstchatbot
## Team members:<br />
  #### 1. sadhik<br />
         1a. git username - sadhik03052000
         1b. reg number - 19pa1a05c7
  #### 2. Keerthana<br />
         2a. git username - Keerthana360
         2b. reg number - 19pa1a12a9
## Packages involved:<br />
 * **pip install --upgrade pip**
 * **pip install beautifulsoup4**
 * **pip install google**
## Modules imported:<br />
 * **Random module**
 * **webbrowser module**
## Objective Of The Bot:<br />
Name of the bot is **PharmaBot**.It helps user **to know the details(uses,side effects,dosage,etc..,) of any medicine that he gives to the bot**.<br />
## Working Of The Bot:
* The programme script of chatbot contains **5** user defined functions namely-<br />
              **1.** greet()<br />
              **2.** welcome(name)<br />
              **3.** menu()<br />
              **4.** details_medicine()<br />
              **5.** pharmabot()<br />
 * whenever the pharmabot() is called the following steps will be perfromed respectively...<br />
              **1.** when the bot call **pharmabot() it calls greet() to greet the user with random greeting stored in the greetings list.**<br />
              **2.** After greeting it **asks the name of user** and stores it in name variable.<br />
              **3.** It **welcomes the user** with his name by calling **welcome(name).**<br />
              **4.** It calls **menu()** to show it's services list to the user.<br />
              **5.** In menu() it asks the user to enter the choice.<br />
              **6.** According to the choice entered by the user the further action takes place.<br />
              **7.** If **choice is 1** it will call **detail_medicine()** and takes us to the website containing info about medicine and again calls **menu() till the condition becomes false.**<br />
              8. If **choice is not 1 0r 2** it *asks to enter choice among 1 and 2* and calls **menu() till the condition becomes false.**<br />
              9. If **choice is 2** it ends the interaction and **says byee.<br />
## Diagramatic Representation:
![IMG_20201019_031142](https://user-images.githubusercontent.com/54762331/96386950-6de24000-11bc-11eb-8ae8-23f05befae26.jpg)
![IMG_20201019_031208](https://user-images.githubusercontent.com/54762331/96386972-9f5b0b80-11bc-11eb-800e-5a5b1a4b01dd.jpg)
## Youtube link:
[![pharma chatbot](https://img.youtube.com/vi/TwhDaEFspNo/0.jpg)](https://www.youtube.com/watch?v=TwhDaEFspNo)
## Resources:
[Beautifulsoup Link](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)
[pypi Link](https://pypi.org/project/google/)
