# Telangana Map Coloring using CSP (Backtracking)

# List of districts
districts = [
    "Adilabad","Komaram Bheem","Nirmal","Mancherial","Nizamabad","Jagitial",
    "Peddapalli","Jayashankar","Bhadradri","Mulugu","Warangal Urban",
    "Warangal Rural","Jangaon","Mahabubabad","Khammam","Karimnagar",
    "Rajanna Sircilla","Kamareddy","Medak","Siddipet","Sangareddy",
    "Vikarabad","Hyderabad","Medchal","Rangareddy","Yadadri","Suryapet",
    "Nalgonda","Mahabubnagar","Narayanpet","Wanaparthy","Nagarkurnool",
    "Jogulamba Gadwal"
]

# Available colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Adjacency constraints
neighbors = {
    "Adilabad": ["Komaram Bheem","Nirmal"],
    "Komaram Bheem": ["Adilabad","Mancherial","Nirmal"],
    "Nirmal": ["Adilabad","Komaram Bheem","Nizamabad","Jagitial"],
    "Mancherial": ["Komaram Bheem","Jagitial","Peddapalli"],
    "Nizamabad": ["Nirmal","Kamareddy","Jagitial"],
    "Jagitial": ["Nirmal","Mancherial","Karimnagar","Rajanna Sircilla"],
    "Peddapalli": ["Mancherial","Karimnagar","Jayashankar"],
    "Jayashankar": ["Peddapalli","Mulugu","Bhadradri"],
    "Bhadradri": ["Jayashankar","Mulugu","Khammam"],
    "Mulugu": ["Jayashankar","Bhadradri","Warangal Rural"],
    "Warangal Urban": ["Warangal Rural","Jangaon","Karimnagar"],
    "Warangal Rural": ["Mulugu","Warangal Urban","Jangaon"],
    "Jangaon": ["Warangal Urban","Warangal Rural","Yadadri","Siddipet"],
    "Mahabubabad": ["Warangal Rural","Khammam","Jangaon"],
    "Khammam": ["Bhadradri","Mahabubabad","Suryapet"],
    "Karimnagar": ["Jagitial","Peddapalli","Warangal Urban","Rajanna Sircilla"],
    "Rajanna Sircilla": ["Karimnagar","Jagitial","Siddipet"],
    "Kamareddy": ["Nizamabad","Medak","Siddipet"],
    "Medak": ["Kamareddy","Sangareddy","Siddipet"],
    "Siddipet": ["Medak","Rajanna Sircilla","Jangaon","Yadadri"],
    "Sangareddy": ["Medak","Vikarabad","Medchal"],
    "Vikarabad": ["Sangareddy","Rangareddy"],
    "Hyderabad": ["Medchal","Rangareddy"],
    "Medchal": ["Hyderabad","Sangareddy","Rangareddy"],
    "Rangareddy": ["Vikarabad","Hyderabad","Medchal","Mahabubnagar"],
    "Yadadri": ["Jangaon","Siddipet","Nalgonda"],
    "Suryapet": ["Khammam","Nalgonda"],
    "Nalgonda": ["Yadadri","Suryapet","Mahabubnagar"],
    "Mahabubnagar": ["Rangareddy","Narayanpet","Wanaparthy","Nagarkurnool"],
    "Narayanpet": ["Mahabubnagar"],
    "Wanaparthy": ["Mahabubnagar","Nagarkurnool"],
    "Nagarkurnool": ["Mahabubnagar","Wanaparthy","Jogulamba Gadwal"],
    "Jogulamba Gadwal": ["Nagarkurnool"]
}

# Check if assignment is valid
def is_valid(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Select unassigned variable (simple version)
def select_unassigned(assignment):
    for d in districts:
        if d not in assignment:
            return d

# Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    district = select_unassigned(assignment)

    for color in colors:
        if is_valid(district, color, assignment):
            assignment[district] = color

            result = backtrack(assignment)
            if result:
                return result

            # Backtrack
            del assignment[district]

    return None

# Solve the CSP
solution = backtrack({})

# Print solution neatly
print("Telangana Map Coloring Solution:\n")
for district in sorted(solution):
    print(f"{district:20} -> {solution[district]}")
