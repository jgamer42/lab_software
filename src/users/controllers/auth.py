from src.users.models import Permission, PermissionRole, Role


class AuthHelper:
    def __init__(self, role: int):
        self.role_manager = Role
        self.permission_manager = Permission
        self.permision_role_manager = PermissionRole
        self.create_permissions(role)
        self.name = self.role_manager.query.get(role).name

    def create_permissions(self, role: int):
        self.permissions = (
            self.permission_manager.query.join(self.permision_role_manager)
            .join(self.role_manager)
            .add_columns(self.permission_manager.name)
            .filter(self.permision_role_manager.role == role)
        )
        self.permissions = [p[1] for p in self.permissions]

    def can_create_admin(self) -> bool:
        if "CREATE_ADMIN_USER" in self.permissions:
            return True
        else:
            return False

    def can_access_crud_books(self) -> bool:
        if "CRUD_BOOKS" in self.permissions:
            return True
        else:
            return False

    def serialize(self) -> list:
        return self.permissions
