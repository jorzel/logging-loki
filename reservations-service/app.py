import logging

from flask import Flask


app = Flask(__name__)

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', encoding='utf-8', level=logging.INFO)


@app.route("/reservations", methods=["GET"])
def reservations():
    logging.info("Reservations endpoint")
    return "ok"
