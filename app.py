from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "so-secret"

@app.route('/')
def make_form():
    """Generate form"""

    prompts = story.prompts

    return render_template("form.html", prompts=prompts)

@app.route('/story')
def tell_story():
    """Show story formed"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)