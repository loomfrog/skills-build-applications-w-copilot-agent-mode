from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

# Define models for teams, activities, leaderboard, and workouts
from django.conf import settings

User = get_user_model()

# Sample data
USERS = [
    {"username": "ironman", "email": "ironman@marvel.com", "team": "marvel"},
    {"username": "captainamerica", "email": "cap@marvel.com", "team": "marvel"},
    {"username": "batman", "email": "batman@dc.com", "team": "dc"},
    {"username": "superman", "email": "superman@dc.com", "team": "dc"},
]

TEAMS = [
    {"name": "marvel", "members": ["ironman", "captainamerica"]},
    {"name": "dc", "members": ["batman", "superman"]},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "run", "distance": 5},
    {"user": "batman", "activity": "cycle", "distance": 10},
]

LEADERBOARD = [
    {"user": "ironman", "points": 100},
    {"user": "batman", "points": 90},
]

WORKOUTS = [
    {"name": "Pushups", "description": "Do 20 pushups"},
    {"name": "Situps", "description": "Do 30 situps"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        db.users.insert_many(USERS)
        db.users.create_index("email", unique=True)
        # Insert teams
        db.teams.insert_many(TEAMS)
        # Insert activities
        db.activities.insert_many(ACTIVITIES)
        # Insert leaderboard
        db.leaderboard.insert_many(LEADERBOARD)
        # Insert workouts
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
