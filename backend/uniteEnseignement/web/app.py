from fastapi import FastAPI
import yaml

app  = FastAPI(
    debug=True,
    openapi_url="/openapi/uEs.json",
    docs_url="/docs/uEs"
)

with open("../oas.yaml", 'r') as file:
    oas_doc = yaml.safe_load(file)

app.openapi = lambda: oas_doc
