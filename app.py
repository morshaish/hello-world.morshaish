from flask import Flask, render_template, request, session
from flask import jsonify
import mysql.connector
from pages.assignment10.assignment10 import assignment10

app = Flask(__name__)
app.secret_key = '1234'

app.register_blueprint(assignment10)


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
    username = ''
    if request.method == 'POST':
        username = request.form['username']
        if username != '':
            session['logged_in'] = True
            session['username'] = username
            return render_template('assignment9.html', request_method=request.method,
                                   username=username)

        logout = request.args['logout']
        if logout:
            session['logged_in'] = False

        else:
            session['logged_in'] = False

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


@app.route('/assignment11/users')
def getusers():
    if request.method == 'GET':
        query = "select * from users1"
        query_result = interact_db(query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                "data": []
            })
        else:
            return jsonify({
                'success': 'True',
                'data': query_result,
            })


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='schema_name'
                                         )
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@app.route('/assignment11/users/selected', defaults={'userid': 1})
@app.route('/assignment11/users/selected/<int:userid>')
def get_user(userid):
    if request.method == "GET":
        query = "SELECT * FROM users1 WHERE userid='%s';" % userid
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                "data": [],
                'User Is Not Exist': []
            })
        else:
            return jsonify({
                'success': 'True',
                'data': query_result,
            })




if __name__ == '__main__':
    app.run(debug=True)
