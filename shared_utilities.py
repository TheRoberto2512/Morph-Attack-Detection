import gdown

def download_dataset(file_id, output, msg=False):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output, quiet=False)
    if msg:
        print(f"\nFile scaricato e salvato come {output}!\n")
