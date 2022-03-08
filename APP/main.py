# from flask import *
# app=Flask(__name__)
# @app.route('/admin')
# def admin():
#     return 'this is admin'
# @app.route('/student')
# def student():
#     return 'this is student'
# @app.route('/staff')
# def staff():
#     return 'this is staff'
# @app.route('/user/<name>')
# def user(name):
#     if name == 'admin':
#         return redirect(url_for('admin'))
#     if name == 'student':
#         return redirect(url_for('student'))
#     if name == 'staff':
#         return redirect(url_for('staff'))
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import *
from flask import Flask
app = Flask(__name__)
@app.route('/')
def message():
    return render_template('base.html')
if __name__ == '__main__':
    app.run(debug=True)