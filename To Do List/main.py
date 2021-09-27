from website import create_app
from flask import render_template
app = create_app()
    
@app.route('/')
def test():
    return render_template('todolist.html')

if __name__ == '__main__':
    app.run(debug=True)