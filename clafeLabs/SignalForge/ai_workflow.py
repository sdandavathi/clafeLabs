import openai
import os
from dotenv import load_dotenv
from tools.register_tools import get_tool_definitions
from tools.register_tools import get_tool_function_map
# from tools import logic  # ❌ Removed invalid import

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print("🔑 OpenAI API Key loaded.")
client = openai.OpenAI()


from openai.types.beta.threads import Run

def run_stock_workflow(ticker):
    print(f"🌀 Running analysis for: {ticker}")

    assistant = client.beta.assistants.create(
        name="Stock Signal Generator",
        instructions="Use tools to analyze ticker and recommend Buy, Sell, or Hold signal based on multiple signals. Return JSON with keys: signal, confidence, reason.",
        tools=get_tool_definitions(),
        model="gpt-4o"
    )

    tool_func_map = get_tool_function_map()
    data = {}

    for name, func in tool_func_map.items():
        if name == "summarize_insights":
            continue
        print(f"🔧 Running tool: {name}...")
        try:
            if name == "get_macro_conditions":
                result = func()
            else:
                result = func(ticker=ticker)
            data[name] = result
            print(f"✅ Output from {name}: {result}")
        except Exception as e:
            data[name] = {"error": str(e)}
            print(f"❌ Error in {name}: {e}")

    thread = client.beta.threads.create()
    print("✅ Thread created:", thread.id)

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"Here are the tool outputs for {ticker}. Please summarize the insights and recommend Buy/Sell/Hold."
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        if run.status == "completed":
            break
        elif run.status == "requires_action":
            print("🛠 Assistant requires action: calling tools...")
            tool_outputs = []
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                tool_name = tool_call.function.name
                tool_call_id = tool_call.id
                result = str(data.get(tool_name, {"error": "Tool not executed"}))
                tool_outputs.append({
                    "tool_call_id": tool_call_id,
                    "output": result
                })

            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )
        elif run.status in ["failed", "cancelled", "expired"]:
            print("❌ Run failed with status:", run.status)
            return {"error": f"Run failed with status: {run.status}"}

    messages = client.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value

if __name__ == "__main__":
    import sys

    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    print(f"\n🔍 Running stock signal workflow for: {ticker}\n")
    result = run_stock_workflow(ticker)
    print("\n📤 Final Result:\n", result)