import pandas as pd
import wptools
import json


def get_profiles_from_titles(input_csv_path, output_json_path):
    df = pd.read_csv(input_csv_path)
    title_list = [profile for profile in df.get('title')]
    data = {}
    for idx in range(0, len(title_list)):
        try:
            dict_img = wptools.page(title_list[idx]).get().data.get('wikidata')
            dict_img.update({'url_img': str(wptools.page(title_list[idx]).get().data.get('image')[0].get('url', "")) if wptools.page(title_list[idx]).get().data.get('image',None) is not None else ""})
            data.update({title_list[idx]: dict_img})
            with open(output_json_path, "w+") as output:
                json.dump(data, output)
        except:
            print("Caught it!")


get_profiles_from_titles(
    input_csv_path='/home/abhi/IdeaProjects/charvalue-2021/dataScrapperPython/layer_1_scrapped_data/data/wiki_page_id_title_politicians_india.csv',
    output_json_path='/home/abhi/IdeaProjects/charvalue-2021/dataScrapperPython/layer_2_profile_scrapped/data/profile_data_politicians.json'
)
