### About this template

This template is used to show to use the Elastic APM library, for Python in this example, to send performance data, about our example web API, to an Elastic APM server and view that information in Kibana.

---

### To use this template clone it with cookiecutter:

1. Install the `cookiecutter` library if it isn't already installed:
   `pip3 install cookiecutter`

2. Use this cookiecutter template: `cookiecutter gh:andrewguest/cookiecutter-elastic-apm-python`

3. Answer the questions when prompted (example below):

| Prompt            | Explanation                                       |
| ----------------- | ------------------------------------------------- |
| `project_name []` | Name for this project.                            |
| `project_slug []` | Automatically formatted version of `project_name` |
| ``                |                                                   |

---

### Services:

| Service            | Port |
| ------------------ | ---- |
| Elastic APM server | 8200 |
| Elasticsearch      | 9200 |
| Kibana             | 5601 |
| FastAPI            | 7000 |
