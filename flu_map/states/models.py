from django.db import models
from django.contrib.localflavor.us.us_states import STATES_NORMALIZED


class Week(models.Model):
    """
    The list of all distinct weeks we're storing data on.
    """
    number = models.IntegerField()
    end_date = models.DateField()


class State(models.Model):
    """
    The list of all the distinct states we're storing data on.
    """
    name = models.CharField(max_length=200)
    website_name = models.CharField(max_length=200)
    website_url = models.CharField(max_length=500)

    def get_postal_code(self):
        return STATES_NORMALIZED.get(self.name.lower())


class ActivityLevel(models.Model):
    """
    A flu activity level for a particular state in a particular week.
    """
    week = models.ForeignKey(Week)
    state = models.ForeignKey(State)
    activity_level = models.IntegerField()

    ACTIVITY_LEVEL_LABELS = {
        0: 'Insufficient Data',
        1: 'Minimal',
        2: 'Minimal',
        3: 'Minimal',
        4: 'Low',
        5: 'Low',
        6: 'Moderate',
        7: 'Moderate',
        8: 'High',
        9: 'High',
        10: 'High',
    }
    
    def get_activity_level_label(self):
        return self.ACTIVITY_LEVEL_LABELS.get(self.activity_level)
    activity_level_label = property(get_activity_level_label)


