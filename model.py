from flask_sqlalchemy import SQLAlchemy
# from seed import load_games


db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    with open("data/games.csv") as g:
        for i, row in enumerate(g):
            row = row.rstrip()
            name, description = row.split("|")

            game = Game(name=name, description=description)

            # We need to add to the session or it won't ever be stored
            db.session.add(game)

        # Once we're done, we should commit our work
        db.session.commit()



if __name__ == '__main__':
    from party import app
    connect_to_db(app)
    print("Connected to DB.")
