from flask import Flask
from src.routes.routes import routes
from src.controllers.errors import NotFoundController

app = Flask(__name__)


app.add_url_rule(routes["index_route"], view_func=routes["indexcontroller"])

app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])


@app.errorhandler(404)
def not_found_error(error):
    not_found_controller = NotFoundController()
    return not_found_controller.get(error), 404
