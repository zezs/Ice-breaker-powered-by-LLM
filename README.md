# Ice Breaker

**NOTE: Currently under progress**
**Estimated timeline: To be finished this weekend (19/7/2024 - 20/7/2024)**

## Overview

Ice Breaker is a comprehensive fullstack application powered by generative AI. It crawls the web to find a person's LinkedIn profile and utilizes the LangChain library to craft engaging ice breakers based on their history. LangChain ReAct (Reasoning Action) agents are employed to ensure the accurate return of the LinkedIn profile URL and to clean tokens in the resulting JSON data. The output from the LLM is parsed using LangChain's output parser to identify four key components from the JSON file: a summary, two intriguing facts, topics of interest, and two crafted ice breakers. The frontend is created with static HTML/CSS, while Flask is used for the backend development.

## Topics covered and Learned
Python | Langchain | LLMs | Langsmith | Geneartive-AI | Prompt Enginerring | Chain of thoughts | Agents | ReAct Agents | Tools | Web scrapping and Crawling | Flask | HTML/CSS | Output Parser | Proxycurl | Tavily Web API |


## Components

- **Flask Backend:** Serves as the backbone of the application, handling HTTP requests, API interactions, and serving dynamic content using Jinja2 templating.

- **LangChain with OpenAI LLM:** Utilizes advanced language models for generating personalized and contextually relevant IceBreaker suggestions.

- **Social Media Integration:** Leverages APIs from Google Search, Twitter, and LinkedIn to gather insights and tailor conversations effectively.

- **Frontend:** Built with HTML and CSS, providing a user-friendly interface for interaction.

