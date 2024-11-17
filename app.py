from flask import Flask

from routes.users import users_bp
from routes.game import game_bp
from routes.level import level_bp
from routes.monsters import monsters_bp
from routes.categories import categories_bp
from routes.questions import questions_bp
from routes.answers import answers_bp
from routes.gameHasMonsters import gameHasMonsters_bp
from routes.gameHasLevel import gameHasLevel_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(game_bp)
app.register_blueprint(level_bp)
app.register_blueprint(monsters_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(answers_bp)
app.register_blueprint(gameHasMonsters_bp)
app.register_blueprint(gameHasLevel_bp)

if __name__ == '__main__':
    app.run(debug=True)