from flask import Flask
app = Flask(__name__)

#intialize directory in chich app begins
#preempt http requester methods to be used (GET, POST)
@app.route('/', methods=['GET', 'POST'])

def index():
    #displays index page within the '/' directory
    return render_template('index.html')

if __name__ == '__main__':
    #run the app from main
  app.run()
