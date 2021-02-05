from app import db


class Post(db.Model):
    id: int = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id: int = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    title: str = db.Column(
        db.String(225),
        nullable=False
    )

    slug: str = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    image: str = db.Column(
        db.String(191),
        nullable=False
    )

    post: str = db.Column(
        db.Text,
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