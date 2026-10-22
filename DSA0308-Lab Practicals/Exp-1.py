import re

text = "I am Mani Varma from mumbai to chennai with flight number 12323"

if re.search(r"mumbai", text, re.IGNORECASE):
    text = re.sub(r"mumbai", "Kadapa", text, flags=re.IGNORECASE)

if re.search(r"chennai", text, re.IGNORECASE):
    text = re.sub(r"chennai", "tirupati", text, flags=re.IGNORECASE)

if re.search(r"\b\d{5}\b", text):
    text = re.sub(r"\b\d{5}\b", "77369", text)
print("Updated Text:", text)

