from datetime import date
from typing import List

from dominate import tags, util

from data_layer import html_class_keys
from data_models.activity import Activity


def construct_activities(title: str, activities_data: List[Activity]) -> tags.div:
    activities = tags.div(cls=html_class_keys.ACTIVITIES)
    activities.add(tags.h2(title, cls=html_class_keys.ACTIVITIES_TITLE))
    activities_data = __sort_activities_on_starting_date(activities_data)
    for activity in activities_data:
        activities.add(__construct_activity(activity))
    return activities


def __construct_activity(activity_data: Activity) -> tags.div:
    activity = tags.div(cls=html_class_keys.ACTIVITY)
    activity.add(tags.h3(activity_data.title, cls=html_class_keys.ACTIVITY_TITLE))
    location = f"{activity_data.location}, {activity_data.city}"
    activity.add(tags.span(location, cls=html_class_keys.ACTIVITY_LOCATION))
    date_ = f"{__format_date(activity_data.start_date)} - {__format_date(activity_data.end_date)}"
    activity.add(tags.span(date_, cls=html_class_keys.ACTIVITY_DATE))
    activity.add(tags.span(activity_data.description, cls=html_class_keys.ACTIVITY_DESCRIPTION))
    activity.add(__construct_skills(activity_data.skills))
    return activity


def __sort_activities_on_starting_date(activities: List[Activity]) -> List[Activity]:
    activities_dict = {activity.start_date: activity for activity in activities}
    return [activities_dict[key] for key in sorted(activities_dict, reverse=True)]


def __construct_skills(skills_list: List[str]) -> tags.div:
    skills = tags.div(cls=html_class_keys.ACTIVITY_SKILLS)
    # skills.add(tags.div("Keywords:", cls=html_class_keys.SKILLS_TITLE))
    for skill in skills_list:
        skills.add(tags.div(skill, cls=html_class_keys.SKILL))
    return skills


def __format_date(date_: date) -> str:
    return date_.strftime("%B %Y")
