# EXPERIMENT - 2
# KNOWLEDGE RESOLUTION : HEALTHCARE MANAGEMENT


# --------------------------------------------------
# KNOWLEDGE BASE - RULES
# --------------------------------------------------

knowledge_base = {

    "rules": [

        {
            "conditions": ["critical_condition"],
            "conclusion": "emergency_service_required",
            "decision": "Activate emergency services immediately"
        },

        {
            "conditions": ["doctor_unavailable"],
            "conclusion": "alternative_doctor_required",
            "decision": "Assign another available doctor"
        },

        {
            "conditions": ["appointment_cancelled"],
            "conclusion": "rescheduling_required",
            "decision": "Reschedule the patient appointment"
        },

        {
            "conditions": ["abnormal_test_result"],
            "conclusion": "further_evaluation_required",
            "decision": "Recommend further medical evaluation"
        },

        {
            "conditions": ["low_medicine_stock"],
            "conclusion": "restocking_required",
            "decision": "Generate medicine restocking alert"
        },

        {
            "conditions": ["specialist_required"],
            "conclusion": "specialist_referral_required",
            "decision": "Refer patient to the appropriate specialist"
        }
    ]
}


# --------------------------------------------------
# CURRENT HEALTHCARE SITUATION
# --------------------------------------------------

healthcare_situation = {

    "patient_name": "Rahul",

    "patient_age": 45,

    "condition": "critical",

    "doctor_available": False,

    "appointment_status": "scheduled",

    "test_result": "abnormal",

    "medicine_stock": "low",

    "specialist_required": True
}


# --------------------------------------------------
# CONVERT INPUT INTO FACTS
# --------------------------------------------------

facts = set()


if healthcare_situation["condition"] == "critical":
    facts.add("critical_condition")


if not healthcare_situation["doctor_available"]:
    facts.add("doctor_unavailable")


if healthcare_situation["appointment_status"] == "cancelled":
    facts.add("appointment_cancelled")


if healthcare_situation["test_result"] == "abnormal":
    facts.add("abnormal_test_result")


if healthcare_situation["medicine_stock"] == "low":
    facts.add("low_medicine_stock")


if healthcare_situation["specialist_required"]:
    facts.add("specialist_required")


# --------------------------------------------------
# KNOWLEDGE RESOLUTION FUNCTION
# --------------------------------------------------

def resolve_knowledge(facts, knowledge_base):

    derived_facts = set()
    decisions = []

    print("\nCurrent Healthcare Facts:")

    for fact in facts:
        print("-", fact)

    print("\nKnowledge Resolution:")

    for rule in knowledge_base["rules"]:

        conditions = set(rule["conditions"])

        if conditions.issubset(facts):

            derived_facts.add(rule["conclusion"])

            decisions.append(rule["decision"])

            print("\nRule Matched:")

            print(
                "IF",
                " AND ".join(rule["conditions"])
            )

            print(
                "THEN",
                rule["conclusion"]
            )

            print(
                "Decision:",
                rule["decision"]
            )

    return derived_facts, decisions


# --------------------------------------------------
# EXECUTE KNOWLEDGE RESOLUTION
# --------------------------------------------------

print("=" * 60)
print(" HEALTHCARE MANAGEMENT KNOWLEDGE RESOLUTION")
print("=" * 60)

print("\nPatient Name:",
      healthcare_situation["patient_name"])

print("Patient Age:",
      healthcare_situation["patient_age"])

print("Patient Condition:",
      healthcare_situation["condition"])

print("Doctor Available:",
      healthcare_situation["doctor_available"])

print("Appointment Status:",
      healthcare_situation["appointment_status"])

print("Medical Test Result:",
      healthcare_situation["test_result"])

print("Medicine Stock:",
      healthcare_situation["medicine_stock"])

print("Specialist Required:",
      healthcare_situation["specialist_required"])


derived_facts, decisions = resolve_knowledge(
    facts,
    knowledge_base
)


# --------------------------------------------------
# DISPLAY DERIVED KNOWLEDGE
# --------------------------------------------------

print("\n" + "=" * 60)
print("DERIVED KNOWLEDGE")
print("=" * 60)

for fact in derived_facts:
    print("-", fact)


# --------------------------------------------------
# DISPLAY FINAL DECISIONS
# --------------------------------------------------

print("\n" + "=" * 60)
print("HEALTHCARE MANAGEMENT DECISIONS")
print("=" * 60)

for decision in decisions:
    print("-", decision)


print("\n" + "=" * 60)
print("Knowledge resolution completed successfully.")
print("=" * 60)
