from app_logging import setup_logging

LOG = setup_logging()

import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")

LOG.info("Opening client's private key \"client.key\"")
with open("client.key", "rb") as fp:
    client_key = fp.read()

LOG.info("Opening client's public key \"client.pem\"")
with open("client.pem", "rb") as fp:
    client_cert = fp.read()

LOG.info("Opening CA cert \"ca.pem\"")
with open("ca.pem", "rb") as fp:
    ca_cert = fp.read()
creds = grpc.ssl_channel_credentials(ca_cert, client_key, client_cert)
recommendations_channel = grpc.secure_channel(
    f"{recommendations_host}:443", creds
)
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )
