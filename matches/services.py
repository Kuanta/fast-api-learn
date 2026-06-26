from sqlalchemy.orm import Session
from matches.models import MatchModel
from matches.schemas import MatchCreateData, MatchUpdateData


def get_all_matches(db: Session):
    return db.query(MatchModel).all()

def get_match_by_id(db: Session, match_id: int):
    return db.query(MatchModel).filter(MatchModel.id == match_id)

def create_match(db: Session, match_data: MatchCreateData):
    new_match = MatchModel(**match_data.model_dump())
    db.add(new_match)
    db.commit()
    db.refresh(new_match)
    return new_match


