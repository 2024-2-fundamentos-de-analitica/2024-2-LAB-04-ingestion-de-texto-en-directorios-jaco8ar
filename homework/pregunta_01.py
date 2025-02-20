# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import os
def leer_archivos(type_folder, feeling):
    phrases = []
    for _, _, files in os.walk(rf"files/input/{type_folder}/{feeling}"):
        for file in files:
            with open(f"files/input/{type_folder}/{feeling}/{file}") as reading_file:
                phrases.append(reading_file.readlines()[0])
    return phrases


def build_df(group_type):
    feelings = ["negative", "neutral", "positive"]
    sentences = []
    feelings_of_df = []
    for feeling in feelings:
        archivos = leer_archivos(group_type, feeling)
        sentences.extend(archivos)
        feelings_of_df.extend([feeling]*len(archivos))

    return (sentences, feelings_of_df)



def pregunta_01():



    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
    """
    sentences_test, feelings_test = build_df("test")

    dict_for_df_test = {
        "phrase": sentences_test,
        "target": feelings_test
    }
    
    test_df = pd.DataFrame(dict_for_df_test)

    sentences_train, feelings_train = build_df("train")

    dict_for_df_train = {
        "phrase": sentences_train,
        "target": feelings_train
    }
    
    train_df = pd.DataFrame(dict_for_df_train)

    test_df.to_csv("files/output/test_dataset.csv", index = False)
    train_df.to_csv("files/output/train_dataset.csv", index = False)
    


pregunta_01()