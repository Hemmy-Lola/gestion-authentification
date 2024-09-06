```app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Nécessaire pour utiliser les messages flash

# Simule une base de données en mémoire
users_db = {}

@app.route('/')
def home():
    return render_template('base.html')

# Route pour s'inscrire (signup)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users_db:
            flash("L'utilisateur existe déjà, veuillez vous connecter.")
            return redirect(url_for('signin'))
        
        users_db[username] = password
        flash("Inscription réussie, veuillez vous connecter.")
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

# Route pour se connecter (signin)
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vérifie les informations de connexion
        if username in users_db and users_db[username] == password:
            flash(f"Bienvenue {username}!")
            return redirect(url_for('home'))
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect.")
    
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```base.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application Flask</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Bienvenue sur l'application Flask</h1>
    <nav>
        <a href="{{ url_for('signin') }}">Se connecter</a>
        <a href="{{ url_for('signup') }}">S'inscrire</a>
    </nav>
    <div>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul class="messages">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
    </div>
    <div>
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

```signin.html
{% extends 'base.html' %}

{% block content %}
<h2>Connexion</h2>
<form method="POST" action="{{ url_for('signin') }}">
    <label for="username">Nom d'utilisateur</label>
    <input type="text" id="username" name="username" required>
    
    <label for="password">Mot de passe</label>
    <input type="password" id="password" name="password" required>
    
    <button type="submit">Se connecter</button>
</form>
{% endblock %}
```

```signup.html
{% extends 'base.html' %}

{% block content %}
<h2>Inscription</h2>
<form method="POST" action="{{ url_for('signup') }}">
    <label for="username">Nom d'utilisateur</label>
    <input type="text" id="username" name="username" required>
    
    <label for="password">Mot de passe</label>
    <input type="password" id="password" name="password" required>
    
    <button type="submit">S'inscrire</button>
</form>
{% endblock %}
```

```style.css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

nav {
    margin-bottom: 20px;
}

nav a {
    margin-right: 10px;
    text-decoration: none;
    color: #333;
}

form {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

label {
    display: block;
    margin-bottom: 8px;
}

input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.messages {
    color: red;
}
``