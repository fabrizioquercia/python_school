from datetime import datetime, timedelta
import pandas as pd

# Definizione delle fasi di studio
phases = [
    ("AZ-104 – Microsoft Azure Administrator", 1, 2),
    ("AWS Developer Associate (DVA-C02)", 3, 4),
    ("AZ-400 – Azure DevOps Engineer Expert", 5, 7),
    ("AWS DevOps Engineer – Professional", 8, 10),
]

# Data di inizio studio
start_date = datetime(2025, 5, 20)
weeks_per_month = 4
schedule = []

# Generazione del calendario settimanale
week_counter = 1
for phase, start_month, end_month in phases:
    num_weeks = (end_month - start_month + 1) * weeks_per_month
    for i in range(num_weeks):
        week_start = start_date + timedelta(weeks=week_counter - 1)
        schedule.append({
            "Settimana": f"Settimana {week_counter}",
            "Data Inizio": week_start.strftime("%Y-%m-%d"),
            "Argomento": phase
        })
        week_counter += 1

# Creazione DataFrame e salvataggio in Excel
df_schedule = pd.DataFrame(schedule)
df_schedule.to_excel("Piano_Studio_DevOps_AWS_Azure.xlsx", index=False)

print("Foglio Excel creato: Piano_Studio_DevOps_AWS_Azure.xlsx")

