from src.controllers.controller import IndexController
from src.controllers.controller import UpdateProdutoController
from src.controllers.controller import DeleteProdutoController
from src.controllers.errors import NotFoundController

routes = {
    "index_route": "/",
    "indexcontroller": IndexController.as_view("index"),
    "not_found_route": 404,
    "not_found_controller": NotFoundController.as_view("not_found"),
    "delete_route": "/delete/products/<int:code>",
    "delete_controller": DeleteProdutoController.as_view("delete"),
    "update_route": "/update/product/<int:code>",
    "update_controller": UpdateProdutoController.as_view("update"),
}
