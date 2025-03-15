

---

## **Multi-Agent Web Retrieval System**  
A multi-agent Retrieval-Augmented Generation (RAG) system that integrates **Google Gemini 1.5 Pro**, **Tavily Search API**, and **LangGraph** to retrieve, fact-check, and summarize information from the web.  

### **📌 Features**
- **Web Search Agent**: Uses **Tavily Search API** to fetch relevant web pages.  
- **Fact-Checking Agent**: Validates retrieved information before summarization.  
- **Summarization Agent**: Generates concise summaries using **Google Gemini 1.5 Pro**.  
- **Multi-Agent Workflow**: Built using **LangGraph & LangChain** for structured execution.  

---

## **🚀 Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/multi-agent-rag.git
cd multi-agent-rag
```

### **2️⃣ Create and Activate Virtual Environment**
```sh
# On Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **🔑 API Key Setup**
Before running the project, create a `.env` file inside the project directory and add your API keys:  

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## **▶️ Running the Project**  ```
1. **Run the script**:
   ```sh
   python main.py
   ```
2. **Enter your query:** 
---

## **🛠 File Structure**
```
multi-agent-rag/
│── agents/               # Contains search, fact-checking, and summarization agents
│   ├── search_agent.py   # Retrieves information from the web
│   ├── fact_checker.py   # Validates information for accuracy
│   ├── summarizer.py     # Summarizes the validated information
│
│── utils/                # Utility files
│   ├── config.py         # Loads environment variables and API keys
│
│── main.py               # Runs the multi-agent system
│── requirements.txt      # Project dependencies
│── README.md             # Documentation
│── .env                  # API keys (Not pushed to GitHub)
│── .gitignore            # Ignore unnecessary files
```

---

## **📚 How It Works**
1. **Search Agent**: Queries **Tavily API** to fetch relevant web results.  
2. **Fact-Checking Agent**: Validates the retrieved data.  
3. **Summarization Agent**: Uses **Google Gemini 1.5 Pro** to generate a refined summary.  

---

## **📌 Example Output**
```
User Query: "Latest advancements in AI research?"
-> Web Search Agent fetches articles
-> Fact-Checker verifies information
-> Summarizer generates a clean summary using Gemini 1.5 Pro
Final Output: "Recent AI advancements include breakthroughs in multimodal models like Gemini 1.5..."
```

---

## **📞 Contact**
For any queries, feel free to reach out:  
Phone : +91 8707808583  

---

### **✅ Now, commit and push it to GitHub!**
```sh
git add README.md
git commit -m "Updated README with query instructions"
git push origin main
```


