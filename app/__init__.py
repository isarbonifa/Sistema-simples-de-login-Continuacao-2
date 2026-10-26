from flask import Flask


def create_app():
  app = Flask(
      __name__, template_folder="views/templates", static_folder="views/static"
  )

  import os
  from dotenv import load_dotenv

  load_dotenv()
  app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave_padrao_para_desenvolvimento")
  #com o os.getenv, a chave é guardada no .env (que fica no .gitignore)

  from app.controllers.auth_controller import auth_bp

  app.register_blueprint(auth_bp)

  return app