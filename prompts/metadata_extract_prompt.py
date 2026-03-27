from src.core.classes import Prompt


metadata_extract_prompt = Prompt(
    version="1",
    model_name="gpt-4.1",
    model_type="foundation",
    variables={"query": ""},
    prompt_text="""
One user query will be provided. The query will be used to search a vector database for relevant fashion products.

Extract useful metadata filters from the query and return them as JSON.
Use only the following metadata keys:
- brand
- color
- category
- top_type
- bottom_type
- dupatta
- pattern
- shape
- neck
- sleeves
- length
- hemline
- top_fabric
- bottom_fabric
- dupatta_fabric
- occasion
- wash_care
- price

The following fields must use only these exact values when present:
- dupatta: ["With dupatta"]
- shape: ["A-line", "Anarkali", "Kaftan", "Pathani", "Straight"]
- top_type: ["Coat", "Kurta", "Kurti", "Shirt", "Sweater", "Sweatshirt", "T-shirt", "Top", "Tunic"]
- bottom_type: ["Capris", "Churidar", "Dhoti pants", "Joggers", "Leggings", "Palazzos", "Patiala", "Pyjamas", "Salwar", "Sharara", "Shorts", "Skirt", "Trousers"]
- occasion: ["Casual", "Daily", "Ethnic", "Festive", "Formal", "Fusion", "Maternity", "Outdoor", "Party", "Sports", "Traditional", "Western", "Work"]
- wash_care: ["Dry clean", "Hand wash", "Machine wash"]
- length: ["Above knee", "Ankle length", "Below knee", "Calf length", "Crop", "Cropped", "Floor length", "Knee length", "Longline", "Maxi", "Midi", "Mini", "Regular", "Three-fourth length"]
- hemline: ["Asymmetric", "Curved", "Dipped", "Flared", "Fringed", "Hem with toggle", "High-low", "Ribbed", "Straight", "Tulip"]

Rules:
- Return only valid JSON and nothing else.
- Always include all keys listed above, even if no value is found.
- All metadata values must be lists.
- If a field is not specified in the query, return an empty list for that field.
- The price field must always be an object with keys min and max.
- If there is no lower bound, use 0 for min.
- If there is no upper bound, use \"inf\" for max.
- If no price is mentioned, return \"price\": {{\"min\": 0, \"max\": \"inf\"}}.
- If the query mentions multiple valid values for one field, include all of them in the list.
- Do not infer unsupported values.
- Prefer precision over recall: only include a metadata value if it is clearly requested or strongly implied by the query.
- Fill `category` only when the query explicitly contains a category value or the product title clearly contains one canonical category value from the catalog.
- For `category`, use the canonical category phrase itself, not a composed phrase made from multiple attributes.
- Do not invent category values like "A-Line Skirt" or "Tailored Suede Jacket" if the canonical category is only "A-line" or "Tailored jacket".
- Examples:
  - "regular trousers" -> `"category": ["Regular trousers"]`
  - "A-Line Skirt" title with canonical category "A-line" -> `"category": ["A-line"]`
  - "Tailored Suede Jacket" title with canonical category "Tailored jacket" -> `"category": ["Tailored jacket"]`

Interpret price expressions like this:
- \"under 2000\", \"less than 2000\" -> {{\"min\": 0, \"max\": 2000}}
- \"above 1500\", \"more than 1500\" -> {{\"min\": 1500, \"max\": \"inf\"}}
- \"between 1000 and 3000\" -> {{\"min\": 1000, \"max\": 3000}}

User query:
{query}

Expected JSON format:

{{
  \"brand\": [],
  \"color\": [],
  \"category\": [],
  \"top_type\": [],
  \"bottom_type\": [],
  \"dupatta\": [],
  \"pattern\": [],
  \"shape\": [],
  \"neck\": [],
  \"sleeves\": [],
  \"length\": [],
  \"hemline\": [],
  \"top_fabric\": [],
  \"bottom_fabric\": [],
  \"dupatta_fabric\": [],
  \"occasion\": [],
  \"wash_care\": [],
  \"price\": {{\"min\": 0, \"max\": \"inf\"}}
}}
    """,
)
