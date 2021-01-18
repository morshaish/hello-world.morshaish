from flask import Blueprint, render_template, request, url_for, redirect
import mysql.connector

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/pages/assignment10',
    template_folder='temaplate')


# noinspection PyUnresolvedReferences
@assignment10.route('/assignment10', methods=['GET', 'POST'])
def ass10():
    return render_template('assignment10.html')


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


@assignment10.route('/users')
def users():
    query = "select * from users1"
    query_result = interact_db(query, query_type='fetch')
    print(query_result)
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        id1 = request.form['id']
        fname1 = request.form['firstName']
        lname1 = request.form['lastName']
        email1 = request.form['email']
        print(id1, fname1, lname1, email1)
        query = "INSERT INTO users1(userid, fname, lname, email) VALUES ('%s', '%s', '%s', '%s')" % (
        id1, fname1, lname1, email1)
        interact_db(query, query_type='commit')
        return redirect('/users')
    else:
        return render_template('insert.html')
    #
    #     query = "INSERT INTO users1(userid, fname, lname, email) VALUES ('%s', '%s', '%s', '%s')" % (id, fname, lname, email)
    #     interact_db(query, query_type='commit')
    # #     return render_template('insert.html')
    # return render_template(, request_method=request.method)


@assignment10.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        id = request.args['id']
        print(id)
        query = "DELETE FROM users1 WHERE userid='%s';" % id
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return 'User does not exist'


@assignment10.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        fname = request.form['firstName']
        lname = request.form['lastName']
        email = request.form['email']
        query = "UPDATE users1 SET fname='%s', lname='%s', email='%s' WHERE userid='%s'" % (fname, lname, email, id)
        interact_db(query, query_type='commit')
        return redirect('/users')
    return render_template('update.html')
