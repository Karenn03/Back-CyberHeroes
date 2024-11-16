from flask import Flask
from routes.users import users_bp
from routes.game import game_bp
from routes.level import level_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(game_bp)
app.register_blueprint(level_bp)

if __name__ == '__main__':
    app.run(debug=True)