from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, model):
        return self.db.query(model).all()

    def get_by_id(self, model, id):
        return self.db.query(model).filter(model.id == id).first()

    def add(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self):
        self.db.commit()

    def delete(self, entity):
        self.db.delete(entity)
        self.db.commit()