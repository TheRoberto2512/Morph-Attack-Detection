![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Morph Attack Detection (MAD)
<p align="justify">
Il <b>morphing</b> è una tecnica sofisticata che combina più volti per creare immagini artificiali con l'obiettivo di eludere i sistemi di riconoscimento facciale. Questa tecnica sfrutta le capacità avanzate dell'intelligenza artificiale per fondere caratteristiche distintive di volti diversi, generando così immagini che appaiono realistiche ma che, in realtà, sono false.
<br><br>In questo progetto vengono utilizzati approcci di Machine Learning e Deep Learning per addestrare degli agenti in grado di rilevare le immagini contraffatte. È possibile consultare la presentazione del progetto a <a href="https://docs.google.com/presentation/d/1-yfGdvXWoD5BI5NDLq10w1Io41wOWotWv0fcinI6cJY/edit#slide=id.p">questo link</a>.
</p>

 
# Dataset utilizzato
<p align="justify">Per il progetto è stato utilizzato il dataset <i>"AMSL Face Morph Image Data Set"</i>, scaricabile da <a href="https://omen.cs.uni-magdeburg.de/disclaimer/index.php">questo link</a>. Il repository contiene solamente i notebooks e i file necessari per addestrare ed eseguire i modelli, ma il dataset per gli addestramenti non viene fornito per via della licenza.</p>

# Installazione
## **Requisiti:**   
L'unico requisito è un account Google per poter accedere a  <a href="https://drive.google.com/">Google Drive</a> e salvare la cartella contenente i notebooks da eseguire tramite <a href="https://colab.research.google.com">Google Colab</a>.     

## **Istruzioni step-by-step:**   
1) Scaricare i file da GitHub e caricarli su Google Drive nella **<u>stessa cartella</u>**;     
 **NOTA:** _È fortemente consigliato di creare la cartella del progetto nella propria home su Google Drive. Qualora si voglia comunque utilizzare una cartella differente sarà necessario aggiornare il percorso della cartella su ogni notebook._

2) Aprire il file `settings.json` e inserire i Google Drive ID per il file zip contenente il dataset e per il file csv contenente informazioni extra riguardo il dataset. Il json fornito non contiene un ID per il dataset;<br>

3) In qualsiasi notebook verrà chiesto di inserire il percorso della cartella Google Drive dove sono contenuti i vari file. Una volta impostata sarà possibile eseguire i notebooks;<br>
 **NOTA:** _Il percorso va impostato manualmente in qualsiasi notebook al momento del suo primo utilizzo, poi rimarrà salvato e non ci sarà bisogno di inserirlo nuovamente._

# Struttura del progetto
Il progetto è stato organizzato in più notebooks/files in base ai modelli e alle operazioni da effettuare:

<div align="center">

| Nome File | Descrizione |
| :---: | :---: |
| `Analisi Dataset.ipynb` | Notebook per l'analisi del dataset e del csv ad esso associato |
| `Pre Processing.ipynb` | Notebook per il pre-processing del dataset |
| `Classificatore I.ipynb` | Notebook contenente il primo classificatore semplice |
| `Classificatore II (CNN).ipynb` | Notebook contenente il secondo classificatore semplice  |       
| `Componente Avanzata.ipynb` | Notebook il sistema di riconoscimento facciale _naive_  |  
| `settings.json`| File di configurazione per download del dataset e di altri file |
| `shared_utilities.py`| File python contenente le funzioni condivise |

</div>

# Autori
<a href="https://github.com/theroberto2512/Morph-Attack-Detection/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=theroberto2512/Morph-Attack-Detection"/>
</a>  
