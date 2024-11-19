import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from controller.userController import users_bp
    from controller.gameController import game_bp
    from controller.levelController import level_bp
    from controller.monsterController import monsters_bp
    from controller.categoryController import categories_bp
    from controller.questionController import questions_bp
    from controller.answerController import answers_bp
    from controller.gameHasMonstersController import gameHasMonsters_bp
    from controller.gameHasLevelController import gameHasLevel_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(level_bp)
    app.register_blueprint(monsters_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(questions_bp)
    app.register_blueprint(answers_bp)
    app.register_blueprint(gameHasMonsters_bp)
    app.register_blueprint(gameHasLevel_bp)

    @app.route('/') 
    def home(): 
        return "Welcome to CyberHeroes API!"
    
    return app