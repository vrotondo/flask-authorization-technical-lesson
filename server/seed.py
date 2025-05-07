#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Document, User

fake = Faker()

with app.app_context():

    print("Deleting all records...")
    User.query.delete()
    Document.query.delete()

    fake = Faker()

    print("Creating users...")
    users = []
    usernames = []
    for i in range(25):

        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        
        usernames.append(username)

        user = User(username=username)
        users.append(user)

    db.session.add_all(users)

    print("Creating documents...")

    documents = []
    documents.append(Document(title="Meeting Notes - March 12",content="Finalized the Q2 roadmap. Action items: update onboarding guide, schedule stakeholder sync, and review vendor contract by next Friday."))
    documents.append(Document(title="Project Zeta Summary",content="Zeta aims to automate task routing using AI. MVP launch set for July. Initial feedback from beta users is positive, especially on UI responsiveness."))
    documents.append(Document(title="Daily Standup Log",content="Blocked on API integration due to missing auth tokens. Waiting on DevOps. Frontend progress: navbar done, dashboard page ~75 percent complete."))
    documents.append(Document(title="Research: Learning Styles",content="Students retain 30% more through visuals. Kinesthetic learning shows potential in hybrid courses. Recommend integrating interactive labs."))
    documents.append(Document(title="Bug Report - Login Issue",content="Users intermittently logged out after 10 mins. Suspected session expiry misconfiguration. Logs show token mismatch errors from auth service."))
    
    db.session.add_all(documents)

    print("Committing users and documents to db...")
    db.session.commit()
    print("Complete.")
