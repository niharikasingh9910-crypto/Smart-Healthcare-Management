import json

# EXPERIMENT - 1
# KNOWLEDGE BASE : HEALTHCARE MANAGEMENT

knowledge_base = {
    "knowledge_base": {
        "domain": "Healthcare Management",

        "entities": {

            "patients": {
                "types": [
                    "adult",
                    "child",
                    "senior_citizen",
                    "emergency_patient"
                ]
            },

            "doctors": {
                "specializations": [
                    "cardiologist",
                    "neurologist",
                    "orthopedic",
                    "dermatologist",
                    "general_physician"
                ]
            },

            "hospitals": {
                "types": [
                    "government",
                    "private",
                    "specialty",
                    "multispecialty"
                ]
            },

            "appointments": {
                "types": [
                    "online",
                    "offline",
                    "emergency"
                ],

                "statuses": [
                    "scheduled",
                    "completed",
                    "cancelled",
                    "pending"
                ]
            },

            "medical_records": {
                "types": [
                    "diagnosis",
                    "prescription",
                    "medical_history",
                    "test_report"
                ]
            },

            "medicines": {
                "types": [
                    "tablet",
                    "capsule",
                    "syrup",
                    "injection"
                ]
            },

            "diagnostic_tests": {
                "types": [
                    "blood_test",
                    "x_ray",
                    "mri",
                    "ct_scan",
                    "ecg"
                ]
            },

            "emergency_services": {
                "types": [
                    "ambulance",
                    "emergency_department",
                    "critical_care"
                ]
            }
        },

        "relationships": [

            {
                "subject": "patient",
                "relationship": "books",
                "object": "appointment"
            },

            {
                "subject": "appointment",
                "relationship": "assigned_to",
                "object": "doctor"
            },

            {
                "subject": "doctor",
                "relationship": "works_at",
                "object": "hospital"
            },

            {
                "subject": "patient",
                "relationship": "has",
                "object": "medical_record"
            },

            {
                "subject": "doctor",
                "relationship": "prescribes",
                "object": "medicine"
            },

            {
                "subject": "patient",
                "relationship": "undergoes",
                "object": "diagnostic_test"
            },

            {
                "subject": "diagnostic_test",
                "relationship": "produces",
                "object": "test_report"
            },

            {
                "subject": "emergency_service",
                "relationship": "responds_to",
                "object": "patient"
            }
        ],

        "rules": [

            {
                "condition": "patient condition is critical",
                "conclusion": "activate emergency services immediately"
            },

            {
                "condition": "doctor is unavailable",
                "conclusion": "assign another available doctor"
            },

            {
                "condition": "appointment is cancelled",
                "conclusion": "reschedule appointment"
            },

            {
                "condition": "medical test result is abnormal",
                "conclusion": "recommend further medical evaluation"
            },

            {
                "condition": "medicine stock is low",
                "conclusion": "generate medicine restocking alert"
            },

            {
                "condition": "patient requires specialist",
                "conclusion": "refer patient to appropriate specialist"
            }
        ],

        "problems": [
            "Long patient waiting times",
            "Doctor unavailability",
            "Appointment cancellations",
            "Medicine shortages",
            "Emergency response delays",
            "Diagnostic test delays",
            "Lack of healthcare resources",
            "Incomplete medical records"
        ],

        "solutions": [
            "Online appointment scheduling",
            "Electronic health records",
            "Doctor scheduling system",
            "Medicine inventory management",
            "Emergency priority system",
            "Automated diagnostic reporting",
            "Healthcare resource optimization",
            "Real-time healthcare monitoring"
        ]
    }
}


# SAVE KNOWLEDGE BASE AS JSON FILE

with open("healthcare_management_knowledge_base.json", "w") as file:
    json.dump(knowledge_base, file, indent=4)


# RETRIEVE KNOWLEDGE BASE

kb = knowledge_base["knowledge_base"]


# DISPLAY KNOWLEDGE BASE

print("=" * 60)
print(" HEALTHCARE MANAGEMENT KNOWLEDGE BASE")
print("=" * 60)


# Entities

print("\nEntities are:")
print(", ".join(kb["entities"].keys()))


# Entity Details

print("\nPatient Types are:")
print(", ".join(kb["entities"]["patients"]["types"]))

print("\nDoctor Specializations are:")
print(", ".join(kb["entities"]["doctors"]["specializations"]))

print("\nHospital Types are:")
print(", ".join(kb["entities"]["hospitals"]["types"]))

print("\nAppointment Types are:")
print(", ".join(kb["entities"]["appointments"]["types"]))

print("\nAppointment Statuses are:")
print(", ".join(kb["entities"]["appointments"]["statuses"]))

print("\nMedical Record Types are:")
print(", ".join(kb["entities"]["medical_records"]["types"]))

print("\nMedicine Types are:")
print(", ".join(kb["entities"]["medicines"]["types"]))

print("\nDiagnostic Test Types are:")
print(", ".join(kb["entities"]["diagnostic_tests"]["types"]))

print("\nEmergency Services are:")
print(", ".join(kb["entities"]["emergency_services"]["types"]))


# Relationships

print("\nRelationships are:")

for relation in kb["relationships"]:
    print(
        relation["subject"],
        "->",
        relation["relationship"],
        "->",
        relation["object"]
    )


# Rules

print("\nRules are:")

for i, rule in enumerate(kb["rules"], 1):
    print(
        f"{i}. IF {rule['condition']} "
        f"THEN {rule['conclusion']}"
    )


# Problems

print("\nProblems are:")

for problem in kb["problems"]:
    print("-", problem)


# Solutions

print("\nSolutions are:")

for solution in kb["solutions"]:
    print("-", solution)


print("\n" + "=" * 60)
print("Knowledge Base successfully created.")
print("JSON file: healthcare_management_knowledge_base.json")
print("=" * 60)
