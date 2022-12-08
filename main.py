from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def get_page():
    return f"<pre>{get_all()}</pre>"


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    return f"<pre>{get_candidate_by_pk(pk)}</pre>"


@app.route("/candidates/<skill_name>")
def get_cand_by_skill(skill_name):
    return f"<pre>{get_by_skill(skill_name)}</pre>"


app.run()
