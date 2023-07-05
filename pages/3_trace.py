from requirements import *

def read_csv(filename):
    df = pd.read_csv(filename, sep=';')
    return df

def extract_coordinates(wkt_string):
    coordinates = []
    cleaned_wkt = wkt_string.replace('MULTILINESTRING ((', '').replace('))', '')
    line_strings = cleaned_wkt.split(', ')

    for line_string in line_strings:
        points = line_string.split(', ')
        for point in points:
            x, y = map(float, point.split(' '))
            coordinates.append((x, y))

    return coordinates

def create_coordinates_dict(coordinates):
    coordinates_dict = {i: coord for i, coord in enumerate(coordinates)}
    return coordinates_dict

def create_graph(coordinates_dict):
    graph = nx.Graph()

    for node_id, coordinates in coordinates_dict.items():
        graph.add_node(node_id, pos=coordinates)

    for i in range(len(coordinates_dict) - 1):
        graph.add_edge(i, i + 1)

    return graph

def plot_graph(graph):
    fig = plt.figure()
    nx.draw(graph, pos=nx.get_node_attributes(graph, 'pos'), with_labels=False, node_size=10, edge_color='red')
    st.pyplot(fig)

# Filename
filename = r'data\bdm_e_ls_kabel_202307051411.csv'

# Read the CSV file
df = read_csv(filename)

# Extract the WKT string
wkt_string = df['ligging_kaart'][0]

# Extract the coordinates from the WKT string
coordinates = extract_coordinates(wkt_string)

# Create a dictionary with IDs associated with each tuple
coordinates_dict = create_coordinates_dict(coordinates)

# Create a graph
graph = create_graph(coordinates_dict)

# Plot the graph
plot_graph(graph)


