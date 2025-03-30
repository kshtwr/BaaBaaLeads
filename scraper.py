from googlesearch import search
from utils import guess_email_from_name, clean_name

def fallback_scrape_leads(company, role):
    query = f'site:linkedin.com/in "{company}" "{role}"'
    try:
        results = list(search(query, num_results=10))
    except Exception as e:
        print(f"Search error: {e}")
        return []

    leads = []
    for url in results:
        raw_name = url.split("/in/")[-1].replace("-", " ").split("/")[0].strip()
        name_guess = clean_name(raw_name)

        if not name_guess:
            continue

        domain = f"{company.lower().replace(' ', '')}.com"
        email_options = guess_email_from_name(name_guess, domain)

        leads.append({
            "Name": name_guess,
            "Company": company,
            "LinkedIn": url,
            "Best Email Guess": email_options[0],
            "Other Guesses": ", ".join(email_options),
        })

    return leads
