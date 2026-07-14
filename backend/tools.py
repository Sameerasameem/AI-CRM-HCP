from langchain_core.tools import tool
from database import SessionLocal
from models import Interaction


@tool
def log_interaction(details: str):
    """
    Save HCP doctor interaction details in CRM.
    """

    db = SessionLocal()

    try:
        interaction = Interaction(
            hcp_name="Unknown HCP",
            details=details
        )

        db.add(interaction)
        db.commit()

        return f"CRM interaction saved successfully: {details}"

    except Exception as e:
        db.rollback()
        return f"Error: {str(e)}"

    finally:
        db.close()


@tool
def edit_interaction(interaction_id: int, updated_details: str):
    """
    Edit an existing HCP interaction.
    """

    db = SessionLocal()

    try:
        interaction = db.query(Interaction).filter(
            Interaction.id == interaction_id
        ).first()

        if interaction is None:
            return "Interaction not found."

        interaction.details = updated_details
        db.commit()

        return f"Interaction {interaction_id} updated successfully."

    except Exception as e:
        db.rollback()
        return f"Error: {str(e)}"

    finally:
        db.close()


@tool
def get_interaction(interaction_id: int):
    """
    Get interaction details by ID.
    """

    db = SessionLocal()

    try:
        interaction = db.query(Interaction).filter(
            Interaction.id == interaction_id
        ).first()

        if interaction is None:
            return "Interaction not found."

        return f"""
Interaction ID: {interaction.id}
HCP: {interaction.hcp_name}
Details: {interaction.details}
"""

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        db.close()


@tool
def list_interactions():
    """
    List all CRM interactions.
    """

    db = SessionLocal()

    try:
        interactions = db.query(Interaction).all()

        if not interactions:
            return "No interactions found."

        output = ""

        for item in interactions:
            output += (
                f"ID: {item.id}\n"
                f"HCP: {item.hcp_name}\n"
                f"Details: {item.details}\n\n"
            )

        return output

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        db.close()


@tool
def summarize_interactions():
    """
    Summarize all CRM interactions.
    """

    db = SessionLocal()

    try:
        interactions = db.query(Interaction).all()

        if not interactions:
            return "No interactions found."

        return (
            f"CRM currently contains "
            f"{len(interactions)} interaction(s)."
        )

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        db.close()