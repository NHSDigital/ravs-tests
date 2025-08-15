import json
from test_data.models.vaccinator_organisations import vaccinator_organisations
from test_data.models.vaccinator_sites import vaccinator_sites
from test_data.models.vaccine_types import vaccine_types
from test_data.models.covid_vaccine_types import covid_vaccine_types
from test_data.models.flu_vaccine_types import flu_vaccine_types
from test_data.models.rsv_vaccine_types import rsv_vaccine_types
from test_data.models.pertussis_vaccine_types import pertussis_vaccine_types
from test_data.models.mmr_vaccine_types import mmr_vaccine_types
from test_data.models.job_roles import job_roles
from test_data.models.consent_decision import consent_decision
from test_data.models.eligible_decision import eligible_decision
from test_data.models.vaccination_sites import vaccination_sites
from test_data.models.vaccinated_decision import vaccinated_decision
from test_data.models.vaccinating_clinicians_fhh39 import vaccinating_clinicians_fhh39
from test_data.models.vaccinating_clinicians_airevalley import vaccinating_clinicians_airevalley
from test_data.models.vaccinating_clinicians import vaccinating_clinicians
from test_data.models.consent_types import consent_types
from test_data.models.consent_types_streamlining import consent_types_streamlining
from test_data.models.consenting_clinicians import consenting_clinicians
from test_data.models.consenting_clinicians_fhh39 import consenting_clinicians_fhh39
from test_data.models.consenting_clinicians_airevalley import consenting_clinicians_airevalley
from test_data.models.assess_outcome_decisions import assessment_outcome
from test_data.models.assessing_clinicians_fhh39 import assessing_clinicians_fhh39
from test_data.models.assessing_clinicians_airevalley import assessing_clinicians_airevalley
from test_data.models.assessing_clinicians import assessing_clinicians
from test_data.models.vaccination_locations import vaccination_locations
from test_data.models.legal_mechanism import legal_mechanism
from test_data.models.assess_vaccine_not_given_reasons import assessment_vaccine_not_given_reasons
from test_data.models.no_consent_reasons import no_consent_reasons
from test_data.models.no_vaccination_reasons import assessment_vaccine_not_given_reasons
from test_data.models.covid_eligibility_types import covid_eligibility_types
from test_data.models.covid_new_eligibility_types import covid_new_eligibility_types
from test_data.models.flu_eligibility_types import flu_eligibility_types
from test_data.models.rsv_eligibility_types import rsv_eligibility_types
from test_data.models.pertussis_eligibility_types import pertussis_eligibility_types
from test_data.models.vaccine_type_dose_amounts import vaccine_type_dose_amounts
from test_data.models.vaccine_type_ampp_codes_and_pack_sizes import vaccine_type_ampp_codes_pack_sizes
from test_data.models.flu_vaccine_add_batch_radio_button_xpath_map import flu_vaccine_add_batch_radio_button_xpath_map
from test_data.models.covid_vaccine_add_batch_radio_button_xpath_map import covid_vaccine_add_batch_radio_button_xpath_map
from test_data.models.flu_vaccine_add_batch_radio_button_xpath_map import flu_vaccine_add_batch_radio_button_xpath_map
from test_data.models.covid_add_vaccine_check_box_xpath_map import covid_add_vaccine_check_box_xpath_map
from test_data.models.flu_add_vaccine_check_box_xpath_map import flu_add_vaccine_check_box_xpath_map
from test_data.models.covid_consent_vaccine_radio_button_xpath_map import covid_consent_vaccine_radio_button_xpath_map
from test_data.models.flu_consent_vaccine_radio_button_xpath_map import flu_consent_vaccine_radio_button_xpath_map
from test_data.models.rsv_consent_vaccine_radio_button_xpath_map import rsv_consent_vaccine_radio_button_xpath_map
from test_data.models.pertussis_consent_vaccine_radio_button_xpath_map import pertussis_consent_vaccine_radio_button_xpath_map
from test_data.models.flu_vaccine_radio_button_xpath_map import flu_vaccine_radio_button_xpath_map
from test_data.models.covid_vaccine_radio_button_xpath_map import covid_vaccine_radio_button_xpath_map
from test_data.models.user_permission_levels import permission_levels
import random

# def get_wrapped_index(index, length):
#     if length == 0:
#         return 0
#     try:
#         index = int(index)
#     except ValueError:
#         return get_random_index(length)
#     if index < 0 or index >= length:
#         return get_random_index(length)
#     return index

def get_wrapped_index(index, length):
    if length == 0:
        return 0
    try:
        index = int(index)
    except ValueError:
        return 0
    return index % length

def get_random_index(length):
    if length <= 0:
        return 0
    return random.randint(0, length - 1)

def get_eligibility_type(index, vaccine):
    if vaccine.lower() == "covid-19":
        index = get_wrapped_index(index, len(covid_eligibility_types))
        return covid_eligibility_types[index]
    elif vaccine.lower() == "flu":
        return flu_eligibility_types[get_wrapped_index(index, len(flu_eligibility_types))]
    elif "rsv" in vaccine.lower():
        return rsv_eligibility_types[get_wrapped_index(index, len(rsv_eligibility_types))]
    elif vaccine.lower() == "pertussis":
        return pertussis_eligibility_types[get_wrapped_index(index, len(pertussis_eligibility_types))]

def get_new_eligibility_type(index, vaccine):
    if vaccine.lower() == "covid-19":
        index = get_wrapped_index(index, len(covid_new_eligibility_types))
        return covid_new_eligibility_types[index]
    elif vaccine.lower() == "flu":
        return flu_eligibility_types[get_wrapped_index(index, len(flu_eligibility_types))]
    elif "rsv" in vaccine.lower():
        return rsv_eligibility_types[get_wrapped_index(index, len(rsv_eligibility_types))]
    elif vaccine.lower() == "pertussis":
        return pertussis_eligibility_types[get_wrapped_index(index, len(pertussis_eligibility_types))]

def get_assessing_clinician(index):
    return assessing_clinicians[get_wrapped_index(index, len(assessing_clinicians))]

def get_assessing_clinician_fhh39(index):
    return assessing_clinicians_fhh39[get_wrapped_index(index, len(assessing_clinicians_fhh39))]

def get_assessing_clinician_airevalley(index):
    return assessing_clinicians_airevalley[get_wrapped_index(index, len(assessing_clinicians_airevalley))]

def get_random_assessing_clinician():
    return assessing_clinicians[get_random_index(len(assessing_clinicians))]

def get_random_assessing_clinician_fhh39():
    return assessing_clinicians_fhh39[get_random_index(len(assessing_clinicians_fhh39))]

def get_staff_role(index):
    return job_roles[get_wrapped_index(index, len(job_roles))]

def get_assessment_outcome(index):
    return assessment_outcome[get_wrapped_index(index, len(assessment_outcome))]

def get_assess_vaccine_not_given_reason(index):
    return assessment_vaccine_not_given_reasons[get_wrapped_index(index, len(assessment_vaccine_not_given_reasons))]

def get_consent_given_by(index):
    return consent_types[get_wrapped_index(index, len(consent_types))]

def get_streamlining_consent_given_by(index):
    return consent_types_streamlining[get_wrapped_index(index, len(consent_types_streamlining))]

def get_consenting_clinician(index):
    return consenting_clinicians[get_wrapped_index(index, len(consenting_clinicians))]

def get_consenting_clinician_fhh39(index):
    return consenting_clinicians_fhh39[get_wrapped_index(index, len(consenting_clinicians_fhh39))]

def get_consenting_clinician_airevalley(index):
    return consenting_clinicians_airevalley[get_wrapped_index(index, len(consenting_clinicians_airevalley))]

def get_no_consent_reason(index):
    return no_consent_reasons[get_wrapped_index(index, len(no_consent_reasons))]

def get_vaccine_to_choose_from(index):
    return vaccine_types[index]

def get_vaccination_type(index, vaccine):
    if vaccine.lower() == "covid-19":
        return covid_vaccine_types[get_wrapped_index(index, len(covid_vaccine_types))]
    elif vaccine.lower() == "flu":
        return flu_vaccine_types[get_wrapped_index(index, len(flu_vaccine_types))]
    elif vaccine.lower() == "respiratory syncytial virus (rsv)":
        return rsv_vaccine_types[get_wrapped_index(index, len(rsv_vaccine_types))]
    elif vaccine.lower() == "pertussis":
        return pertussis_vaccine_types[get_wrapped_index(index, len(pertussis_vaccine_types))]
    elif vaccine.lower() == "mmr":
        return mmr_vaccine_types[get_wrapped_index(index, len(mmr_vaccine_types))]

def get_vaccination_site(index):
    return vaccination_sites[get_wrapped_index(index, len(vaccination_sites))]

def get_vaccination_location(index, vaccine):
    if vaccine.lower() == "respiratory syncytial virus (rsv)":
        return None
    if vaccine.lower() == "pertussis":
        return None
    if vaccine.lower() == "mmr":
        return None
    return vaccination_locations[get_wrapped_index(index, len(vaccination_locations))]

def get_legal_mechanism(index):
    return legal_mechanism[get_wrapped_index(index, len(legal_mechanism))]

def get_vaccinator(index):
    return vaccinating_clinicians[get_wrapped_index(index, len(vaccinating_clinicians))]

def get_vaccinator_fhh39(index):
    return vaccinating_clinicians_fhh39[get_wrapped_index(index, len(vaccinating_clinicians_fhh39))]

def get_vaccinator_airevalley(index):
    return vaccinating_clinicians_airevalley[get_wrapped_index(index, len(vaccinating_clinicians_airevalley))]

def get_vaccination_not_given_reason(index):
    return assessment_vaccine_not_given_reasons[get_wrapped_index(index, len(assessment_vaccine_not_given_reasons))]

def get_vaccine_dose_amount(vaccine_type):
    return vaccine_type_dose_amounts.get(vaccine_type, "Unknown vaccine type")

def get_vaccine_type_ampp_codes(vaccine_type):
    for vaccine in vaccine_type_ampp_codes_pack_sizes["vaccines"]:
        if vaccine["name"] == vaccine_type:
            return {
                "packSizes": vaccine["packSizes"]
            }
    return "Unknown vaccine type"

def get_random_vaccine_type_pack_size(vaccine_type):
    pack_sizes = get_vaccine_type_ampp_codes(vaccine_type)

    if isinstance(pack_sizes, dict) and "packSizes" in pack_sizes:
        pack_sizes_data = pack_sizes["packSizes"]

        print("pack_sizes_data type:", type(pack_sizes_data))
        print("pack_sizes_data content:", pack_sizes_data)

        if isinstance(pack_sizes_data, list) and pack_sizes_data:
            size_options = [item["size"] for item in pack_sizes_data if "size" in item]

            if size_options:
                return size_options[0] if len(size_options) == 1 else random.choice(size_options)
            else:
                print("Error: No valid 'size' values found in pack_sizes_data")
                return "Unknown pack size"
        else:
            print("Error: packSizes is not a list or is empty")
            return "Unknown pack size"
    else:
        print("Error: 'packSizes' key is missing in pack_sizes")
        return "Unknown pack size"

def get_vaccine_type_pack_size_by_index(index, vaccine_type):
    pack_sizes = get_vaccine_type_ampp_codes(vaccine_type)

    if isinstance(pack_sizes, dict) and "packSizes" in pack_sizes:
        pack_sizes_data = pack_sizes["packSizes"]

        print("pack_sizes_data type:", type(pack_sizes_data))
        print("pack_sizes_data content:", pack_sizes_data)

        if isinstance(pack_sizes_data, list) and pack_sizes_data:
            if(len(pack_sizes_data) < 2):
                print("Error: not enough packSizes")
                return None

            size_options = [item["size"] for item in pack_sizes_data if "size" in item]

            if size_options:
                wrapped_index = get_wrapped_index(index, len(size_options))
                return size_options[wrapped_index]
            else:
                print("Error: No valid 'size' values found in pack_sizes_data")
                return None
        else:
            print("Error: packSizes is not a list or is empty")
            return None
    else:
        print("Error: 'packSizes' key is missing in pack_sizes")
        return None


def get_flu_consent_vaccine_xpath(vaccine_type):
    return flu_consent_vaccine_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_rsv_consent_vaccine_xpath(vaccine_type):
    return rsv_consent_vaccine_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_pertussis_consent_vaccine_xpath(vaccine_type):
    return pertussis_consent_vaccine_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_covid_consent_vaccine_xpath(vaccine_type):
    return covid_consent_vaccine_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_flu_add_vaccine_checkbox_xpath(vaccine_type):
    return flu_add_vaccine_check_box_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_covid_add_vaccine_checkbox_xpath(vaccine_type):
    return covid_add_vaccine_check_box_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_flu_vaccine_add_batch_radio_button_xpath(vaccine_type):
    return flu_vaccine_add_batch_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_covid_vaccine_add_batch_radio_button_xpath(vaccine_type):
    return covid_vaccine_add_batch_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_flu_vaccine_xpath(vaccine_type):
    return flu_vaccine_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_covid_vaccine_xpath(vaccine_type):
    return covid_vaccine_radio_button_xpath_map.get(vaccine_type, "Unknown vaccine type")

def get_user_permission_level(index):
    return permission_levels[get_wrapped_index(index, len(permission_levels))]

def get_single_packsize_vaccines() -> list:
    return [
        vaccine["name"]
        for vaccine in vaccine_type_ampp_codes_pack_sizes["vaccines"]
        if len(vaccine["packSizes"]) == 1
    ]
