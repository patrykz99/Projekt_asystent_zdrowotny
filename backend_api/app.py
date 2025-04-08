from flask import Flask, send_from_directory
from dotenv import load_dotenv


class HealthConsultantApp():
    def __init__(self):
        self.app = Flask(__name__,static_url_path='',static_folder='../template_front')
        
        self.set_routes()
        
    def set_routes(self):
        
        @self.app.route("/")
        def index():
            return send_from_directory('../template_front','index.html')

        @self.app.route("/chat",methods=["POST"])
        def chat():
            pass
        
    def run_app(self):
        self.app.run(debug=True)
        