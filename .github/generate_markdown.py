import yaml

def fetch_yaml_local(yaml_path):
    with open(yaml_path, 'r') as file:
        return file.read()

def generate_markdown(yaml_path, markdown_path):
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    # Generate Markdown content from the YAML data
    markdown_content = f"# {data.get('name', 'Core Data Model')}\n\n"
    markdown_content += f"## Description\n\n{data.get('description', 'No description')}\n\n"

    for model in data.get('models', []):
        # Extract the model name and description
        model_name = model.get('name', 'Unnamed Model')
        model_description = model.get('description', 'No description')

        # Add a section header for the model
        markdown_content += f"## {model_name}\n\n"
        markdown_content += f"Model Description: {model_description}\n\n"

        # Add a table header for the model columns
        markdown_content += "| Name | Description |\n"
        markdown_content += "| ---- | ----------- |\n"

        # Loop through each column in the 'columns' section for the model
        for column in model.get('columns', []):
            # Extract the column name and description
            name = column.get('name', 'Unnamed')
            description = column.get('description', 'No description')
            # Add a table row with the column name and description
            markdown_content += f"| {name} | {description} |\n"

def write_markdown_local(markdown_path, markdown_content):
    # Write the generated Markdown content to the specified Markdown file
    with open(markdown_path, 'w') as markdown_file:
        markdown_file.write(markdown_content)

yaml_path = 'models/core/core_models.yml'
markdown_path = '/.github/output.md'

yaml_content = fetch_yaml_local(yaml_path)
markdown_content = generate_markdown(yaml_content)
write_markdown_local(markdown_path, markdown_content)
