from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def signup_form():
    return render_template("index.html",username = "", email = "", username_error = "", password_error = "", password_validate_error = "", email_error = "")

@app.route("/signup", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    
    username_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""


    if username.strip() == "" or (len(username)<3) or (len(username)>20):
        username_error = "That's not a valid username"

    if password.strip() == "" or (len(password)<3) or (len(password)>20):
        password_error = "That's not a valid password"
        
    if verify_password == "" or (password != verify_password):
        password_validate_error = "Passwords don't match"
        
    if (email != '') and (len(email)<3 or len(email)>20 or email.count('@')!=1 or email.count('.')!=1 or email.count(' ')>0):
        email_error = "That's not a valid email." 

    if (not username_error) and (not password_error) and (not password_validate_error) and (not email_error):
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template("index.html", username= username, email = email, username_error = username_error, password_error= password_error,password_validate_error=password_validate_error, email_error=email_error)


@app.route("/welcome")
def valid_signup():
    user_name = request.args.get('username')
    return render_template("welcome.html", username = user_name)

app.run()
