import json
from models.vaccinator_organisations import vaccinator_organisations
from models.vaccinator_sites import vaccinator_sites
from models.vaccine_types import vaccine_types
from models.covid_vaccine_types import covid_vaccine_types
from models.flu_vaccine_types import flu_vaccine_types
from models.job_roles import job_roles
from models.consent_decision import consent_decision
from models.eligible_decision import eligible_decision
from models.vaccination_routes import vaccination_routes
from models.vaccinated_decision import vaccinated_decision
from models.vaccinating_clinicians import vaccinating_clinicians
from models.consent_types import consent_types
from tests.test_data.models.covid_eligibility_types import eligibility_types
from models.consenting_clinicians import consenting_clinicians
from models.assess_outcome_decisions import assessment_outcome
from models.assessing_clinicians import assessing_clinicians
from models.care_models import care_models
from models.prescribing_methods import prescribing_methods
from models.assess_vaccine_not_given_reasons import assessment_vaccine_not_given_reasons
from models.no_consent_reasons import no_consent_reasons
from models.no_vaccination_reasons import assessment_vaccine_not_given_reasons
from models.covid_eligibility_types import covid_eligibility_types
import random


def get_wrapped_index(index, length):
    if length == 0:
        return 0
    if index is None or index < 0 or index >= length:
        return random.randint(0, length - 1)
    return index

def get_eligibility_type(index):
    eligibility_types(get_wrapped_index(index, len(eligibility_types)))

def get_assessing_clinician(index):
    assessing_clinicians(get_wrapped_index(index, len(assessing_clinicians)))

def get_assessment_outcome(index):
    assessment_outcome(get_wrapped_index(index, len(assessment_outcome)))

def get_assess_vaccine_not_given_reason(index):
    assessment_vaccine_not_given_reasons(get_wrapped_index(index, len(assessment_vaccine_not_given_reasons)))

def get_consent_given_by(index):
    consent_types(get_wrapped_index(index, len(consent_types)))

def get_consenting_clinician(index):
    consenting_clinicians(get_wrapped_index(index, len(consenting_clinicians)))

def get_no_consent_reason(index):
    no_consent_reasons(get_wrapped_index(index, len(no_consent_reasons)))

def get_vaccination_type(index, vaccine_type):
    if vaccine_type.lower() == "covid-19":
        covid_vaccine_types(get_wrapped_index(index, len(covid_vaccine_types)))
    elif vaccine_type.lower() == "flu":
        flu_vaccine_types(get_wrapped_index(index, len(flu_vaccine_types)))

def get_vaccination_route(index):
    vaccination_routes(get_wrapped_index(index, len(vaccination_routes)))

def get_prescribing_method(index):
    prescribing_methods(get_wrapped_index(index, len(prescribing_methods)))

def get_vaccinator(index):
    vaccinating_clinicians(get_wrapped_index(index, len(vaccinating_clinicians)))

def get_vaccination_not_given_reason(index):
    assessment_vaccine_not_given_reasons(get_wrapped_index(index, len(assessment_vaccine_not_given_reasons)))

