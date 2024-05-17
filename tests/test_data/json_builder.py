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
from models.no_vaccination_reasons import vaccine_not_given_reasons
import random

def initialize_and_write_to_json(filename):
    global data
    data = build_json()
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def update_and_write_to_json(filename, new_data):
    global data
    data.update(new_data)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def build_json(index, nhs_number, chosen_vaccine, eligible, consent, vaccinated, eligibility_assessment_date, vaccination_date, batch_number, batch_expiry_date, patient_name, patient_dob, patient_address):

    def get_wrapped_index(index, length):
        if length == 0:
            return 0
        if index > 1:
            return random.randint(0, length - 1)
        return index % length

    data = {
    "vaccinator_organisation": vaccinator_organisations[get_wrapped_index(index, len(vaccinator_organisations))],
    "vaccinator_site": vaccinator_sites[get_wrapped_index(index, len(vaccinator_sites))],
    "vaccinator_care_model": care_models[get_wrapped_index(index, len(care_models))],
    "nhs_number": nhs_number,
    "chosen_vaccine": chosen_vaccine,
    "chosen_vaccine_type": covid_vaccine_types[get_wrapped_index(index, len(covid_vaccine_types))],
    "eligible_decision": eligible_decision,
    "eligibility_type": eligibility_types[get_wrapped_index(index, len(eligibility_types))],
    "staff_role": job_roles[get_wrapped_index(index, len(job_roles))],
    "eligibility_assessing_clinician": assessing_clinicians[get_wrapped_index(index, len(assessing_clinicians))],
    "eligibility_assessment_date": eligibility_assessment_date,
    "eligibility_assessment_outcome": assessment_outcome[get_wrapped_index(index, len(assessment_outcome))],
    "eligibility_assessment_no_vaccine_given_reason": assessment_vaccine_not_given_reasons[get_wrapped_index(index, len(assessment_vaccine_not_given_reasons))],
    "assessment_comments": "Automated assessment comments " + eligibility_assessment_date + " " + eligibility_types[get_wrapped_index(index, len(eligibility_types))] + " "+ vaccine_types[get_wrapped_index(index, len(vaccine_types))],
    "consent_decision": consent_decision[get_wrapped_index(index, len(consent_decision))],
    "consent_given_by": consenting_clinicians[get_wrapped_index(index, len(consenting_clinicians))],
    "name_of_person_consenting": "consenting adult",
    "relationship_to_patient": "relative",
    "consent_clinician_details": consenting_clinicians[get_wrapped_index(index, len(consenting_clinicians))],
    "no_consent_reason": no_consent_reasons[get_wrapped_index(index, len(no_consent_reasons))],
    "vaccinated_decision": vaccinated_decision[get_wrapped_index(index, len(vaccinated_decision))],
    "vaccination_date": vaccination_date,
    "vaccine_type2": covid_vaccine_types[get_wrapped_index(index, len(covid_vaccine_types))],
    "vaccination_route": vaccination_routes[get_wrapped_index(index, len(vaccination_routes))],
    "batch_number": batch_number,
    "batch_number_to_select": batch_number + " - " + batch_expiry_date,
    "batch_expiry_date": batch_expiry_date,
    "dose_amount": "0.3 ml",
    "prescribing_method": prescribing_methods[get_wrapped_index(index, len(prescribing_methods))],
    "vaccinator": vaccinating_clinicians[get_wrapped_index(index, len(vaccinating_clinicians))],
    "no_vaccination_reason": vaccine_not_given_reasons[get_wrapped_index(index, len(vaccine_not_given_reasons))],
    "vaccination_comments": "Automated vaccination comments " + vaccination_date + " " + eligibility_types[get_wrapped_index(index, len(eligibility_types))] + " "+ vaccine_types[get_wrapped_index(index, len(vaccine_types))],
    "patient_name": patient_name,
    "date_of_birth": patient_dob,
    "address": patient_address
}

    if chosen_vaccine == "Flu":
        data.update({
        "chosen_vaccine_type": flu_vaccine_types[get_wrapped_index(index, len(flu_vaccine_types))],
        "vaccine_type2": flu_vaccine_types[get_wrapped_index(index, len(flu_vaccine_types))]
        })

    if eligible.lower() == "no":
        data.update({
        "eligible_decision": "No",
        })

    if consent.lower() == "no":
        data.update({
        "consent_decision": "No",
        })

    if vaccinated.lower() == "no":
        data.update({
        "vaccinated_decision": "No",
        })

    with open('vaccine_record.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(data)
