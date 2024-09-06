from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "supersecretkey"
users_db = {}

@app.route("/", methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in users_db:
            flash("L'utilisateur existe déjà, veuillez vous connecter.")
            return redirect(url_for('login'))
        
        users_db [email] = password
        flash("Inscription réussie, veuillez vous connecter.")
        return redirect(url_for('login'))
                        
    return render_template("signup.html.jinja")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in users_db and users_db[email] == password:
            flash(f"Bienvenue {email}!")
            return redirect(url_for('profile'))
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect.")
    return render_template("login.html.jinja")

@app.route("/profile")
def profile():
    return render_template("profile.html.jinja")


if __name__ == '__main__':
    app.run(debug=True)


