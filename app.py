from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def cvStart():
    return render_template('homepageCV.html')


@app.route('/Contact')
def contact():
    return render_template('cvConntactPage.html')


@app.route('/About')
def about():
    return render_template('cvMor.html')


@app.route('/assignment8')
def assign():
    return render_template('assignment8.html',
                           hobbies={'Dance', 'Travel', 'Watch Movies'},
                           ComedySeries={'Brooklyn99', '70s Show', 'Friends', 'Great Country'},
                           DramaSeries={'Greys anatomy', 'Suits', 'Decker', 'Game Of Thrones'},
                           foodAndCalories={'Hamburger': "200", 'peanutButter': "400", 'Pizza': "300"}
                           )


@app.route('/tv')
def tv():
    return render_template('tv.html',
                           user={'name': "haim", 'if Work': "no", 'loveComedy': 'yes'},
                           ComedySeries={'Brooklyn99', '70s Show', 'Friends', 'Great Country'},
                           DramaSeries={'Greys anatomy', 'Suits', 'Deckster', 'Game Of Thrones'},
                           )


@app.route('/assignment9', methods=['GET', 'POST'])
def goToAssignment9():
    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username
        return render_template('assignment9.html',  request_method=request.method,
                               username=username)

    if request.method == 'GET':
        global this1
        users = {'10': ["byron.fields@reqres.in", "Byron", "Fields", 'https://reqres.in/img/faces/10-image.jpg'],
                 '11': ["george.edwards@reqres.in", "George", "Edwards", "https://reqres.in/img/faces/11-image.jpg"],
                 '12': ["Rachel.howell@reqres.in", "Rachel", "Howell", "https://reqres.in/img/faces/12-image.jpg"]
                 }
        if 'name' in request.args:
            name = request.args['name']
            if name in users.keys():
                for u in users.keys():
                    if u == name:
                        this1 = users[u]
                return render_template('assignment9.html', name=name, request_method=request.method,
                                       users=users, val1=this1
                                       )
    return render_template('assignment9.html',
                           request_method=request.method, users=users)


@app.route('/mission7')
def go7():
    return render_template('mission7.html')


if __name__ == '__main__':
    app.run(debug=True)
