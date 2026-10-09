
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow requests from your GitHub Pages website
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "https://spsaraniit-hash.github.io"
            ]
        }
    }
)

# Sample academic data only.
# Live stock prices will be connected in a later step.
COMPANIES = [
    {
        "symbol": "TCS",
        "name": "Tata Consultancy Services",
        "sector": "Information Technology",
        "price": None,
        "data_type": "sample"
    },
    {
        "symbol": "INFY",
        "name": "Infosys",
        "sector": "Information Technology",
        "price": None,
        "data_type": "sample"
    },
    {
        "symbol": "RELIANCE",
        "name": "Reliance Industries",
        "sector": "Energy and Retail",
        "price": None,
        "data_type": "sample"
    },
    {
        "symbol": "HDFCBANK",
        "name": "HDFC Bank",
        "sector": "Banking",
        "price": None,
        "data_type": "sample"
    },
    {
        "symbol": "ICICIBANK",
        "name": "ICICI Bank",
        "sector": "Banking",
        "price": None,
        "data_type": "sample"
    },
    {
        "symbol": "SBIN",
        "name": "State Bank of India",
        "sector": "Banking",
        "price": None,
        "data_type": "sample"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Stock Market Analysis API is running",
        "status": "success"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Backend is working"
    })


@app.route("/api/companies")
def get_companies():
    return jsonify({
        "count": len(COMPANIES),
        "companies": COMPANIES
    })


@app.route("/api/companies/<symbol>")
def get_company(symbol):
    symbol = symbol.upper()

    for company in COMPANIES:
        if company["symbol"] == symbol:
            return jsonify(company)

    return jsonify({
        "error": "Company not found"
    }), 404


if __name__ == "__main__":
    app.run()
