from behave import Given, When, Then
from app_bdd import incrementor


@Given('a new incrementor of size {stride}')
def given_incrementor(context, stride: str):
    context.incrementor1 = incrementor(int(stride))


@When('we increment {num}')
def when_increment(context, num: str):
    context.results = context.incrementor1(int(num))


@Then('we should see {results}')
def then_results(context, results: str):
    assert(context.results == int(results))
