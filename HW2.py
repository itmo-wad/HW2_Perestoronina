from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("HW1.html")
    
@app.route('/img/')
def index2():
    return "<a href='/img/1.jpg'>The 1st image</a>" "<a href='/img/2.jpg'> The 2nd image </a>" "<a href='/img/3.jpg'> The 3rd image </a>" "<a href='/img/4.jpg'> The 4th image </a>" "<a href='/img/5.jpg'> The 5th image </a>" "<a href='/img/6.jpg'> The 6th image </a>" "<a href='/img/7.jpg'> The 7th image </a>" "<a href='/img/8.jpg'> The 8th image </a>" "<a href='/img/9.jpg'> The 9th image </a>"
  
@app.route('/img/<path:path>')
def index3(path):
    return send_from_directory('static\\img', path)

@app.route('/static/js/<path:path>')
def index13(path):
    return send_from_directory('static', path)  # Send files from static/img directory    

    
    
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)