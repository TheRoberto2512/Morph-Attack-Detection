# IMPORT LIBRERIE
from datetime import datetime
import tensorflow as tf
import numpy as np
import requests
import shutil
import random
import gdown
import math
import os
# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 

def download_dataset(file_id, output, msg=False):
  '''
  Funzione per scaricare il dataset.
  
  Parametri:
  - file_id: ID del file su Google Drive.
  - output: nome da assegnare al file appena scaricato.
  - msg: se True, stampa il messaggio alla fine del download (default = False).
  '''
  
  url = f'https://drive.google.com/uc?id={file_id}'
  gdown.download(url, output, quiet=False)
  if msg:
    print(f"\nFile scaricato e salvato come {output}!\n")

# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- #        

def get_date_and_time():
  '''Funzione per ottenere data e ora tramite API request (in alternativa usa l'utc di datetime).'''
  
  response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Rome')

  if response.status_code == 200:
    datetime_string = response.json()['datetime']
    date = datetime_string.split('T')[0]
    time = datetime_string.split('T')[1].split('.')[0]
  else:
    current_time = datetime.utcnow().strftime('%Y-%m-%dS%H:%M:%S')
    date = '(E)_' + current_time.split('S')[0] # indica che è fallita l'API request
    time = current_time.split('S')[1]

  return (date, time)
  
# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- #  
  
def save_model_weights(file_path, drive_path, output_name, add_DateTime=True):
  '''
  Funzione per salvare i pesi del modello convolutivo.
  
  Parametri:
  - file_path: percorso del file sull'ambiente Colab.
  - drive_path: path della directory su Drive dove salvare il file.
  - output_name: nome da assegnare al file.
  - add_DateTime: se True, aggiunge data e ora alla fine del nome (default = True).
  '''
  
  if add_DateTime == True:
    date, time = get_date_and_time()
    filename = output_name + '_' + date + '_' + time + '.keras'
  else:
    filename = output_name
  
  shutil.copy(file_path, drive_path + filename)
  
# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- #  

def move_files(source_folder, dest_folder, files):
  '''
  Funzione per spostare i file.

  Parametri:
  - source_folder: la cartella di origine dei file da spostare.
  - dest_folder: la cartella di destinazione dei file spostati.
  - files: la lista dei file da spostare.
  '''

  os.makedirs(dest_folder, exist_ok=True)
  for file_name in files:
      src = os.path.join(source_folder, file_name)
      dst = os.path.join(dest_folder, file_name)
      shutil.move(src, dst)

# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 

def split_dataset(path_dataset, train, val, test, bona_fide_count, morphed_count, VAL, TEST):
  '''
  Funzione per suddividere il dataset.
  
  Parametri:
  - path_dataset: percorso del dataset.
  - train: percorso della cartella train.
  - val: percorso della cartella val.
  - test: percorso della cartella test.
  - bona_fide_count: numero di immagini di bona_fide nel dataset.
  - morphed_count: numero di immagini di morphed nel dataset.
  - VAL: percentuale di split per il validation set.
  - TEST: percentuale di split per il test set.
  '''

  bona_fide_count = len(os.listdir(os.path.join(path_dataset,'bona_fide')))
  morphed_count = len(os.listdir(os.path.join(path_dataset,'morphed')))

  # calcolo del numero di immagini da spostare in ogni cartella
  bona_fide_to_test = int(math.ceil(bona_fide_count * TEST / 100))
  bona_fide_to_val = int(math.ceil(bona_fide_count * VAL / 100))
  bona_fide_to_train = bona_fide_count - (bona_fide_to_test + bona_fide_to_val)

  morphed_to_test = int(morphed_count * TEST / 100)
  morphed_to_val = int(morphed_count * VAL / 100)
  morphed_to_train = morphed_count - (morphed_to_test + morphed_to_val)

  # suddivisione e spostamento dei file per la classe bona_fide
  bona_fide_files = os.listdir(os.path.join(path_dataset, 'bona_fide'))
  random.shuffle(bona_fide_files)

  move_files(os.path.join(path_dataset, 'bona_fide'), os.path.join(test, 'bona_fide'), bona_fide_files[:bona_fide_to_test])
  move_files(os.path.join(path_dataset, 'bona_fide'), os.path.join(val, 'bona_fide'), bona_fide_files[bona_fide_to_test:bona_fide_to_test + bona_fide_to_val])
  move_files(os.path.join(path_dataset, 'bona_fide'), os.path.join(train, 'bona_fide'), bona_fide_files[bona_fide_to_test + bona_fide_to_val:])

  # suddivisione e spostamento dei file per la classe morphed
  morphed_files = os.listdir(os.path.join(path_dataset, 'morphed'))
  random.shuffle(morphed_files)

  move_files(os.path.join(path_dataset, 'morphed'), os.path.join(test, 'morphed'), morphed_files[:morphed_to_test])
  move_files(os.path.join(path_dataset, 'morphed'), os.path.join(val, 'morphed'), morphed_files[morphed_to_test:morphed_to_test + morphed_to_val])
  move_files(os.path.join(path_dataset, 'morphed'), os.path.join(train, 'morphed'), morphed_files[morphed_to_test + morphed_to_val:])
  
# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 

def get_img_array(img_path, target_size):
    '''
    Funzione per ottenere l'immagine sotto forma di array.
    
    Parametri:
    - img_path: percorso dell'immagine.
    - target_size: dimensioni dell'immagine come tupla (width, height).
    '''
    
    img = tf.keras.utils.load_img(img_path, target_size=target_size) # carica l'immagine
    img_array  = tf.keras.utils.img_to_array(img)                    # converte l'immagine in un array
    img_array  = np.expand_dims(img_array , axis=0)                  # espande le dimensioni dell'array per adattarsi al modello

    return img_array

# -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # -- -- # 
