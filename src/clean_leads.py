import csv
from pathlib import Path


INPUT_FILE = Path("data/sample_leads.csv")
OUTPUT_FILE = Path("data/cleaned_leads.csv")

VALID_STATUSES = {
    "new": "New",
    "contacted": "Contacted",
    "qualified": "Qualified",
    "needs review": "Needs review",
}


def clean_text(value):
    """Remove unnecessary spaces from a text value."""
    return " ".join(value.strip().split())


def normalize_status(status):
    """Convert commercial statuses to a consistent format."""
    cleaned_status = clean_text(status).lower()
    return VALID_STATUSES.get(cleaned_status, "Needs review")


def clean_phone(phone):
    """Keep only digits and add the Mexican country prefix."""
    digits = "".join(character for character in phone if character.isdigit())

    if not digits:
        return ""

    if len(digits) == 10:
        return f"+52{digits}"

    if len(digits) == 12 and digits.startswith("52"):
        return f"+{digits}"

    return digits


def clean_lead(lead):
    """Clean one lead and identify missing contact information."""
    cleaned_lead = {
        key: clean_text(value)
        for key, value in lead.items()
    }

    cleaned_lead["phone"] = clean_phone(cleaned_lead["phone"])
    cleaned_lead["status"] = normalize_status(cleaned_lead["status"])

    missing_fields = []

    if not cleaned_lead["phone"]:
        missing_fields.append("phone")

    if not cleaned_lead["website"]:
        missing_fields.append("website")

    cleaned_lead["missing_fields"] = ", ".join(missing_fields)
    cleaned_lead["is_complete"] = "Yes" if not missing_fields else "No"

    return cleaned_lead


def main():
    """Read the sample data, clean it, and create a new CSV file."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    with INPUT_FILE.open("r", encoding="utf-8-sig", newline="") as input_file:
        reader = csv.DictReader(input_file)
        cleaned_leads = [clean_lead(lead) for lead in reader]

    if not cleaned_leads:
        print("No leads were found.")
        return

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(cleaned_leads[0].keys())

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_leads)

    print(f"Cleaned {len(cleaned_leads)} leads.")
    print(f"Output created at: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
