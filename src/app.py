from flask import Flask
app = Flask(__name__)

@app.route("/home")  
def home():  
    return "Este es mi portafolio"  

@app.route("/about-me")  
def about_me():  
    return "Soy un desrrollador web en formación con 4Geeks academy" 

@app.route("/contact-me")  
def contact_me():  
    return "Mi correo electrónico es diegomenoruceta@gmail.com" 


app.run(host='0.0.0.0', port=4201)