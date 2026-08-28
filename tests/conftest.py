from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def isolate_activities():
    original_activities = deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(original_activities)
