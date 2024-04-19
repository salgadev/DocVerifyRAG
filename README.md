---
title: DocVerifyRAG
emoji: 🖺
colorFrom: pink
colorTo: green
sdk: streamlit
sdk_version: 1.27.0
app_file: app.py
pinned: false
---

<!-- PROJECT TITLE -->
  <h1 align="center">DocVerifyRAG: Anomaly detection for BIM document metadata</h1>
 <div id="header" align="center">
</div>
<h2 align="center">
 Description
</h2>
<p align="center"> Introducing DocVerifyRAG, a cutting-edge solution revolutionizing document verification processes across various sectors. Our app goes beyond mere document classification; it focuses on ensuring metadata accuracy by cross-referencing against a vast vector database of exemplary cases. Inspired by the necessity for precise data management, DocVerifyRAG leverages AI to scrutinize document metadata, instantly flagging anomalies and offering suggested corrections. Powered by Vectara vector store technology and supported by the innovative capabilities of together.ai API, our app employs advanced anomaly detection algorithms to scrutinize metadata, ensuring compliance with regulatory standards and enhancing data integrity. With DocVerifyRAG, users can effortlessly verify document metadata accuracy, minimizing errors and streamlining operational efficiency.</p>

## Table of Contents

<details>
<summary>DocVerifyRAG</summary>
  
- [Table of Contents](#table-of-contents)
- [TRY the prototype](#try-the-prototype)
- [Screenshots](#screenshots)
- [Technology Stack](#technology-stack)
  - [Features](#features)
  - [Install locally](#install-locally)
  - [Usage](#usage)
- [Authors](#authors)
- [License](#license)

</details>

## TRY the prototype
[DocVerifyRAG](https://docverifyrag.vercel.app/)

## Screenshots
![ttthh](https://github.com/eliawaefler/DocVerifyRAG/assets/19821445/331845d7-a360-4315-92ef-d4bb50021eaa)

## Technology Stack
| Technology | Description |
| --- | --- |
| **Python** | Primary programming language used for development. |
| **LangChain** | Framework for developing applications powered by large language models (LLMs). |
| **Vectara** | Provides efficient vector search capabilities via the Boomerang model in a "RAG as a service" architecture. |
| **intfloat/multilingual-e5-large** | Generates efficient and performant multilingual language embeddings. |
| **Together AI** | Platform for training, fine-tuning, and deploying gen AI models. Its inference API was used with the model `mistralai/Mixtral-8x7B-Instruct-v0.1`. |
| **Streamlit** | Open-source Python library for creating custom web apps, used as the frontend. |
| **Hugging Face Spaces** | Service for developer-friendly deployments of data applications. |

The backend is built using Python, LangChain, Vectara, and Together AI's inference API with the `mistralai/Mixtral-8x7B-Instruct-v0.1` model for processing and understanding large amounts of data. Streamlit is used for the frontend, providing an intuitive interface for users. Hugging Face Spaces simplifies the deployment process, making the application easily accessible.


### Features

1. **Metadata Verification:**
- Cross-references document metadata against a comprehensive vector database of exemplary cases.
- Instantly identifies anomalies and discrepancies, ensuring metadata accuracy and compliance.

2. **Automated Metadata Correction:**
- Offers suggested metadata corrections based on processed PDF files, facilitating swift and accurate adjustments.
- Potential for automated inspection of numerous metadata rows for seamless large-scale data verification.

3. **Question Answering Retriever:**
- Utilizes Vectara vector store technology for efficient retrieval of relevant information.
- Employs Hugging Face embeddings E5 multilingual model for precise analysis of multilingual data.
- Identifies anomalies in names, descriptions, and disciplines, providing actionable insights for data accuracy.

4. **User-Friendly Interface:**
- Intuitive web interface for effortless document upload, metadata verification, and correction.
- Simplifies document management processes, reducing manual effort and enhancing operational efficiency.

### Install locally

1. Clone the repository:
    ```bash
    $ git clone https://github.com/salgadev/DocVerifyRAG.git
    ```

2. Install dependencies:
    ```bash
    $ pip install -r requirements.txt
    ```

3. Run using Streamlit:
    ```bash
    $ streamlit run app.py
    ```

### Usage

Access the web interface and follow the prompts to upload documents, classify them, and verify metadata. The AI-powered anomaly detection system will automatically flag any discrepancies or errors in the document metadata, providing accurate and reliable document management solutions.
## Authors

| Name           | Link                                      |
| -------------- | ----------------------------------------- |
| Sandra Ashipala | [GitHub](https://github.com/sandramsc) |
| Elia Wäfler | [GitHub](https://github.com/eliawaefler) |
| Carlos Salgado | [GitHub](https://github.com/salgadev) |


## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/eliawaefler/DocVerifyRAG/blob/main/LICENSE)