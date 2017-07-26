import pyrebase

config = {
	 "apiKey": "AIzaSyC9vpBfsZbCtsIMvvimJy1n3FMfmc90N4s",
    "authDomain": "rpoint-22019.firebaseapp.com",
    "databaseURL": "https://rpoint-22019.firebaseio.com",
    "projectId": "rpoint-22019",
    "storageBucket": "rpoint-22019.appspot.com",
    "messagingSenderId": "425524786368"
    }

firebase = pyrebase.initialize_app(config)

database = firebase.database()
auth = firebase.auth()
auth.sign_in_with_email_and_password("georgesarji@gmail.com", "Georgeis1")

count=database.child("Tests").child("Count").get().val()
Tests=database.child("Tests").get().val()
print (Tests["1"])