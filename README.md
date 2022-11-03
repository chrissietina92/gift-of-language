# gift-of-language
<b><u>CFG degree project</u></b>

<b>Background</b>:

Having a rich and varied vocabulary  can make it easier for you to express yourself or explain concepts both verbally and in writing. Developing your vocabulary can be challenging, especially when it is not your native language. The aim of the app is to be a supplementary resource for the learning of the english language by helping them build and grow on their existing english vocabulary. The app hopes to achieve this by providing a unique word each day for the user to learn. Along with the word, the app will also provide a definition, how to read/say the word phonetically and an example of the word being used in a sentence. Users can opt in to be notified about the word of the day. They can also search through previously learnt words. The Gift Of Language app is a member only app, this means that users will have to sign up and then log in to the app each time they want to use it. This is so that users progress and data can be stored and accessed in the future.  The words the app will use will come from a dictionary API ([https://dictionaryapi.dev](https://dictionaryapi.dev/)). The app will have one database with two tables; one that stores user information and the other that stores searched words.

<b>How the Gift of Language app works:</b>

<i>Before running the app, you must</i>:
- run the SQL file in MYSQL in order to USE our created database
- ensure your computer has installed all the python packages we use in our project, these are as follows:
                          - requests
                          - mysql.connector
                          - flask
                          - schedule
- have your config file with USER, PASSWORD and HOST details

<i>The gift of Language app can either be run through the python console OR using an API we have created</i>:
- If the user choses to run the app through the python console on Pycharm, they can do this by running the main.py file.
- If they would like to run the app through the FLASK web, they can do this by running the GOL_api.py file.
