from celery import Celery
from os import environ
from degree_planner.dp.recommend import recommend
from degree_planner.dp.fulfill import get_optimized_fulfillment, get_group_fulfillment, get_fulfillment_details
from degree_planner.dp.requirement import Requirement

celery_broker = 'redis://redis-celery:6379/0'
celery_backend = 'redis://redis-celery:6379/1'
celery_app = Celery("celery_app", broker=celery_broker, backend=celery_backend)

celery_app.conf.update(
    task_serializer=environ.get('CELERY_TASK_SERIALIZER', 'pickle'),
    result_serializer=environ.get('CELERY_RESULT_SERIALIZER', 'pickle'),
    accept_content=environ.get('CELERY_ACCEPT_CONTENT', 'pickle').split(','),
    result_expires=60,
)

@celery_app.task()
def dp_recommend(taken_courses, catalog, requirements, custom_tags=None, specification_sets=None) -> dict:
    Requirement.specification_sets = specification_sets
    recommendation = recommend(taken_courses, catalog, requirements, custom_tags)
    return recommendation

@celery_app.task()
def dp_fulfill(taken_courses, requirements, forced_wildcard_resolutions=None, groups=None, return_all=False) -> dict:
    fulfillment = get_optimized_fulfillment(taken_courses, requirements, forced_wildcard_resolutions, groups, return_all)
    return fulfillment

@celery_app.task()
def dp_fulfill_groups(fulfillments, groups, forced_groupings=None) -> dict:
    ''' returns {'groups': , 'tally': }'''
    fulfillment_groups = get_group_fulfillment(fulfillments, groups, forced_groupings)
    return fulfillment_groups

@celery_app.task()
def dp_fulfill_details(all_courses, taken_courses, requirements) -> dict:
    ''' returns {'details_all_taken': , 'details_all_possible':} '''
    fulfillment_details = get_fulfillment_details(all_courses, taken_courses, requirements)
    return fulfillment_details
