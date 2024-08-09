# Feature: Consent Feature

# consent_type_values = [
#     "5",  # Clinician decision to vaccinate following the Best Interests process of the Mental Capacity Act
#     "3",  # Consent given by Court Appointed Deputy
#     "4",  # Consent given by Independent Mental Capacity Advocate
#     "6",  # Consent given by person with lasting power of attorney for personal welfare
#     "2",  # Consent given by person with parental responsibility
#     "1"   # Informed consent given for treatment
# ]

# eligibility_values = [
#     "12",  # Individual has had CAR-T therapy or stem cell transplantation since receiving their last vaccination?
#     "11",  # Individual is a carer?
#     "3",   # Individual is a health care worker?
#     "10",  # Individual is a household contact of people with immunosuppression?
#     "4",   # Individual is a social care worker?
#     "8",   # Individual is clinically at risk?
#     "9",   # Individual is either homeless or lives in a closed setting such as residents of supported living accommodation?
#     "6",   # Individual is eligible due to pregnancy?
#     "5",   # Individual is eligible due to their age?
#     "7",   # Individual is immunosuppressed?
#     "1",   # Individual lives in a care home?
#     "2"    # Individual works in a care home?
# ]

# @consent
# Scenario: Consent page should be visible without vaccine selection
#   Given I am on the patient details page
#   When I click the choose vaccine button
#   Then the consent page should open

# @consent
# Scenario Outline: Choose vaccine type page should be visible
#   Given I am on the choose vaccine page
#   When I check the <vaccineType> vaccine checkbox
#   Then I should be able to continue to screen patient

# Examples:
# |vaccineType  |
# |covid        |
# |seasonal Flu |


# @consent
# Scenario Outline: Record consent, select consentType
#   Given I am on the Record consent page for covid vaccine
#   When I select, Yes they consent, radio button
#   And I select <consentType> from dropdown
#   Then name, relationship to patient and clinician questions should be displayed <isDisplayed>

# Examples:
# | consentType                                             | isDisplayed |
# | Clinician decision to vaccinate following the Best Interests process of the Mental Capacity Act | True        |
# | Consent given by Court Appointed Deputy                | True        |
# | Consent given by Independent Mental Capacity Advocate   | True        |
# | Consent given by person with lasting power of attorney for personal welfare | True        |
# | Consent given by person with parental responsibility   | True        |
# | Informed consent given for treatment                   | False       |
