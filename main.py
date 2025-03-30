import streamlit as st
import pandas as pd
from scraper import fallback_scrape_leads
from utils import score_lead, generate_message_draft

st.title("🐐 BaaBaaLeads")
st.subheader("An AI-Driven LeadGen Tool")
st.write("Input a company and target role to instantly discover relevant leads with **verified LinkedIn links and smart email guesses**. Use **AI-powered scoring** to prioritize high-impact contacts, **sort/filter** to your desire, and download the results as a **ready-to-use CSV** — complete with **custom message drafts** for every lead!")

company = st.text_input("Company Name")
role = st.text_input("Target Role")
pitch = st.text_area("Your Outreach Pitch (used in Message drafts)")

if st.button("Generate Leads"):
    raw_leads = fallback_scrape_leads(company, role)

    if not raw_leads:
        st.warning("No leads found. Try adjusting your input.")
    else:
        leads = []
        for lead in raw_leads:
            try:
                # Add company to lead if missing
                if "Company" not in lead:
                    lead["Company"] = company

                lead["Lead Score"] = score_lead(lead, role)
                lead["Message Draft"] = generate_message_draft(
                    lead.get("Name", "there"), lead.get("Company", "a company"), role, pitch
                )
                leads.append(lead)
            except Exception as e:
                st.error(f"Error processing lead: {lead}\n{e}")

        # Save to session state
        st.session_state["leads"] = leads
        st.session_state["company"] = company
        st.session_state["role"] = role
        st.success("Leads generated! Adjust the slider below to filter them.")

# Display leads if present in session state
if "leads" in st.session_state:
    leads = st.session_state["leads"]
    df = pd.DataFrame(leads)
    min_score = st.slider("Minimum Lead Score", 0, 10, 0) #0 is set as default to make up for any scraping/parsing edge cases (trusting PageRank)
    df_filtered = df[df["Lead Score"] >= min_score]
    st.dataframe(df_filtered)
    st.download_button(
        "Download Leads CSV",
        df_filtered.to_csv(index=False),
        "leads.csv",
        "text/csv"
    )
