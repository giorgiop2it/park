import streamlit as st
from datetime import datetime, timedelta

# Funzione per calcolare l'ora di uscita
def calcola_ora_uscita(entrance_time, break_start, break_end, work_hours=7, work_minutes=12, min_lunch_break=30):
    # Convertire tutto in datetime
    entrance_dt = datetime.combine(datetime.today(), entrance_time)
    break_start_dt = datetime.combine(datetime.today(), break_start)
    break_end_dt = datetime.combine(datetime.today(), break_end)

    # Calcolare pausa pranzo e verificarne la durata minima
    actual_lunch_break = break_end_dt - break_start_dt
    mandatory_lunch_break = timedelta(minutes=min_lunch_break)
    
    if actual_lunch_break < mandatory_lunch_break:
        extra_time = mandatory_lunch_break - actual_lunch_break
        break_end_dt += extra_time

    # Calcolare tempo totale lavorato al mattino e pausa pranzo
    work_duration = timedelta(hours=work_hours, minutes=work_minutes)
    afternoon_work_start = break_end_dt
    exit_time = afternoon_work_start + work_duration - (break_start_dt - entrance_dt)

    return exit_time

# Configurazione dell'app Streamlit
st.title("Calcolo Ora di Uscita Continuo")
st.write("Inserisci l'orario di ingresso e di uscita per la pausa pranzo, e il sistema calcolerà l'orario di uscita considerando un totale di 7 ore e 12 minuti lavorativi e una pausa pranzo obbligatoria di almeno 30 minuti.")

# Input orari
entrance_time = st.time_input("Orario di ingresso", value=datetime.strptime("09:00", "%H:%M").time())
break_start = st.time_input("Inizio pausa pranzo", value=datetime.strptime("12:00", "%H:%M").time())
break_end = st.time_input("Fine pausa pranzo", value=datetime.strptime("12:30", "%H:%M").time())

# Calcolo ora di uscita
if st.button("Calcola"):
    exit_time = calcola_ora_uscita(entrance_time, break_start, break_end)
    
    # Visualizzazione risultato
    st.success(f"L'ora di uscita è: {exit_time.time()}")


