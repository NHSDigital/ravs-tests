import json
from models import vaccinator_sites, vaccinator_organisations, vaccine_types, covid_vaccine_types, flu_vaccine_types, job_roles, consent_decision, eligible_decision, vaccination_routes, vaccinated_decision, vaccinating_clinicians, consent_types, eligibility_types, consenting_clinicians, assess_outcome_decisions, assessing_clinicians, care_models, prescribing_methods

def build_json(index, nhs_number, chosen_vaccine):

    # Sequentially pick each value from the lists
    eligibility_assessing_clinician_index = 0
    consent_clinician_details_index = 0
    prescribing_method_index = 0
    eligibility_assessment_outcome_index = 0
    eligibility_assessment_no_vaccine_given_reason_index = 0
    def get_wrapped_index(index, length):
        if length == 0:
            return 0
        return index % length

    data = {
        "vaccinator_organisation": vaccinator_organisations[index],
        "vaccinator_site": vaccinator_sites[index],
        "vaccinator_care_model": care_models[index],
        "nhs_number": nhs_number,
        "chosen_vaccine": vaccine_types[index],
        "chosen_vaccine_type": covid_vaccine_types[index],
        "eligible_decision": eligible_decision,
        "eligibility_type": eligibility_types[index],
        "staff_role": job_roles[index],
        "eligibility_assessing_clinician": eligibility_assessing_clinician[eligibility_assessing_clinician_index],
        "eligibility_assessment_date": eligibility_assessment_date,
        "eligibility_assessment_outcome": eligibility_assessment_outcome[eligibility_assessment_outcome_index],
        "eligibility_assessment_no_vaccine_given_reason": eligibility_assessment_no_vaccine_given_reason[eligibility_assessment_no_vaccine_given_reason_index],
        "assessment_comments": assessment_comments,
        "consent_decision": consent_decision,
        "consent_given_by": consent_given_by,
        "name_of_person_consenting": name_of_person_consenting,
        "relationship_to_patient": relationship_to_patient,
        "consent_clinician_details": consent_clinician_details[consent_clinician_details_index],
        "no_consent_reason": no_consent_reason,
        "vaccinated_decision": vaccinated_decision,
        "vaccination_date": vaccination_date,
        "vaccine_type2": vaccine_type2,
        "vaccination_route": vaccination_route,
        "batch_number": batch_number,
        "batch_number_to_select": batch_number_to_select,
        "batch_expiry_date": batch_expiry_date,
        "dose_amount": dose_amount,
        "prescribing_method": prescribing_method[prescribing_method_index],
        "vaccinator": vaccinator,
        "no_vaccination_reason": no_vaccination_reason,
        "vaccination_comments": vaccination_comments,
        "patient_name": patient_name,
        "date_of_birth": date_of_birth,
        "address": address
    }

    # Update index for next value
    eligibility_assessing_clinician_index = (eligibility_assessing_clinician_index + 1) % len(eligibility_assessing_clinician)
    consent_clinician_details_index = (consent_clinician_details_index + 1) % len(consent_clinician_details)
    prescribing_method_index = (prescribing_method_index + 1) % len(prescribing_method)
    eligibility_assessment_outcome_index = (eligibility_assessment_outcome_index + 1) % len(eligibility_assessment_outcome)
    eligibility_assessment_no_vaccine_given_reason_index = (eligibility_assessment_no_vaccine_given_reason_index + 1) % len(eligibility_assessment_no_vaccine_given_reason)

    with open('vaccine_record.json', 'w') as f:
        json.dump(data, f, indent=4)
