from flask import Flask
from datetime import datetime
#import db
import sys
print(sys.version)

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <p>User {user}.</p>
    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time, user=sys.version)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)