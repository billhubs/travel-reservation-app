from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'  # SQLite database
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    departure_date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default="Pending")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        service_type = request.form['service_type']
        departure_date = request.form['departure_date']
        new_reservation = Reservation(name=name, service_type=service_type, departure_date=departure_date)
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('confirmation', reservation_id=new_reservation.id))
    return render_template('reservation.html')

@app.route('/confirmation/<int:reservation_id>')
def confirmation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    return render_template('confirmation.html', reservation=reservation)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/admin')
def admin():
    reservations = Reservation.query.all()
    return render_template('admin.html', reservations=reservations)
