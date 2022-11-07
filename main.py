import os
from app import create_app
from dotenv import load_dotenv
from flask import render_template
load_dotenv()
env_name=os.getenv('FLASK_ENV')
print(env_name)
app = create_app()
port=os.getenv('FLASK_PORT')

# @app.route('/')                       
# def index():
#     return  render_template('index.html')
if __name__ == '__main__': 

    app.run(host='0.0.0.0', port=port, debug=True)
