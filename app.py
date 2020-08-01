from flask import Flask, render_template

app = Flask(__name__)


@app.route('/',  methods=['GET'])
def show_homepage():
    return render_template('pages/home.html')


@app.route('/pages/create_post.html', methods=['GET'])
def show_create_post():
    return render_template('pages/create_post.html')


if __name__ == '__main__':
    app.run()



