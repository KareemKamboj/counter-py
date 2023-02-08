from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)   
app.secret_key = "shhhhhh" 

@app.route('/increment', methods=['POST'])
def increment():
    session['increment'] = request.form['increment']
    return redirect('/')


@app.route('/')          
def counter():
    if 'visit' in session:
        if'increment' in session:
            session['visit'] += int(session['increment'])
        else:
            session['visit'] += 1
    else:
        session['visit'] = 1
    return render_template("index.html") 


@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":      
    app.run(debug=True) 