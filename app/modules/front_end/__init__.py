from flask import Blueprint


#Create new Blueprint
front_end = Blueprint("front_end",__name__,template_folder="templates")

from app.modules.front_end.views import post_view, home_view
