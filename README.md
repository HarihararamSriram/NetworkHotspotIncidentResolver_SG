<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Identification of Potential Hotspots In Network Infrastructure</h2>

  <p align="center">
    Provides resolutions to network hotspot scenarios
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="./img/P1.png">

This application is a platform that can automatically identify the most appropriate resolution for a given hotspot. This solution should leverage historical data and frequency of resolutions to determine the best course of action.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Tools we used:

* Python
* Streamlit
* Scikit-Learn
* ChatGPT
* Google Colab

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Installation

* cmd
  ```sh
  pip install -r requirements.txt
  ```
## Usage

1) The model we have used can be trained by running the cells in our Jupyter Notebook "./Network_Hotspot_Training.ipynb"
2) Once the model is trained run the chatbot interface with the following command in terminal
* cmd
  ```sh
  streamlit run main.py
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Train Model
- [x] Build a ChatBot Interface
- [ ] Integrate LLM
- [ ] Integrate NLP Techniques and RNN


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## DEMO
<video src="./videos/Recording.mp4">