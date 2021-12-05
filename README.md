# README

Educational Search Engine for Information Retrival and Web Analytics course at UPF. The web application retrives information of the @WHO tweets dataset by using Word2Vec and Cosine Similarity. It also provides two dashboards with web analytics statistics, for the global SE and for every Tweet in the dataset. It is built over a Python Flask backend and JS simple frontend.  

## Authors

Víctor Aguado <br>
Mar Castroviejo <br>
Marta Gràcia <br>

## Preview
<img src="https://github.com/SrtoPeixet/EducationalSearchEngine/raw/master/preview.gif" width="1080" height=auto />

## Requeriments & Installation

You will need some packages if you want to run it locally. For the backend, we use DeepTranslator for processing tweets in non-english languages. You will also need to install jsonpickl, gensim and nlkt. If anyone finds another requirement please let us know in order to update the following snippet. 

`pip install deep-translator`<br>
`pip install jsonpickle`<br>
`pip install gensim`<br>
`pip install nlkt`<br>

Npm is also required for running the dashboards. We are using chartJS, installation is quite straight forward. Please refer to:

- NPM Download: https://nodejs.org/es/download/
- ChartJS Installation: https://www.chartjs.org/docs/latest/getting-started/installation.html

You may also need a pluging for the chromatic scale used in some charts.

`npm install d3-scale-chromatic`

NOTE: We know that installation may require some time, this porject is thought to be uploaded in some hosting service and used online, not locally. If you need some video demo we can provide it. You can also check source code for IRWA specific functionalities to avoid installation process.

## Usage

For initiating the server, run the following command in the project root directory. If you use VSCode enviroment you just have to hit "PLAY" button and it will automatically start in that file.

`python web_app.py`

You will see in the terminal a message displaying your localhost IP and port. Access that address via web browser.

## Comments

As this is a Information Retrival project, we did not spent the required time in solving frontend bugs, such as hitting the previous result button in the first result, and this kind of basic exceptions. We also want to comment that we could display more statistics in the dashboards, however, with the ones we are showing we demonstrate how it has to be done, and implementing new ones is quite straight forward. 

We could extend this project with more complex statistic such as Heatmaps, implementing the top content ranking, counting usefullness of clicks, related clicks on results and many more... It could be very interesting to do so in a TFG taking in consideration the work load it supposes. 

Finally, we hope you enjoy it, and make us know any comment/idea you have !
