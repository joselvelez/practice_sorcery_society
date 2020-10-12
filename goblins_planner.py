# List of gamers attending game night
gamers = []

# Function to add gamers to gamers list. 
def add_gamer(gamer, gamers_list):
    if 'name' in gamer.keys() and 'availability' in gamer.keys():
        gamers_list.append(gamer)

kimberly = {'name': 'Kimberly Waner', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
    return {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0
    }
count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    best_day = ''
    max_day = 0
    for day in availability_table:
        if availability_table.get(day) > max_day:
            max_day = availability_table.get(day)
            best_day = day
    return best_day

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    gamers_avaiable = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            gamers_avaiable.append(gamer['name'])
    return gamers_avaiable

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = "{name}, {day_of_week}, {game}"

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, day_of_week=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")