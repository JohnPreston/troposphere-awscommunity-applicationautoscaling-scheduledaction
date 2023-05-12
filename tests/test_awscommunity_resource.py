import pytest
from troposphere import Template

from troposphere_awscommunity_applicationautoscaling_scheduledaction import (
    ScalableTargetAction,
    ScheduledAction,
)


def test_valid_input():
    props: dict = {
        "ScheduledActionName": "cfn-testing-resource",
        "ServiceNamespace": "dynamodb",
        "ScalableDimension": "dynamodb:table:ReadCapacityUnits",
        "ScalableTargetAction": ScalableTargetAction(
            **{"MinCapacity": 1, "MaxCapacity": 4}
        ),
        "Schedule": "cron(5 2 ? * FRI)",
        "Timezone": "Europe/London",
        "ResourceId": "table/awscommunityscheduledactiontesttable",
    }
    tpl = Template()
    action = tpl.add_resource(ScheduledAction("MyAction", **props))
    tpl.to_dict()


def test_invalid_target_value():
    with pytest.raises(ValueError):
        ScalableTargetAction(**{"MinCapacity": -1, "MaxCapacity": 4}),


def test_invalid_target_value_type():
    with pytest.raises(TypeError):
        ScalableTargetAction(**{"MinCapacity": "1", "MaxCapacity": 4}),


def test_invalid_schedule():
    props: dict = {
        "ScheduledActionName": "cfn-testing-resource",
        "ServiceNamespace": "dynamodb",
        "ScalableDimension": "dynamodb:table:ReadCapacityUnits",
        "ScalableTargetAction": ScalableTargetAction(
            **{"MinCapacity": 1, "MaxCapacity": 4}
        ),
        "Schedule": "notvalid(5 2 ? * FRI)",
        "Timezone": "Europe/London",
        "ResourceId": "table/awscommunityscheduledactiontesttable",
    }
    tpl = Template()
    with pytest.raises(ValueError):
        action = tpl.add_resource(ScheduledAction("MyAction", **props))
        tpl.to_dict()


def test_invalid_schedule_type():
    props: dict = {
        "ScheduledActionName": "cfn-testing-resource",
        "ServiceNamespace": "dynamodb",
        "ScalableDimension": "dynamodb:table:ReadCapacityUnits",
        "ScalableTargetAction": ScalableTargetAction(
            **{"MinCapacity": 1, "MaxCapacity": 4}
        ),
        "Schedule": 42,
        "Timezone": "Europe/London",
        "ResourceId": "table/awscommunityscheduledactiontesttable",
    }
    tpl = Template()
    with pytest.raises(TypeError):
        action = tpl.add_resource(ScheduledAction("MyAction", **props))
        tpl.to_dict()
