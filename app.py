from flask import Flask, render_template

forest_blog = Flask(__name__)


@forest_blog.route('/', methods=['GET'])
def show_homepage():
    return render_template('pages/home.html')


@forest_blog.route('/pages/create_post.html', methods=['GET'])
def show_create_post():
    return render_template('pages/create_post.html')


if __name__ == '__main__':
    forest_blog.run()



