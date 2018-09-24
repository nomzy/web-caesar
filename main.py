from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="POST">
      <label for="key" > <strong> Rotate by: </strong></label>
         <input type="text" name="rot" id = "key" value=0>
         <br/>
         <textarea name="text">{onome}</textarea>
      <input type="submit" value="Submit Query"/>
      </form>
    </body>
    
</html>"""




@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot_key = int (request.form["rot"])
    messgae = request.form["text"]
    encrypted_message = rotate_string(message,rot_key)

    return form.format(onome = encrypted_message)


app.run()