from pyscript import document, when

CLUB_DETAILS = {
    "Chess Club": {
        "Description": "A club for chess enthusiasts of all skill levels.",
        "Meeting Time": "Every Wednesday 3:30-5:00 PM",
        "Location": "Room 405",
        "Advisor": "Mr. Santos",
        "Number of Members": 20,
        "Category": "Academic"
    },
    "Robotics Team": {
        "Description": "Design, build, and program robots for competition.",
        "Meeting Time": "Tuesdays & Thursdays 4:00-6:00 PM",
        "Location": "Engineering Lab (Room 101)",
        "Advisor": "Ms. Chen",
        "Number of Members": 15,
        "Category": "STEM"
    },
    "Art Appreciation": {
        "Description": "Exploring different art forms, techniques, and history.",
        "Meeting Time": "Every Friday 3:00-4:30 PM",
        "Location": "Art Studio (Room 205)",
        "Advisor": "Mrs. Lee",
        "Number of Members": 25,
        "Category": "Creative"
    },
    "Debate Club": {
        "Description": "Develop public speaking and critical thinking skills.",
        "Meeting Time": "Every Monday 3:30-5:30 PM",
        "Location": "Library Conference Room",
        "Advisor": "Mr. Davies",
        "Number of Members": 18,
        "Category": "Academic"
    }
}

club_select = document.getElementById("club-select")
display_area = document.getElementById("club-info-display")


def populate_dropdown():
    club_select.innerHTML = ""
    for club_name in CLUB_DETAILS:
        option = document.createElement("option")
        option.value = club_name
        option.textContent = club_name
        club_select.appendChild(option)

    club_select.value = "Chess Club"


def render_club_info():
    selected = club_select.value
    club = CLUB_DETAILS[selected]

    html = f"<span class='club-name-title'>{selected}</span>"

    for key, value in club.items():
        html += f"""
        <div class="detail-line">
            <span class="detail-key">{key}:</span> {value}
        </div>
        """

    display_area.innerHTML = html


# INITIAL LOAD
populate_dropdown()
render_club_info()


# ✅ THIS IS THE FIX
@when("click", "#show-info-button")
def show_info(event):
    render_club_info()
