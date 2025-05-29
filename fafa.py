from datetime import datetime, timedelta
import pandas as pd

# Dettaglio settimanale per ciascuna certificazione
phases_detailed = [
    ("AZ-104 – Microsoft Azure Administrator", [
        "Gestione risorse, subscriptions, RBAC",
        "Reti virtuali, NSG, DNS",
        "Storage (Blob, File, lifecycle)",
        "VM, scaling set, dischi",
        "Monitoraggio, Log Analytics, Advisor",
        "Azure AD, identità, simulazione esame"
    ]),
    ("AWS Developer Associate (DVA-C02)", [
        "IAM, S3, EC2, Lambda base",
        "API Gateway, DynamoDB, Step Functions",
        "CloudWatch, X-Ray, EventBridge",
        "CodePipeline, CodeBuild, CICD",
        "Lab pratico: App Serverless",
        "Simulazione esame + ripasso"
    ]),
    ("AZ-400 – Azure DevOps Engineer Expert", [
        "Azure DevOps: repo, branching",
        "Azure Pipelines: YAML, task",
        "GitHub Actions + integrazione",
        "IaC con Bicep/Terraform",
        "KeyVault, Secrets, sicurezza",
        "Azure Monitor e App Insights",
        "CI/CD avanzato e testing",
        "Simulazione esame AZ-400"
    ]),
    ("AWS DevOps Engineer – Professional", [
        "CodePipeline, CodeDeploy, blue/green",
        "CloudFormation avanzato",
        "CloudWatch, CloudTrail",
        "Auto Scaling, ECS, Lambda",
        "Logging, auditing, alert",
        "IaC avanzata",
        "Cost optimization, security",
        "Simulazione esame AWS DevOps Pro"
    ])
]

# Generazione calendario settimanale
start_date = datetime(2025, 5, 20)
schedule = []
week_counter = 1

for phase, topics in phases_detailed:
    for topic in topics:
        week_start = start_date + timedelta(weeks=week_counter - 1)
        schedule.append({
            "Settimana": f"Settimana {week_counter}",
            "Data Inizio": week_start.strftime("%Y-%m-%d"),
            "Certificazione": phase,
            "Argomento": topic,
            "Completato (S/N)": ""
        })
        week_counter += 1

# Creazione Excel
df = pd.DataFrame(schedule)
df.to_excel("Piano_Studio_DevOps_AWS_Azure.xlsx", index=False)

print("📁 File Excel creato: Piano_Studio_DevOps_AWS_Azure.xlsx")
