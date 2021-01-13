from flask import Blueprint, render_template

assignment10 = Blueprint('assignment10',
                         __name__,
                         static_folder='assignment10',
                         static_url_path='/pages/assignment10',
                         template_folder='pages/template')


@assignment10.route('/assignment10')
def ass10():
    return render_template('assignment10.html')
