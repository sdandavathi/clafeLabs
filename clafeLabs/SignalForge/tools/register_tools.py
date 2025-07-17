#from openai._utils import function_to_openai_tool
from tools.get_ticker_data import get_ticker_data
from tools.analyze_technical_indicators import analyze_technical_indicators
from tools.analyze_sentiment import analyze_sentiment
from tools.detect_anomalies import detect_anomalies
from tools.smart_money_summary import smart_money_summary
from tools.get_macro_conditions import get_macro_conditions
from tools.summarize_insights import summarize_insights

# ✅ Tool functions used at runtime
def get_tool_function_map():
    return {
        "get_ticker_data": get_ticker_data,
        "analyze_technical_indicators": analyze_technical_indicators,
        "analyze_sentiment": analyze_sentiment,
        "detect_anomalies": detect_anomalies,
        "smart_money_summary": smart_money_summary,
        "get_macro_conditions": get_macro_conditions,
        "summarize_insights": summarize_insights
    }

# ✅ Tool schema definitions for OpenAI Assistant
def get_tool_definitions():
    return [
        {
            "type": "function",
            "function": {
                "name": "get_ticker_data",
                "description": "Get historical and recent ticker data for a stock symbol.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol (e.g., AAPL, TSLA)"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "analyze_technical_indicators",
                "description": "Perform technical analysis and generate signals based on indicators like RSI, MACD.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "analyze_sentiment",
                "description": "Analyze sentiment for a stock ticker using recent news.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "detect_anomalies",
                "description": "Detect volume-based trading anomalies for a given stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "smart_money_summary",
                "description": "Summarize institutional or unusual options activity for a stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_macro_conditions",
                "description": "Fetch current macroeconomic indicators affecting market sentiment.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "summarize_insights",
                "description": "Generate a summary of technical, macro, and sentiment signals to produce a Buy/Sell/Hold recommendation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        }
    ]