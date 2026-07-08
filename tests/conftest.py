import pytest
from fastapi.testclient import TestClient
from src.app import app


# Store original activities data
ORIGINAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join our competitive basketball team and compete in leagues",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn tennis skills and participate in friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["jessica@mergington.edu", "ryan@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["maya@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Join our orchestra and perform classical and modern music",
        "schedule": "Tuesdays and Fridays, 4:30 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["david@mergington.edu", "clara@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop argumentation and public speaking skills through competitive debate",
        "schedule": "Mondays and Thursdays, 3:30 PM - 4:45 PM",
        "max_participants": 20,
        "participants": ["sarah@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific principles through hands-on projects",
        "schedule": "Wednesdays, 4:00 PM - 5:15 PM",
        "max_participants": 22,
        "participants": ["marcus@mergington.edu", "anna@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """Provide a test client with fresh activity data for each test."""
    # Reset activities to original state
    from src import app as app_module
    app_module.activities.clear()
    app_module.activities.update(ORIGINAL_ACTIVITIES)
    
    return TestClient(app)
