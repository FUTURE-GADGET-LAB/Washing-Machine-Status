from flask import *
import os

app=Flask(__name__)

ImageFolder = os.path.join('static','Images')
app.config['UPLOAD_FOLDER'] = ImageFolder


# HomePage route
@app.route('/')
def Disp():
    # pic = os.path.join(app.config['UPLOAD_FOLDER'],'graph1.png')
    pic = 'http://192.168.137.132/photo'
    return render_template('renderHTMLfile.html', WashingMachTime = pic)

if __name__ == "__main__":
    app.run(debug=True)

# http://192.168.137.132/photo