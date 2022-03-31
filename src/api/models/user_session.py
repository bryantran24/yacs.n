from tortoise import fields
from tortoise.models import Model


class UserSession(Model):
    session_id = fields.UUIDField(pk=True)
    user_id = fields.IntField(nullable=False)
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()

    class Meta:
        table = "user_session"