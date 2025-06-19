from sqlalchemy.orm import Session
from .schemas import FlowersImage


def add_flowers_image(db: Session, name: str, image_path: str):
    """ """
    fl_image = FlowersImage(name=name, image_path=image_path)
    db.add(fl_image)
    db.commit()
    db.refresh(fl_image)
    return fl_image
