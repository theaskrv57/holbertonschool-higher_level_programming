#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    Parameters:
        template (str): The template string with placeholders.
        attendees (list): List of dictionaries with attendee information.
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders, use 'N/A' if value is missing or None
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        # Generate output file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
