from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Homepage.html')

@app.route('/calendrier')
def calendrier():
    return render_template('calendrier.html')

@app.route('/prof_par_etu')
def prof_par_etu():
    return render_template('prof_par_etu.html')

@app.route('/prof_filiere')
def prof_filiere():
    return render_template('prof_filiere.html')

if __name__ == '__main__':
    app.run(debug=True)
