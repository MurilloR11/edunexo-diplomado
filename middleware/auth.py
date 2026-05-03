from functools import wraps
from flask import session, redirect, url_for, flash

ROLE_DASHBOARD = {
    "ADMINISTRADOR": "dashboard_admin",
    "DOCENTE": "dashboard_docente",
    "ESTUDIANTE": "dashboard_estudiante",
}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Inicia sesión para continuar.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user_id" not in session:
                flash("Inicia sesión para continuar.", "error")
                return redirect(url_for("login"))
            user_role = session.get("user_role")
            if user_role not in roles:
                flash("No tienes permiso para acceder a esta sección.", "error")
                endpoint = ROLE_DASHBOARD.get(user_role)
                return redirect(url_for(endpoint) if endpoint else url_for("login"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def redirect_by_role():
    role = session.get("user_role")
    endpoint = ROLE_DASHBOARD.get(role)
    if endpoint:
        return redirect(url_for(endpoint))
    flash("Rol no reconocido. Vuelve a iniciar sesión.", "error")
    return redirect(url_for("login"))
