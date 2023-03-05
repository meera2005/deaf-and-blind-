import os
from flask import Flask, render_template, redirect, url_for
from flask.globals import request
from werkzeug.utils import secure_filename
import camelot
import os
import openai
from dictionary import *
from table1 import *
from chat import *

openai.api_key = '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'
# openai.api_key = os.environ.get("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")
# openai.organization=os.getenv("OPENAI_ORGANIZATION")


# from workers import pdf2text, txt2questions

# Constants
UPLOAD_FOLDER = './pdf/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@ app.route('/',methods=['GET', 'POST'])
def index():
    if not os.path.isdir('./pdf'):
        os.mkdir('./pdf')
    flag=0
    if request.method == 'POST':
        try:
            # Retrieve file from request
            uploaded_file = request.files['pdf-file']
            # file_path = os.path.join(r'C:\Users\91918\One\Desktop\programmes\project_medical')
                #app.config['UPLOAD_FOLDER'],
                #secure_filename(
                    #uploaded_file.filename))
            file_exten = uploaded_file.filename.rsplit('.', 1)[1].lower()
            flag=1
            # Save uploaded file
            uploaded_file.save(uploaded_file.filename)
        except Exception as e:
            print(e) 
        print(type(uploaded_file))
        d=file_read(uploaded_file.filename)
        # msg='ghdhsdjkkj'
        msg=opppen(d) 
        msg.replace('-', '<li>')
        print('here1')
        return render_template('index.html',my_string=msg) 
        print('here2')
        # if(flag==1):
        #     d=file_read() 
        #     response=openai.ChatCompletioncreate(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Who are you?"}])
        #     print(response.choices[0].message.content)

    else:
      return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

