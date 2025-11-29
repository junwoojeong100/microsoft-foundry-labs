# Azure AI Foundry Agent Invocation using Activity Protocol
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# TODO: Update these values with your actual Azure AI Foundry details
# Get these from: https://ai.azure.com → Your Project → Deployments
FOUNDRY_ENDPOINT = "https://foundry-junwoo.services.ai.azure.com/api/projects/proj-default"
AGENT_NAME = "ModelRouterAgent"
API_VERSION = "2025-11-15-preview"

# Create OpenAI client with Azure authentication
client = OpenAI(
    api_key=get_bearer_token_provider(
        DefaultAzureCredential(), 
        "https://ai.azure.com/.default"
    ),
    base_url=f"{FOUNDRY_ENDPOINT}/applications/{AGENT_NAME}/protocols/openai",
    default_query={"api-version": API_VERSION}
)

try:
    # Call the agent using responses API
    response = client.responses.create(
        input="제주도 2박 3일 여행 코스 추천해줘"
    )
    
    print(f"Response: {response.output_text}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\n🔍 Troubleshooting:")
    print("1. Check your endpoint URL at https://ai.azure.com")
    print("2. Verify the project name and agent name exist")
    print("3. Ensure you're logged in: az login")
    print("4. Confirm the agent is deployed and running")

