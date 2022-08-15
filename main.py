from flask import jsonify

from src.app import prod_app

app = prod_app()


@app.errorhandler(404)
def method_not_allowed(a):
    return jsonify({"Message": "not found pls ask for help"})


@app.errorhandler(401)
def forbiden(a):
    return jsonify({"Message": "Not loged pls login to the API"})


@app.errorhandler(400)
def bad_request(a):
    return jsonify({"Message": "Bad request , pls review the payload"})


@app.errorhandler(500)
def server_error(a):
    return jsonify({"Message": "interal server error pls call to support"})


if __name__ == "__main__":
    app.run(debug=True)
