from functools import wraps
from flask import flash, redirect, session, url_for


def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user" not in session:
      flash("Faça login para acessar esta página.", "warning")
      return redirect(url_for("auth.login"))
    return f(*args, **kwargs)

  return decorated_function


def guest_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user" in session:
      return redirect(url_for("auth.welcome"))
    return f(*args, **kwargs)

  return decorated_function