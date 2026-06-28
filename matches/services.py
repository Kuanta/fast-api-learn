from sqlalchemy.orm import Session
from matches.models import MatchModel, MatchParticipantModel
from matches.schemas import MatchData
from players.services import increase_win, increase_lose


def get_all_matches(db: Session) -> list[MatchData]:
    return db.query(MatchModel).all()

def get_match_by_id(db: Session, match_id: int):
    return db.query(MatchModel).filter(MatchModel.id == match_id).first()

def create_match(db: Session, match_data: MatchData):
    new_match = MatchModel(
        game_id=match_data.game_id,
        winner_faction=match_data.winner_faction,
        is_draw=match_data.winner_faction is None,
    )
    db.add(new_match)
    db.flush()

    # Add participants
    for participant_data in match_data.participants:
        participant = MatchParticipantModel()
        participant.match_id = new_match.id
        participant.account_id = participant_data.account_id
        participant.faction_id = participant_data.faction_id
        db.add(participant)

        # Update win lsoe
        if participant_data.faction_id == match_data.winner_faction:
            increase_win(participant_data.account_id, match_data.game_id, db)
        else:
            increase_lose(participant_data.account_id, match_data.game_id, db)

    db.commit()
    db.refresh(new_match)
    return new_match


