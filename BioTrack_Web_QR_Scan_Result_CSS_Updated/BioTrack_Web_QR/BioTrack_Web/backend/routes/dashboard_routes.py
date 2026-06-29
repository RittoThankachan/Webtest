# ==========================================
# IMPORTS
# ==========================================

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from backend.database import get_db
from backend.models import Request

from datetime import date

# ==========================================
# ROUTER
# ==========================================

router = APIRouter()


# ==========================================
# KPI DATA
# ==========================================

@router.get("/api/dashboard")

def dashboard_data(
    db: Session = Depends(get_db)
):

    requests = (
    db.query(Request)
    .order_by(Request.id.desc())
    .all()
)

    open_calls = len([
        r for r in requests
        if r.status == "Open"
    ])

    in_progress = len([
        r for r in requests
        if r.status == "In Progress"
    ])

    awaiting_parts = len([
        r for r in requests
        if r.status == "Awaiting Parts"
    ])

    closed_today = len([
        r for r in requests
        if (
            r.status == "Closed"
            and
            r.fixed_datetime
            and
            r.fixed_datetime.date()
            == date.today()
        )
    ])

    closed_requests = [
        r for r in requests
        if r.final_downtime_hours
    ]

    avg_downtime = 0

    if closed_requests:

        avg_downtime = round(

            sum(
                r.final_downtime_hours
                for r in closed_requests
            )
            /
            len(closed_requests),

            2
        )

    recent_logs = []

    for r in requests[:10]:

        recent_logs.append({

            "ticket":
                r.ticket_number,

            "equipment":
                r.equipment_name,

            "department":
                r.department,

            "priority":
                r.priority,

            "status":
                r.status,

            "call_received":
                str(r.call_received_datetime)
                if r.call_received_datetime
                else None,

            "engineer_start":
                str(r.engineer_start_datetime)
                if r.engineer_start_datetime
                else None,

            "fixed_time":
                str(r.fixed_datetime)
                if r.fixed_datetime
                else None,

            "downtime":
                r.final_downtime_hours
        })

    return {

        "open_calls":
            open_calls,

        "closed_calls":
            len([
                r for r in requests
                if r.status == "Closed"
            ]),

        "today_calls":
            len([
                r for r in requests
                if (
                    r.call_received_datetime
                    and
                    r.call_received_datetime.date()
                    == date.today()
                )
            ]),

        "avg_downtime":
            avg_downtime,

        "recent_logs":
            recent_logs
    }
# ==========================================
# EDIT REQUEST
# ==========================================

@router.put("/api/requests/{ticket}/edit")
def edit_request(
    ticket: str,
    data: dict,
    db: Session = Depends(get_db)
):

    request = (
        db.query(Request)
        .filter(
            Request.ticket_number == ticket
        )
        .first()
    )

    if not request:

        return {
            "success": False,
            "message": "Request not found"
        }

    from datetime import datetime

    try:

        if data.get("call_received"):

            request.call_received_datetime = (
                datetime.strptime(
                    data["call_received"],
                    "%d-%m-%Y %I:%M %p"
                )
            )

        if data.get("engineer_start"):

            request.engineer_start_datetime = (
                datetime.strptime(
                    data["engineer_start"],
                    "%d-%m-%Y %I:%M %p"
                )
            )

        if data.get("fixed_time"):

            request.fixed_datetime = (
                datetime.strptime(
                    data["fixed_time"],
                    "%d-%m-%Y %I:%M %p"
                )
            )

        request.final_downtime_hours = (
            data.get(
                "downtime",
                request.final_downtime_hours
            )
        )

        db.commit()

        return {
            "success": True
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }   
# ==========================================
# EDIT REQUEST
# ==========================================

@router.put("/api/requests/{ticket}/edit")
def edit_request(
    ticket: str,
    data: dict,
    db: Session = Depends(get_db)
):

    request = (
        db.query(Request)
        .filter(
            Request.ticket_number == ticket
        )
        .first()
    )

    if not request:

        return {
            "success": False,
            "message": "Request not found"
        }

    from datetime import datetime

    try:

        if data.get("call_received"):

            request.call_received_datetime = (
                datetime.strptime(
                    data["call_received"],
                    "%d-%m-%Y %I:%M %p"
                )
            )

        if data.get("engineer_start"):

            request.engineer_start_datetime = (
                datetime.strptime(
                    data["engineer_start"],
                    "%d-%m-%Y %I:%M %p"
                )
            )

        if data.get("fixed_time"):

            request.fixed_datetime = (
                datetime.strptime(
                    data["fixed_time"],
                    "%d-%m-%Y %I:%M %p"
                )
            )

        request.final_downtime_hours = (
            data.get(
                "downtime",
                request.final_downtime_hours
            )
        )

        db.commit()

        return {
            "success": True
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }