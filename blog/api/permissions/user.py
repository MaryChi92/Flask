from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForGet,
    PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import User


class CustomUserGetPermission(PermissionMixin):
    """
    Describe permissions for get User
    """

    ALL_AVAILABLE_FIELDS = [
        "id",
        "username",
        "email",
        "is_staff",
    ]

    def get(
        self, *args, many=True, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForGet:
        if not current_user.is_authenticated:
            raise AccessDenied("No access")

        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get


class CustomUserPatchPermission(PermissionMixin):
    """
    Describe permission for patch User.
    """

    PATCH_AVAILABLE_FIELDS = (
        "username",
        "is_staff",
    )

    def patch_permission(
        self, *args, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForPatch:

        if not (current_user.is_authenticated and current_user.is_staff):
            raise AccessDenied("Login first and keep being user or admin")

        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(
        self,
        *args,
        data=None,
        obj=None,
        user_permission: PermissionUser = None,
        **kwargs
    ) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(
            model=User
        )
        return {
            field: data
            for field, data in data.items()
            if field in permission_for_patch.columns
        }