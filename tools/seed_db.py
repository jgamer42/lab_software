import hashlib
import json
import os
import sys

sys.path.append(os.getcwd())
from extensions import db
from src.app import prod_app
from src.users import models as user_models


def seed_permissions() -> None:
    """Method used to insert the permissions registred on the file permisos.json on seeders"""
    app = prod_app()
    seeders_path: str = f"{os.getcwd()}/src/users/seeders"
    seeder_file = open(seeders_path + "/permisos.json", "r")
    seeder_permisos: dict = json.load(seeder_file)
    with app.app_context():
        for permiso in seeder_permisos:
            try:
                new_role = user_models.Permission(**permiso)
                db.session.add(new_role)
                db.session.commit()
            except Exception as Error:
                print(f"fails with {permiso}")
                continue


def seed_roles() -> None:
    """Method used to insert the permissions registred on the file roles.json on seeders"""
    app = prod_app()
    seeders_path: str = f"{os.getcwd()}/src/users/seeders"
    seeder_file = open(seeders_path + "/roles.json", "r")
    seeder_roles: dict = json.load(seeder_file)
    seed_permissions()
    with app.app_context():
        for rol in seeder_roles:
            try:
                new_role = user_models.Role(
                    id=rol.get("id"), name=rol.get("name", "no_existe")
                )
                db.session.add(new_role)
                db.session.commit()
            except Exception as Error:
                print(f"fails with {rol}")
                continue
            for permiso in rol.get("permissions"):
                try:
                    role_permissions = user_models.PermissionRole(
                        role=new_role.id, permission=permiso
                    )
                    db.session.add(role_permissions)
                    db.session.commit()
                except Exception as Error:
                    print(f"fails with {rol}")
                    continue


def seed_users() -> None:
    """Method used to insert the permissions registred on the file roles.json on seeders"""
    app = prod_app()
    seeders_path: str = f"{os.getcwd()}/src/users/seeders"
    seeder_file = open(seeders_path + "/users.json", "r")
    seeder_users: dict = json.load(seeder_file)
    seed_roles()
    with app.app_context():
        for user in seeder_users:
            try:
                new_role = user_models.User(**user)
                db.session.add(new_role)
                db.session.commit()
            except Exception as Error:
                print(f"fails with {user}")
                continue


seed_users()
