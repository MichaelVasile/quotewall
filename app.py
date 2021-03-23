from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy(app)

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    context = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Quote %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        quote_content = request.form['quote']
        name_content = request.form['name']
        context_content = request.form['context']

        new_quote = Quotes(quote=quote_content, name=name_content, context=context_content)

        try:
            db.session.add(new_quote)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error..."
    else:
        quotes = Quotes.query.order_by(Quotes.date_created.desc()).all()
        return render_template('index.html', quotes=quotes)

@app.route('/debug', methods=['POST', 'GET'])
def debug():
    if request.method == 'POST':
        quote_content = request.form['quote']
        name_content = request.form['name']
        context_content = request.form['context']

        new_quote = Quotes(quote=quote_content, name=name_content, context=context_content)

        try:
            db.session.add(new_quote)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error..."
    else:
        quotes = Quotes.query.order_by(Quotes.date_created.desc()).all()
        return render_template('debug.html', quotes=quotes)

# @app.route('/quotes')
# def quotes():
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)