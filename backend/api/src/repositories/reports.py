from sqlalchemy.orm import Session
from api.src.models import Report, reports_enum


class RepoReports():
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_report(
        self,
        battery_level: float,
        remaining_points: dict | list,
        status_report: reports_enum
    ) -> Report:
        try:
            report = Report(
                battery_level=battery_level,
                remaining_points=remaining_points,
                status_report=status_report
            )
            self.db.add(report)
            self.db.commit()
            return report
        except:
            self.db.rollback()
            raise
