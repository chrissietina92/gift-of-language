📦<b>Gift Of Language - CFG degree project</b>

Group 5: Daniella Omokore, Xhensjola Hysa, Rebecca Ayaji, Christina O'Brien, Najat Yusuf

ℹ️<b>Overview</b>:

Communication is an important life skill; it enables people to express how they feel, understand the world around them and build connections with others. One of the biggest barriers to communication is understanding language.

For our group project, we created an application called the Gift of Language (GOL). The GOL app is targeted towards those wishing to improve their vocabulary and build their existing knowledge of English and encourage users to use learnt words in the real world. This app can also build life skills such as communication and public speaking as users will gain confidence in the language. 

Having a rich and varied vocabulary can make it easier for you to express yourself or explain concepts both verbally and in writing. Developing your vocabulary can be challenging, especially when it not your native language. The aim of the app is to be a supplementary resource for the learning of the english language by helping them build and grow on their existing english vocabulary. Ultimately, GOL is aiming to support those who are new to the language with a personalised and intimate way of learning English. We would like to improve the quality of communication between English speakers, through the understanding of the core language and the cultural context of the language used. 

The app hopes to achieve this by providing a unique word each day for the user to learn. Along with the word, the app will also provide a definition, how to read/say the word phonetically and an example of the word being used in a sentence. Users can opt in to be notified about the word of the day. They can also search through previously learnt words. The Gift Of Language app is a member only app, this means that users will have to sign up and then log in to the app each time they want to use it. This is so that users progress and data can be stored and accessed in the future.  The words the app will use will come from a dictionary API ([https://dictionaryapi.dev](https://dictionaryapi.dev/)). The app will have one database with two tables; one that stores user information and the other that stores searched words.



<b>✍️Authors</b>:

<i>Github:</i>
* https://github.com/daniellaomokore
* https://github.com/chrissietina92
* https://github.com/Xhensjola
* https://github.com/Becky-AJ
* https://github.com/najatyusuf



🚀<b>Usage</b>:

![GOL web page](https://user-images.githubusercontent.com/85261489/199945098-a2b325dd-b795-4692-bd71-a7f971cf3cad.png)
<i>The first page of the Flask web app, here the user can either choose to either log in or sign up.</i>

![GOL word of the day page](https://user-images.githubusercontent.com/85261489/199945131-4f75bc31-f914-412c-b096-7ff3702fc168.png)
<i>This page is the “word of the day” page. Here the user can click on the  “new word” button and it will print a randomly selected word and definition onto the page.</i>

⬇️<b>Installation:</b>

<i>Before running the app, you must</i>:
* run the SQL file in MYSQL in order to USE our created database
* ensure your computer has installed all the python packages we use in our project, these are as follows:
                          * requests
                          * mysql.connector
                          * flask
                          * schedule
                          * time
                          * itertools
                          * re
                          * random
                          
                        
* have your config file with USER, PASSWORD and HOST details


✨<b>How to Run:</b>

<i>The gift of Language app can either be run through the python console OR using an API we have created:</i>

* If the user choses to run the app through the python console on Pycharm, they can do this by running the main.py file.
* If they would like to run the app through the FLASK web app (, they can do this by running the GOL_api.py) and then clicking this link: http://127.0.0.1:5001

🌟<b>Features of Gift Of Language</b>

<i>Before using the application, users must create a new account or log in with their account. The Gift of Language members can then experience these features: </i>

* daily word of the day
* search words and its definition
* display previous learnt words
* streaks

