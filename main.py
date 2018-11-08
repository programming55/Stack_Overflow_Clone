from app import app

app.secret_key = 'make this hard to guess!'
app.run(debug=True)