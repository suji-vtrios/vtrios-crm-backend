from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import leads
from app.database import Base
from app.database import engine

from app.models import lead
from app.models import followup
from app.routes import followups
from app.models import student
from app.routes import students
from app.models import batch
from app.routes import batches
from app.models import user
from app.routes import auth
from app.routes import users
from app.routes import analytics
from app.routes import public
from app.routes import notifications
from app.routes import messages
from app.routes import templates
from app.routes import conversations
from app.routes import webhooks
from app.config import settings

from app.models.lead import Lead
from app.models.user import User
from app.models.course import Course
from app.models.batch import Batch
from app.models.student import Student
from app.models.notification import Notification
from app.models.message import Message
from app.models.template import Template
from app.models.conversation import Conversation
from app.routes import wati
from app.routes import meta_webhook


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vtrios CRM API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    settings.FRONTEND_URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    followups.router,
    prefix="/followups",
    tags=["Followups"]
)

@app.get("/")
def root():
    return {
        "message":
        "Vtrios CRM API Running"
    }

app.include_router(
    leads.router,
    prefix="/leads",
    tags=["Leads"]
)

app.include_router(
    students.router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    batches.router,
    prefix="/batches",
    tags=["Batches"]
)


app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["Analytics"]
)

app.include_router(
    public.router,
    prefix="/public",
    tags=["Public"]
)

app.include_router(
    notifications.router,
    prefix="/notifications",
    tags=["Notifications"]
)

app.include_router(
    messages.router,
    prefix="/messages",
    tags=["Messages"]
)

app.include_router(
    templates.router,
    prefix="/templates",
    tags=["Templates"]
)

app.include_router(
    conversations.router,
    prefix="/conversations",
    tags=["Conversations"]
)

app.include_router(
    webhooks.router,
    prefix="/webhooks",
    tags=["Webhooks"]
)

app.include_router(
    wati.router,
    prefix="/wati",
    tags=["WATI"]
)

app.include_router(
    meta_webhook.router,
    prefix="/meta",
    tags=["Meta"]
)