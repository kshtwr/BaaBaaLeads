import re
import os
from nameparser import HumanName
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion import ChatCompletion
from openai import OpenAIError
from dotenv import load_dotenv

# Use env var or fallback
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def guess_email_from_name(name, company_domain):
    parts = name.lower().split()
    if len(parts) < 2:
        return [f"{parts[0]}@{company_domain}"]
    first, last = parts[0], parts[-1]
    return [
        f"{first}@{company_domain}",
        f"{first}.{last}@{company_domain}",
        f"{first[0]}{last}@{company_domain}",
        f"{last}@{company_domain}"
    ]

def validate_and_format_name(name):
    try:
        prompt = (
            f"Return only the properly capitalized, spell-checked version of this name with no numbers/symbols, if it is valid."
            f"If the name is not valid, return it exactly as you received it. "
            f"Do not add any extra words or formatting. Only return the name itself.\n\n"
            f"{name}"
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=10,
        )
        output = response.choices[0].message.content.strip()
        return output
    except OpenAIError as e:
        print(f"[OpenAI Error in name validation] {e}")
        return name  # fallback

def generate_message_draft(name, company, role, pitch):
    try:
        prompt = (
            f"Write a short, friendly cold outreach message to {name} at {company}. "
            f"Their role is likely related to '{role}'. Mention this pitch: '{pitch}'. "
            "Keep it professional and warm. End with a question inviting a reply."
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        print(f"[OpenAI Error in message generation] {e}")
        return f"Hi {name},\n\n{pitch}\n\nLooking forward to connecting!"

def cross_ref_gpt(name, company, target_role):
    try:
        prompt = (
            f"Evaluate whether someone called {name}, works as a {target_role}, at {company}."
            """If you are 100% sure that they work the person works there return just the number: 1.
            If you are 100% sure that they do not work there then return just the number: -1.
            Else return just the number: 0.""" 
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=1,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        print(f"Cross-referencing unavailable!")
        return 0
        

def score_lead(lead, target_role):
    score = 0
    email = lead.get("Best Email Guess", "")
    name = lead.get("Name", "") or ""
    company = lead.get("Company", "")
    linkedin = lead.get("LinkedIn", "")
    email_guesses = lead.get("Other Guesses", "")
    title = lead.get("Extracted Title", "")

    # Good email
    if "@" in email and not any(g in email for g in ["info@", "support@", "hello@", "contact@"]):
        score += 2
    else:
        score -= 1

    # Multiple guesses
    if "," in email_guesses:
        score += 1

    # Company in email
    if company.lower() in email.lower():
        score += 1

    # LinkedIn present
    if linkedin:
        score += 2

    # Target role match in title or name
    if target_role.lower() in (title + name).lower():
        score += 2

    # Name looks valid
    if len(name.split()) >= 2:
        score += 1

    # Penalize generic pages
    if any(x in name.lower() for x in ["business", "login", "profile"]):
        score -= 2

    # OpenAI Cross-check
    if int(cross_ref_gpt(name, company, target_role)) > 0:
        score += 3
    elif int(cross_ref_gpt(name, company, target_role)) < 0:
        score -= 1

    return score

def clean_name(raw_name):
    if not raw_name:
        return None
    cleaned = re.sub(r"\b[\da-f]{4,}\b", "", raw_name, flags=re.IGNORECASE)
    cleaned = cleaned.replace("-", " ").strip()
    banned_keywords = ["business", "company", "profile", "https", "login"]
    if any(keyword in cleaned.lower() for keyword in banned_keywords):
        return None
    if len(cleaned) < 2 or cleaned.lower().startswith("http"):
        return None
    name = HumanName(cleaned)
    full_name = f"{name.first} {name.last}".strip()
    full_name = validate_and_format_name(full_name)
    return full_name if full_name else None
