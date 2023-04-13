"""Setup at app startup"""
from app import routes
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-cgrqc8fdvk4rjsvbhdfg-a.oregon-postgres.render.com",
    database="todo_app_sxu7",
    user="todo_app_sxu7_user",
    password="8DRYLFyuH3Npu9t5mGacuuTHJBawP0g2")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
