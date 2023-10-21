from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts for demonstration
posts = [
    {
        'title': 'My First Blog Post',
        'content': 'This is the content of my first blog post.',
    },
    {
        'title': 'Another Blog Post',
        'content': 'Here is another blog post. Flask is awesome!',
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    if 0 <= post_id < len(posts):
        post = posts[post_id]
        return render_template('post.html', post=post)
    else:
        return "Post not found"

if __name__ == '__main__':
    app.run(debug=True)
