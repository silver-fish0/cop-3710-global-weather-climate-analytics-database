import streamlit as st
import os
import sqlite3
import csv
print(os.path.abspath("weather.db"))

def get_connection():
    return sqlite3.connect("weather.db")

st.title("Global Weather & Climate Analytics")

menu = ["Station Elevations", "Station Values", "Querydates of Roles", "User Organizations", "Measurement Date Values"]
choice = st.sidebar.selectbox("Select Action", menu)

# --- STATION ELEVATIONS ---
if choice == "Station Elevations":
    st.write("### Search station names above a certain elevation ")
    elevation = st.text_input("Elevation: ")

    if st.button("Search"):	
        try:
            elevation=float(elevation)
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT w.StationName, l.Elevation FROM WeatherStation w JOIN Location l ON w.LocationID=l.LocationID WHERE l.Elevation != '' AND l.Elevation > ?", (elevation,))
            data = cur.fetchall()
            cur.close()
            conn.close()

            if data:
                st.table(data)
            else:
                st.info("No records found.")
        except Exception as e:
            st.error(f"Error: {e}")

# --- STATION VALUES ---
elif choice == "Station Values":
    st.write("### Search station names above a certain measurement value ")
    Svalue = st.text_input("Value: ")

    if st.button("Search"):	
        try:
            Svalue=float(Svalue)
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT w.StationName, d.Value FROM WeatherStation w JOIN DailyMeasurement d ON w.StationID=d.StationID WHERE d.Value != '' AND d.Value > ?", (Svalue,))
            data = cur.fetchall()
            cur.close()
            conn.close()

            if data:
                st.table(data)
            else:
                st.info("No records found.")
        except Exception as e:
                st.error(f"Error: {e}")

# --- QUERYDATES OF ROLES ---
elif choice == "Querydates of Roles":
    st.write("### Search query dates with a specific role ")
    role = st.text_input("Role: ")

    if st.button("Search"):	
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT u.Role, q.QueryDate FROM Users u JOIN UserQuery q ON u.UserID=q.UserID WHERE u.Role != '' AND u.Role = ?", (role,))
            data = cur.fetchall()
            cur.close()
            conn.close()

            if data:
                st.table(data)
            else:
                st.info("No records found.")
        except Exception as e:
                st.error(f"Error: {e}")

# --- USER ORGANIZATIONS ---
elif choice == "User Organizations":
    st.write("### Search userIDs with a specific organization ")
    organization = st.text_input("Organization: ")

    if st.button("Search"):	
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT UserID, Organization FROM Users WHERE Organization != '' AND Organization = ?", (organization,))
            data = cur.fetchall()
            cur.close()
            conn.close()

            if data:
                st.table(data)
            else:
                st.info("No records found.")
        except Exception as e:
            st.error(f"Error: {e}")

# --- MEASUREMENTDATE VALUES ---
elif choice == "Measurement Date Values":
    st.write("### Search measurement dates above a certain value ")
    Dvalue = st.text_input("Value: ")

    if st.button("Search"):	
        try:
            Dvalue=float(Dvalue)
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT MeasurementDate, Value FROM DailyMeasurement WHERE Value != '' AND Value > ?", (Dvalue,))
            data = cur.fetchall()
            cur.close()
            conn.close()

            if data:
                st.table(data)
            else:
                st.info("No records found.")
        except Exception as e:
                st.error(f"Error: {e}")