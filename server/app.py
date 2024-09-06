from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this to a more secure key in production
users_db = {}

@app.route("/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Récupérer toutes les informations du formulaire d'inscription
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        birthday = request.form.get('birthday')
        phone = request.form.get('phone')

        # Vérifier si l'utilisateur existe déjà
        if email in users_db:
            flash("L'utilisateur existe déjà, veuillez vous connecter.")
            return redirect(url_for('login'))

        # Stocker toutes les informations de l'utilisateur dans users_db
        users_db[email] = {
            'password': password,
            'firstname': firstname,
            'lastname': lastname,
            'birthday': birthday,
            'phone': phone
        }
        
        flash("Inscription réussie, veuillez vous connecter.")
        return redirect(url_for('login'))

    return render_template("signup.html.jinja")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users_db and users_db[email]['password'] == password:
            session['user'] = email  # Stocke l'utilisateur dans la session
            flash(f"Bienvenue {email}!")
            return redirect(url_for('profile'))
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect.")
    
    return render_template("profile.html.jinja")

@app.route("/profile")
def profile():
    if 'user' not in session:
        flash("Veuillez vous connecter pour accéder à cette page.")
        return redirect(url_for('login'))  # Redirection vers login si non connecté

    # Récupérer les informations de l'utilisateur depuis users_db
    user_info = users_db[session['user']]

    return render_template(
        "profile.html",
        firstname=user_info['firstname'],
        lastname=user_info['lastname'],
        email=session['user'],
        birthday=user_info['birthday'],
        phone=user_info['phone']
    )

@app.route("/logout", methods=['POST'])
def logout():
    session.pop('user', None)  # Déconnecte l'utilisateur
    flash("Vous êtes déconnecté.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
