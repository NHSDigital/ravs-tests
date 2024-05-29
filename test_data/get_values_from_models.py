import json
from test_data.models.vaccinator_organisations import vaccinator_organisations
from test_data.models.vaccinator_sites import vaccinator_sites
from test_data.models.vaccine_types import vaccine_types
from test_data.models.covid_vaccine_types import covid_vaccine_types
from test_data.models.flu_vaccine_types import flu_vaccine_types
from test_data.models.job_roles import job_roles
from test_data.models.consent_decision import consent_decision
from test_data.models.eligible_decision import eligible_decision
from test_data.models.vaccination_routes import vaccination_routes
from test_data.models.vaccinated_decision import vaccinated_decision
from test_data.models.vaccinating_clinicians import vaccinating_clinicians
from test_data.models.consent_types import consent_types
from test_data.models.consenting_clinicians import consenting_clinicians
from test_data.models.assess_outcome_decisions import assessment_outcome
from test_data.models.assessing_clinicians import assessing_clinicians
from test_data.models.care_models import care_models
from test_data.models.prescribing_methods import prescribing_methods
from test_data.models.assess_vaccine_not_given_reasons import assessment_vaccine_not_given_reasons
from test_data.models.no_consent_reasons import no_consent_reasons
from test_data.models.no_vaccination_reasons import assessment_vaccine_not_given_reasons
from test_data.models.covid_eligibility_types import covid_eligibility_types
from test_data.models.flu_eligibility_types import flu_eligibility_types
import random

def get_wrapped_index(index, length):
    if length == 0:
        return 0
    try:
        index = int(index)
    except ValueError:
        return 0
    if index < 0 or index >= length:
        return 0
    return index

def get_eligibility_type(index, vaccine):
    if vaccine.lower() == "covid-19":
        index = get_wrapped_index(index, len(covid_eligibility_types))
        return covid_eligibility_types[index]
    elif vaccine.lower() == "flu":
        return flu_eligibility_types[get_wrapped_index(index, len(flu_eligibility_types))]

def get_assessing_clinician(index):
    return assessing_clinicians[get_wrapped_index(index, len(assessing_clinicians))]

def get_staff_role(index):
    return job_roles[get_wrapped_index(index, len(job_roles))]

def get_assessment_outcome(index):
    return assessment_outcome[get_wrapped_index(index, len(assessment_outcome))]

def get_assess_vaccine_not_given_reason(index):
    return assessment_vaccine_not_given_reasons[get_wrapped_index(index, len(assessment_vaccine_not_given_reasons))]

def get_consent_given_by(index):
    return consent_types[get_wrapped_index(index, len(consent_types))]

def get_consenting_clinician(index):
    return consenting_clinicians[get_wrapped_index(index, len(consenting_clinicians))]

def get_no_consent_reason(index):
    return no_consent_reasons[get_wrapped_index(index, len(no_consent_reasons))]

def get_vaccination_type(index, vaccine):
    if vaccine.lower() == "covid-19":
        return covid_vaccine_types[get_wrapped_index(index, len(covid_vaccine_types))]
    elif vaccine.lower() == "flu":
        return flu_vaccine_types[get_wrapped_index(index, len(flu_vaccine_types))]

def get_vaccination_route(index):
    return vaccination_routes[get_wrapped_index(index, len(vaccination_routes))]

def get_prescribing_method(index):
    return prescribing_methods[get_wrapped_index(index, len(prescribing_methods))]

def get_vaccinator(index):
    return vaccinating_clinicians[get_wrapped_index(index, len(vaccinating_clinicians))]

def get_vaccination_not_given_reason(index):
    return assessment_vaccine_not_given_reasons[get_wrapped_index(index, len(assessment_vaccine_not_given_reasons))]

