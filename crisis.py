from typing import List


CRISIS_KEYWORDS: List[str] = [
    "suicidal","suicide", "Kill myself", "want to die", "hopeless", "worthless", "can't go on", "give up", "ending it all", "no reason to live"
    ]



SAFETY_MESSAGE = (
    "It sounds like you're goingh through a really tough time."
    "YOu're not alone, and there are people who want to help you and be with you."
    "Please consider reaching out to mental health professionals or contacting a helpline:\n\n"
    "**India:** 915XXXXXXX (iCall), 1800-XXX-XXXX (ABC Foundation)\n"
    "**USA:** 988 (Crisis Lifeline)\n\n"
    "**UK:** 116 123 (Samaritans)\n\n"
    "You matters the most. 💙 "
)


def contains_crisis_keywords(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)