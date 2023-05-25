from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# Criando a rota do início
@app.route('/')
def homepage():
    name = request.args.get("name")
    response = {"data": f"Hello, {name} !"}
    return jsonify(response)  

# Exemplo ===>  http://127.0.0.1:5000/?name=Python


# Para identificar o nome
# @app.route('/home')
# def name():
#     name = request.args.get("name")
#     if not name:
#         return jsonify({"status": "error"},)

#     response = {"data": f"Hello, {name} !"}
#     return jsonify(response)


# Para criar first and last name
# @app.route('/home')
# def fullname():
#     fname = request.args.get("fname")
#     lname = request.args.get("lname")

#     if not fname and not lname:
#         return jsonify({"status": "error"},)
#     elif fname and not lname:
#         response = {"data": f"Hello, {fname} !"}
#     elif not fname and lname:
#         response = {"data": f"Hello, Mr. {lname} !"}
#     else:
#         response = {"data": f"Is your name {fname} {lname}"}

#     return jsonify(response)

# exemplo ==> http://127.0.0.1:5000/home?fname=Flask&lname=jonsify






if __name__ == "__main__":
    app.run(debug=True)
