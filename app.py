import dash
from dash import html
import flask
import yaml

requested_url = flask.request.host
print(f"Requested URL: {requested_url}")

app = dash.Dash(__name__)
server = app.server

# Load the company-specific configurations from the YAML file
with open('config.yaml') as config_file:
    company_configurations = yaml.safe_load(config_file)

# Define the Dash layout
app.layout = html.Div([
    html.Img(id="logo-image", src=""),
    html.H1("Welcome to the Dashboard!"),
    dash.dcc.Location(id="url", refresh=False),
])

# Update the logo image based on the requested URL
@app.callback(
    dash.dependencies.Output("logo-image", "src"),
    [dash.dependencies.Input("url", "pathname")]
)
def update_logo_image(pathname):
    # Get the requested URL
    requested_url = flask.request.host
    print(f"Requested URL: {requested_url}")

    # Determine the logo based on the requested URL
    logo_filename = company_configurations.get(requested_url, {}).get("logo", "default_logo.png")
    print(company_configurations)

    print(f"Logo filename: {logo_filename}")

    # Generate the logo image source path
    logo_path = f"{logo_filename}"

    return logo_path

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
