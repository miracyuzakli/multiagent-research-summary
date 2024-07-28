# Multiagent Research Summary

### Research and Summary Agent

This project involves creating two agents using the OpenAI API to perform research on a given topic and then summarize the researched content. The project demonstrates the usage of the OpenAI API for stream processing to handle real-time responses.

### Prerequisites

1. Python 3.x
2. OpenAI Python library
3. dotenv library

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/miracyuzakli/multiagent-research-summary.git
    cd multiagent-research-summary
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install openai python-dotenv
    ```

4. Create a `.env` file in the project directory and add your OpenAI API key:
    ```sh
    OPENAI_API_KEY=your_openai_api_key
    ```

### Usage

1. Modify the `topic` variable in the `main()` function to your desired research topic.

2. Run the script:
    ```sh
    python main.py
    ```

3. The script will output the research content and its summary.

### Code Structure

- `ResearchAgent`: Class responsible for conducting research on a given topic.
- `SummaryAgent`: Class responsible for summarizing the researched content.
- `main()`: Main function to orchestrate the research and summarization process.

### Example Output

```
Research Content: ...
Summary: ...
```

