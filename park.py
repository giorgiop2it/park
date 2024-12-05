import streamlit as st
from datetime import datetime, timedelta

# Funzione per calcolare l'ora di uscita
def calcola_ora_uscita(entrance_1, exit_1, entrance_2, work_hours=7, work_minutes=12, min_lunch_break=30):
    # Calcolo del tempo lavorato al mattino
    work_morning = exit_1 - entrance_1

    # Calcolo della pausa pranzo
    lunch_break = entrance_2 - exit_1
    mandatory_lunch_break = timedelta(minutes=min_lunch_break)
    
    # Assicurarsi che la pausa pranzo sia di almeno 30 minuti
    if lunch_break < mandatory_lunch_break:
        extra_lunch_time = mandatory_lunch_break - lunch_break
        entrance_2 += extra_lunch_time

    # Calcolo del tempo residuo da lavorare al pomeriggio
    total_work_time = timedelta(hours=work_hours, minutes=work_minutes)
    remaining_work_time = total_work_time - work_morning

    # Calcolo dell'orario di uscita
    exit_time = entrance_2 + remaining_work_time
    return exit_time

# Configurazione dell'app Streamlit
st.title("Calcolo Ora di Uscita")
st.write("Inserisci i seguenti orari per calcolare l'orario di uscita considerando 7 ore e 12 minuti di lavoro e una pausa pranzo obbligatoria di almeno 30 minuti.")

# Input orari
entrance_1 = st.time_input("Orario di ingresso mattina", value=datetime.strptime("09:00", "%H:%M").time())
exit_1 = st.time_input("Orario di uscita mattina", value=datetime.strptime("12:00", "%H:%M").time())
entrance_2 = st.time_input("Orario di ingresso pomeriggio", value=datetime.strptime("12:30", "%H:%M").time())

# Calcolo ora di uscita
if st.button("Calcola"):
    entrance_1_dt = datetime.combine(datetime.today(), entrance_1)
    exit_1_dt = datetime.combine(datetime.today(), exit_1)
    entrance_2_dt = datetime.combine(datetime.today(), entrance_2)
    
    exit_time = calcola_ora_uscita(entrance_1_dt, exit_1_dt, entrance_2_dt)
    
    # Visualizzazione risultato
    st.success(f"L'ora di uscita è: {exit_time.time()}")

