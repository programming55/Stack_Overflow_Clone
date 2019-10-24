# Stack Overflow Clone

This project aims to create a question answer-portal like Stack Overflow. Registered users get the ability to ask and answer questions. The feature to upvote and downvote both questions and answers as well as add comments has also been provided. The project was deployed using Flask (Python). Each registered user has an associated user profile where one may add profile picture, a short bio, etc. Handling of various error routes (404 error, 403 error, etc.) has also been done. Major design aspects of the webiste have been also been made from scratch (without using pre-existing templates).

A brief description of the files and directories in the repository is as follows:
- **app:** This directory contains the app built on the Flask backend. The typical MVC (Model View Controller) architecture has been followed. The databse file is also stored here. A relational database was used for the project.
- **cert.pem & key.pem:** These are files that are used to enable https communication (self-signed ceftificates).
- **main.py** Contains the code to initialize and run the app.
