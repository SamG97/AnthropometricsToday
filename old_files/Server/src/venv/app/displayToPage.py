from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    with open("fakeResults.txt", "r") as f: #replace with actual file
        content = [line.strip() for line in f]
    data = {'ocular_width': content[0], 'face_width':content[1], 'profile_width':content[2]}
    return render_template('index.html', title='Results', data=data) #replace
                                        #X.html with actual template for card
