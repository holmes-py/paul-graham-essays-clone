from multiprocessing import Pool, freeze_support
from pyhtml2pdf import converter

def call_and_save(link):
    link_URI = link.split('>')[0].split('"')[1]
    url_to_fetch = f"https://paulgraham.com/{link_URI}"
    file_Name = link.split(">")[1][:-3].replace('/','_')
    if len(file_Name)>2 and 'turbifycdn' not in link_URI: 
        print(f"{raw_data.index(link)}/{len(raw_data)}. Blog name: {file_Name}, link: {url_to_fetch}")
        converter.convert(url_to_fetch, f'pdfs/{file_Name}.pdf', print_options={"scale": 1.5})
    else: 
        print(f"Skipping {link_URI}")
    

raw_data = open('extracted-blog-regex.txt', 'r').readlines()

if __name__ == '__main__':
    freeze_support()  # Add this line
    with Pool(20) as p:
        p.map(call_and_save, raw_data)