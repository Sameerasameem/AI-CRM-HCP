from langchain_core.tools import tool
from database import SessionLocal
from models import Interaction

@tool
def log_interaction(
    hcp_name: str,
    interaction_type: str,
    notes: str
):
    """
    Log an interaction into PostgreSQL database.
    """

    db = SessionLocal()

    try:
        interaction = Interaction(
            hcp_name=hcp_name,
            interaction_type=interaction_type,
            notes=notes
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return {
            "status": "success",
            "message": f"Interaction saved successfully for {hcp_name}"
        }

    finally:
        db.close()
@tool
def search_interaction(hcp_name: str):
    """
    Search interactions from PostgreSQL database.
    """

    db = SessionLocal()

    try:
        interactions = (
            db.query(Interaction)
            .filter(Interaction.hcp_name.ilike(f"%{hcp_name}%"))
            .all()
        )

        if not interactions:
            return {
                "status": "No interactions found"
            }

        result = []

        for i in interactions:
            result.append({
                "id": i.id,
                "hcp_name": i.hcp_name,
                "interaction_type": i.interaction_type,
                "notes": i.notes,
                "created_at": str(i.created_at)
            })

        return result

    finally:
        db.close()

@tool
def generate_summary(hcp_name: str):
    """
    Generate summary of HCP interactions.
    """

    db = SessionLocal()

    try:
        interactions = (
            db.query(Interaction)
            .filter(Interaction.hcp_name.ilike(f"%{hcp_name}%"))
            .all()
        )

        if not interactions:
            return {
                "summary": "No interactions found."
            }

        summary = ""

        for i in interactions:
            summary += f"- {i.interaction_type}: {i.notes}\n"

        return {
            "summary": summary
        }

    finally:
        db.close()
@tool
def edit_interaction(
    interaction_id: int,
    notes: str
):
    """
    Edit an existing interaction.
    """

    db = SessionLocal()

    try:

        interaction = db.query(Interaction).filter(
            Interaction.id == interaction_id
        ).first()

        if interaction is None:
            return {
                "status": "Interaction not found"
            }

        interaction.notes = notes

        db.commit()

        return {
            "status": "success",
            "message": "Interaction updated successfully"
        }

    finally:
        db.close()

@tool
def recommend_next_action(hcp_name: str):
    """
    Recommend next follow-up action.
    """

    db = SessionLocal()

    try:
        count = (
            db.query(Interaction)
            .filter(Interaction.hcp_name.ilike(f"%{hcp_name}%"))
            .count()
        )

        if count == 0:
            return {
                "recommendation": "Schedule the first meeting."
            }

        return {
            "recommendation": f"Schedule a follow-up meeting with {hcp_name}."
        }

    finally:
        db.close()

tools = [
    log_interaction,
    edit_interaction,
    search_interaction,
    generate_summary,
    recommend_next_action
]