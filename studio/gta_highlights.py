"""
GTA Clip AI - Gameplay Highlight Detector
Uses transcript text and timestamps to find possible highlights.
No external dependencies required.
"""

HIGHLIGHT_KEYWORDS = {
    "mission": [
        "mission complete", "mission passed",
        "mission completed", "objective complete"
    ],
    "chase": [
        "police chase", "wanted level",
        "police are after", "escape the police"
    ],
    "stunt": [
        "big jump", "stunt jump", "car flip",
        "vehicle jump", "crazy landing"
    ],
    "race": [
        "race won", "finished first",
        "new record", "race complete"
    ],
    "funny": [
        "that was funny", "what just happened",
        "unexpected", "that was crazy"
    ],
    "achievement": [
        "achievement unlocked", "trophy earned",
        "new achievement"
    ],
    "fail": [
        "mission failed", "race failed",
        "that went wrong"
    ]
}


def detect_gta_highlights(segments, min_score=1):
    """
    segments format:
    [
        {"start": 10, "end": 15, "text": "Mission complete"}
    ]
    """

    highlights = []

    for segment in segments:
        text = str(segment.get("text", "")).lower()
        matched_categories = []

        for category, keywords in HIGHLIGHT_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                matched_categories.append(category)

        if len(matched_categories) >= min_score:
            highlights.append({
                "start": float(segment.get("start", 0)),
                "end": float(segment.get("end", 0)),
                "text": segment.get("text", ""),
                "categories": matched_categories,
                "score": len(matched_categories)
            })

    return sorted(
        highlights,
        key=lambda item: item["score"],
        reverse=True
    )
