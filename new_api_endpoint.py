from flask import Flask, request, jsonify
from new_schema import PortfolioUpload, ValidationError

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running!"})

@app.route("/upload", methods=["POST"])
def upload():
    try:
        data = request.get_json()
        portfolio = PortfolioUpload(**data)
        return jsonify({
            "status": "success",
            "holdings_count": len(portfolio.holdings)
        }), 200
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "detail": e.errors()
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
