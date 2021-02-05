from app import db


class User(db.Model):
    id: int = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name: str = db.Column(
        db.String(191),
        nullable=False
    )

    email: str = db.Column(
        db.String(191),
        unique=True,
        nullable=False
    )

    password: str = db.Column(
        db.String(191),
        nullable=False
    )

    role: str = db.Column(
        db.String(191),
        nullable=False
    )

    created_at: str = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )

    updated_at: str = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )

    @property
    def rolenames(self):
        try:
            return self.role.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, identifier):
        return cls.query.filter(User.email == identifier).one_or_none()

    @classmethod
    def identify(cls, _id):
        return cls.query.get(_id)

    @property
    def identity(self):
        return self.id

