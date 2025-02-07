import streamlit as st
import random

# -------------------------
# RESET HELPER FUNCTION (for filters)
# -------------------------
def reset_champion_data():
    # Remove all keys that store champion lists and reroll counters.
    keys_to_remove = [key for key in st.session_state if key.startswith("champions_") or key.startswith("reroll_count_")]
    for key in keys_to_remove:
        del st.session_state[key]

# -------------------------
# FULL RESET FUNCTION (for the reset button)
# -------------------------
def reset_page():
    st.session_state.clear()
    st.experimental_rerun()

# -------------------------
# CUSTOM CSS (Tooltip, Dividers, and Small Number Input)
# -------------------------
st.markdown("""
    <style>
    /* Tooltip styles */
    .tooltip {
      position: relative;
      display: inline-block;
    }
    .tooltip .tooltiptext {
      visibility: hidden;
      width: 220px;
      background-color: #555;
      color: #fff;
      text-align: center;
      border-radius: 6px;
      padding: 5px;
      position: absolute;
      z-index: 1;
      bottom: 125%; /* Position above the icon */
      left: 50%;
      margin-left: -110px;
      opacity: 0;
      transition: opacity 0.3s;
      font-size: 0.9em;
    }
    .tooltip:hover .tooltiptext {
      visibility: visible;
      opacity: 1;
    }
    /* Style for the vertical divider */
    .vertical-divider {
      border-left: 2px solid #ccc;
      height: 100%;
      min-height: 300px;
      margin: auto;
    }
    /* Make number inputs smaller */
    input[type="number"] {
      width: 50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# -------------------------
# HELPER FUNCTION
# -------------------------
def get_random_champions(num_champions=3, exclude_unkillables=False):
    """Returns a list of random champions."""
    champions = [
        "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Ambessa", "Amumu", "Anivia", "Annie", "Aphelios",
        "Ashe", "Aurelion Sol", "Aurora", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar",
        "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko",
        "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar",
        "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna",
        "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin",
        "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "K'Sante", "LeBlanc",
        "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai",
        "Master Yi", "Mel", "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus",
        "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn",
        "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc",
        "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett",
        "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain",
        "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle",
        "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex",
        "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao",
        "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
    ]
    if exclude_unkillables:
        unkillables = ['Sion', "Dr. Mundo", "Cho'Gath", "Tahm Kench", "Nautilus", "Ornn", "Zac", "Rammus"]
        champions = [champ for champ in champions if champ not in unkillables]
    if num_champions > len(champions):
        num_champions = len(champions)
    return random.sample(champions, num_champions)

# -------------------------
# TITLE
# -------------------------
st.markdown("<h1 style='font-size: 30px; text-align: center;'>Champ Randomizer</h1>", unsafe_allow_html=True)

# -------------------------
# FILTER SECTION (Side by Side)
# -------------------------
# Each filter now has an on_change callback to reset champion data.
filter_col1, filter_col2, filter_col3 = st.columns(3)
with filter_col1:
    team_size = st.radio(
        "",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: f"{x}v{x}",
        key="filter_team_size",
        on_change=reset_champion_data
    )
with filter_col2:
    num_champs = st.number_input(
        "Champs/Summoner:",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        key="filter_num_champs",
        on_change=reset_champion_data
    )
with filter_col3:
    # Two sub-columns: one for the checkbox and one for the tooltip icon.
    checkbox_col, tooltip_col = st.columns([0.8, 0.2])
    with checkbox_col:
        exclude_unkillables = st.checkbox(
            "Exclude Unkillables",
            key="filter_exclude_unkillables",
            on_change=reset_champion_data
        )
    with tooltip_col:
        tooltip_html = '''
        <div class="tooltip">
          <span style="font-size: 1.2em; color: blue; cursor: pointer;">&#9432;</span>
          <span class="tooltiptext"> Sion, Dr. Mundo, Cho'Gath, Tahm Kench, Nautilus, Ornn, Zac, Rammus, Ksante</span>
        </div>
        '''
        st.markdown(tooltip_html, unsafe_allow_html=True)

# Insert a horizontal divider between filters and teams.
st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------
# TEAM INPUT SECTION
# -------------------------
# Create three columns: Team 1, Divider, and Team 2.
col1, divider, col2 = st.columns([1, 0.1, 1])
team1_names = []
team2_names = []
team1_placeholders = []  # Placeholders for champion outputs for Team 1
team2_placeholders = []  # Placeholders for champion outputs for Team 2

with col1:
    st.subheader("Team 1")
    for i in range(team_size):
        name = st.text_input("Summoner:", key=f"team1_player_{i}")
        team1_names.append(name)
        team1_placeholders.append(st.empty())

with col2:
    st.subheader("Team 2")
    for i in range(team_size):
        name = st.text_input("Summoner:", key=f"team2_player_{i}")
        team2_names.append(name)
        team2_placeholders.append(st.empty())

# Insert a horizontal divider between team inputs and the buttons.
st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------
# COMBINE PLAYERS & PLACEHOLDERS
# -------------------------
all_players = team1_names + team2_names
all_placeholders = team1_placeholders + team2_placeholders

# -------------------------
# BUTTONS: GENERATE CHAMPIONS & RESET PAGE (Side by Side)
# -------------------------
button_col1, button_col2, _ = st.columns([0.3,0.15,0.55])
with button_col1:
    if st.button("Generate Champions"):
        # Check if any summoner box is empty.
        if any(player_name.strip() == "" for player_name in all_players):
            st.error("Please enter a summoner name for all players.")
        else:
            for i, player_name in enumerate(all_players):
                # Generate and store the champions for this summoner.
                st.session_state[f"champions_{i}"] = get_random_champions(num_champs, exclude_unkillables)
                # Reset the reroll counter for each summoner.
                st.session_state[f"reroll_count_{i}"] = 0

with button_col2:
    if st.button("Reset"):
        reset_page()

# -------------------------
# DISPLAY CHAMPION LISTS WITH REROLL BUTTONS
# -------------------------
for i, player_name in enumerate(all_players):
    if player_name and f"champions_{i}" in st.session_state:
        container = all_placeholders[i]
        with container.container():
            # Create two columns: one for the champion list, one for the reroll button.
            col_list, col_button = st.columns([3, 1])
            with col_list:
                champion_list_md = "\n".join([f"- {champion}" for champion in st.session_state[f"champions_{i}"]])
                st.markdown(champion_list_md)
            with col_button:
                # Allow reroll only if the user hasn't rerolled yet.
                if st.session_state[f"reroll_count_{i}"] < 1:
                    if st.button("↻", key=f"reroll_{i}"):
                        st.session_state[f"champions_{i}"] = get_random_champions(num_champs, exclude_unkillables)
                        st.session_state[f"reroll_count_{i}"] += 1
            
