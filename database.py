from sqlalchemy import create_engine, Column, Integer, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from decimal import Decimal

# Define the base for our ORM models
Base = declarative_base()

class RefundRecord(Base):
    """The database schema for storing refund calculations."""
    __tablename__ = "refund_history"
    
    id = Column(Integer, primary_key=True, index=True)
    refund_amount = Column(Numeric(10, 2))
    total_amount = Column(Numeric(10, 2))
    tax_paid = Column(Numeric(10, 2))
    calculated_refund = Column(Numeric(10, 2))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class TaxDatabase:
    """Encapsulates all database operations."""
    
    def __init__(self, db_url: str = "sqlite:///./tax_refunds.db"):
        # connect_args is specific to SQLite for multi-threaded FastAPI access
        self.engine = create_engine(db_url, connect_args={"check_same_thread": False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        # Create the tables if they don't exist
        Base.metadata.create_all(bind=self.engine)

    def save_result(self, refund_amount: Decimal, total_amount: Decimal, tax_paid: Decimal, result: Decimal):
        """Saves a calculation record to the database."""
        session = self.SessionLocal()
        try:
            record = RefundRecord(
                refund_amount=refund_amount,
                total_amount=total_amount,
                tax_paid=tax_paid,
                calculated_refund=result
            )
            session.add(record)
            session.commit()
            session.refresh(record)
            return record
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_history(self):
        """Retrieves history for the audit log."""
        session = self.SessionLocal()
        try:
            return session.query(RefundRecord).order_by(RefundRecord.id.desc()).all()
        finally:
            session.close()
