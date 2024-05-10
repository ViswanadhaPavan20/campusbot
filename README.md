# Campus Bot - Chatbot for SRGEC (Seshadri Rao Gudlavalleru Engineering College)

Campus Bot is an AI-powered chatbot designed to assist students, faculty, and visitors with their queries regarding SRGEC (Sri Rajagopala Garu Engineering College, Gudlavalleru). It utilizes the RAG (Retrieval-Augmented Generation) architecture, combining information retrieval from a web-scraped knowledge base with natural language generation capabilities.

## Features

- `Natural Language Understanding`: Campus Bot can understand and respond to user queries in natural language, making the interaction intuitive and user-friendly.
- `Web-Scraped Knowledge Base`: The chatbot leverages a knowledge base created by web scraping relevant information from the SRGEC website using Beautiful Soup4.
- `Vector Database`: The scraped information is stored in a Qdrant vector database, allowing efficient retrieval of relevant information using semantic similarity.
- `Retrieval-Augmented Generation`: Campus Bot employs the RAG architecture, combining information retrieval from the knowledge base with natural language generation to provide informative and contextual responses.
- `Streamlit Interface`: The chatbot features a user-friendly interface built with the Streamlit framework, making it accessible and easy to use.
- `Cloud Deployment`: Campus Bot is deployed on Streamlit Cloud, ensuring seamless access and scalability.

## Architecture
<img width="828" alt="Final Architecture" src="https://github.com/MaruthiKo/campusbot/assets/63769209/93be6ad4-76bf-438a-a085-1e9c0e7fd7a0">


## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/campus-bot.git
```

2. Navigate to the project directory:

```bash
cd campus-bot
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the Campus Bot locally, execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit application, and you can interact with the chatbot through the provided interface.

## Deployment

Campus Bot is deployed on Streamlit Cloud, which allows for easy access and scalability. You can access the deployed chatbot at the following URL: [CampusBot](https://iotbot.streamlit.app/)

## Contributing

Contributions to Campus Bot are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the easy-to-use application framework.
- [Beautiful Soup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping capabilities.
- [Qdrant](https://qdrant.tech/) for the vector database used in the knowledge base.
- [RAG Architecture](https://www.semanticscholar.org/paper/Retrieval-Augmented-Generation-for-Knowledge-Intensive-Lewis-Hancock/5d6ce4ac40b6d65a5d6cd02b5f8f2ffb0ff9b379) for the retrieval-augmented generation approach.

```
