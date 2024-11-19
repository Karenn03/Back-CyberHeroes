from typing import Type, TypeVar, Generic
from sqlalchemy.orm import Session

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_all(self):
        try:
            return self.db.query(self.model).all()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error retrieving all records: {e}")

    def get_by_id(self, id):
        try:
            return self.db.query(self.model).filter(self.model.id == id).first()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error retrieving record by ID: {e}")

    def add(self, entity):
        try:
            self.db.add(entity)
            self.db.commit()
            self.db.refresh(entity)
            return entity
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error adding entity: {e}")

    def update(self, entity):
        try:
            self.db.merge(entity)
            self.db.commit()
            self.db.refresh(entity)
            return entity
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating entity: {e}")

    def delete(self, entity):
        try:
            self.db.delete(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error deleting entity: {e}")