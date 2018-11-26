from flask import Flask
from flask import request, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/file')
def file():
    return render_template("file.html")


@app.route('/fileRead')
def file_read():
    return render_template("fileRead.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()
    '''
    # error = None
    return render_template("login.html")


def do_login():
    print('do_login')
    pass


def show_login_form():
    print('show_login_form')
    pass


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


'''
string	(default) accepts any text without a slash
int	    accepts positive integers
float	accepts positive floating point values
path	like string but also accepts slashes
uuid	accepts UUID strings
'''


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

'''
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'
'''




