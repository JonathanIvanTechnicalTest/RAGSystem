import json

# Sample synthetic data extracted from the PDF
synthetic_data = [
    {"prompt": "What is the design of the Robot X2000?", "response": "The Robot X2000 has a humanoid design."},
    {"prompt": "What can the Robot X2000 do?", "response": "The Robot X2000 is capable of walking and talking."},
    {"prompt": "What is the battery capacity of the Robot X2000?", "response": "The Robot X2000 is equipped with a 1000mAh battery."},
    {"prompt": "How does the Robot X2000 recognize objects?", "response": "The Robot X2000 uses AI to recognize objects."},
    {"prompt": "What features does the Robot X2000 have?", "response": "The Robot X2000 is capable of walking, talking, and recognizing objects using AI."},
    {"prompt": "What is the power source for the Robot X2000?", "response": "The Robot X2000 uses a rechargeable 1000mAh battery."}
]

# Function to write the data to a JSONL file
def write_jsonl(data, filename="fine_tuning_data.jsonl"):
    with open(filename, 'w') as f:
        for item in data:
            json.dump(item, f)
            f.write("\n")

# Call the function to create the JSONL file
write_jsonl(synthetic_data)

print("Data has been written to fine_tuning_data.jsonl")
