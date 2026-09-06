import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Float, Boolean, DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class DBDemandSignal(Base):
    __tablename__ = "demand_signals"

    signal_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source = Column(String, nullable=False)
    source_id = Column(String, nullable=False)
    raw_text = Column(Text, nullable=False)
    url = Column(String, nullable=True)
    author_reference = Column(String, nullable=True)
    country = Column(String, default="US")
    language = Column(String, default="en")
    timestamp = Column(DateTime, default=datetime.utcnow)
    fingerprint = Column(String, index=True, nullable=True)
    extra_metadata = Column(JSON, default=dict)

    intents = relationship("DBPurchaseIntent", back_populates="signal", cascade="all, delete-orphan")

class DBPurchaseIntent(Base):
    __tablename__ = "purchase_intents"

    intent_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    signal_id = Column(String, ForeignKey("demand_signals.signal_id"), nullable=False)
    intent_score = Column(Float, nullable=False)
    extracted_requirements = Column(JSON, nullable=False)
    qualified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    signal = relationship("DBDemandSignal", back_populates="intents")
    messages = relationship("DBOutreachMessage", back_populates="intent")

class DBProduct(Base):
    __tablename__ = "products"

    product_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    category = Column(String, nullable=True)
    specifications = Column(JSON, default=dict)

    offers = relationship("DBOffer", back_populates="product", cascade="all, delete-orphan")

class DBOffer(Base):
    __tablename__ = "offers"

    offer_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = Column(String, ForeignKey("products.product_id"), nullable=False)
    merchant = Column(String, nullable=False)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String, default="USD")
    in_stock = Column(Boolean, default=True)
    seller = Column(String, nullable=True)
    shipping_destination = Column(String, nullable=True)
    shipping_cost = Column(Float, default=0.0)
    rating = Column(Float, nullable=True)
    affiliate_url = Column(Text, nullable=False)
    commission_rate = Column(Float, default=0.0)
    rank_score = Column(Float, nullable=True)
    verified = Column(Boolean, default=False)

    product = relationship("DBProduct", back_populates="offers")

class DBContact(Base):
    __tablename__ = "contacts"

    contact_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source = Column(String, nullable=False)
    author_reference = Column(String, nullable=False)
    channel = Column(String, nullable=False)
    permission_granted = Column(Boolean, default=False)
    opted_out = Column(Boolean, default=False)
    last_contacted_at = Column(DateTime, nullable=True)

    messages = relationship("DBOutreachMessage", back_populates="contact")

class DBOutreachMessage(Base):
    __tablename__ = "outreach_messages"

    message_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    intent_id = Column(String, ForeignKey("purchase_intents.intent_id"), nullable=False)
    contact_id = Column(String, ForeignKey("contacts.contact_id"), nullable=False)
    message_type = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    response_received = Column(String, nullable=True)

    intent = relationship("DBPurchaseIntent", back_populates="messages")
    contact = relationship("DBContact", back_populates="messages")

class DBAnalyticsEvent(Base):
    __tablename__ = "analytics_events"

    event_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_type = Column(String, nullable=False)
    entity_id = Column(String, nullable=True)
    event_data = Column(JSON, default=dict)
    timestamp = Column(DateTime, default=datetime.utcnow)
