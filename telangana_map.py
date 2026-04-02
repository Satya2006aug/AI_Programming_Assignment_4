import matplotlib.pyplot as plt
import networkx as nx

# Telangana districts
districts = [
'Adilabad','Nirmal','Nizamabad','Kamareddy','Karimnagar',
'Peddapalli','Jagitial','Rajanna Sircilla','Medak','Sangareddy',
'Siddipet','Warangal','Hanamkonda','Mulugu','Bhadradri',
'Khammam','Mahabubabad','Jangaon','Yadadri','Nalgonda',
'Suryapet','Rangareddy','Hyderabad','Vikarabad','Medchal',
'Mahabubnagar','Nagarkurnool','Wanaparthy','Jogulamba',
'Narayanpet','Komaram Bheem','Mancherial','Jayashankar'
]

# CSP domain
colors = ['Pink','Green','Brown','Yellow']

# Adjacency constraints
neighbors = {

'Adilabad':['Nirmal','Komaram Bheem','Mancherial'],
'Nirmal':['Adilabad','Nizamabad'],
'Nizamabad':['Nirmal','Kamareddy'],
'Kamareddy':['Nizamabad','Medak'],
'Medak':['Kamareddy','Sangareddy','Siddipet'],
'Sangareddy':['Medak','Vikarabad','Rangareddy'],
'Vikarabad':['Sangareddy','Rangareddy'],
'Rangareddy':['Hyderabad','Medchal','Vikarabad'],
'Hyderabad':['Rangareddy','Medchal'],
'Medchal':['Hyderabad','Rangareddy'],

'Karimnagar':['Peddapalli','Jagitial','Rajanna Sircilla','Siddipet'],
'Peddapalli':['Karimnagar','Mancherial'],
'Jagitial':['Karimnagar'],
'Rajanna Sircilla':['Karimnagar'],
'Siddipet':['Medak','Karimnagar','Jangaon'],

'Warangal':['Hanamkonda','Mulugu'],
'Hanamkonda':['Warangal','Jangaon'],
'Mulugu':['Warangal'],
'Jangaon':['Siddipet','Hanamkonda'],

'Nalgonda':['Suryapet','Yadadri'],
'Suryapet':['Nalgonda'],
'Yadadri':['Nalgonda'],

'Mahabubnagar':['Narayanpet','Nagarkurnool'],
'Nagarkurnool':['Mahabubnagar','Wanaparthy'],
'Wanaparthy':['Nagarkurnool','Jogulamba'],
'Jogulamba':['Wanaparthy'],
'Narayanpet':['Mahabubnagar']
}

# -------- CSP --------

def is_valid(district, color, assignment):
    if district in neighbors:
        for neighbor in neighbors[district]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
    return True


def backtrack(assignment):

    # goal test
    if len(assignment) == len(districts):
        return assignment

    # select unassigned variable
    for district in districts:
        if district not in assignment:

            for color in colors:

                if is_valid(district, color, assignment):

                    assignment[district] = color

                    result = backtrack(assignment)

                    if result:
                        return result

                    del assignment[district]

            return None


solution = backtrack({})

print("\nTelangana District Coloring\n")

for d in solution:
    print(d,"->",solution[d])


# -------- GRAPH DISPLAY --------

G = nx.Graph()

for d in districts:
    G.add_node(d)

for d in neighbors:
    for n in neighbors[d]:
        G.add_edge(d,n)

node_colors = [solution[d] for d in G.nodes()]

plt.figure(figsize=(12,9))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=8,
    edge_color="black"
)

plt.title("Telangana District Map Coloring (CSP)")
plt.show()
