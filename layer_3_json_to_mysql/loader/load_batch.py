import json
from sqlalchemy import create_engine
import pandas as pd
import re


def get_features_character(json_path):
    profiles = []
    character_dict = get_character_names(json_path)
    for k, v in enumerate(character_dict.items()):
        try:
            title = v[0]
            feature = v[1]
            profiles.append({'character_id': k + 2000,
                             'aggregated_rating': 0,
                             'category': 1,
                             'character_achievements': re.sub("[\(\[].*?[\)\]]", "",str(feature.get('award received ('
                                                                                                    'P166)',
                                                                                                    ""))) if type(
                                 feature.get('award received (P166)', "")) != list else re.sub("[\(\[].*?[\)\]]", "",
                                                                                               str(",".join(feature.get('award received (P166)', "")))),
                             'character_birth_place': str(feature.get('place of birth (P19)', "")),
                             'character_description':
                                 re.sub("[\(\[].*?[\)\]]", "",
                                        ",".join([x.capitalize() for x in str("".join(feature.get('position held (P39)', "")) + ", " +
                                            feature.get('member of political party (P102)', "") + ", " +
                                            feature.get('candidacy in election (P3602)', "")
                                            ).split(", ") if x != ""])),
                             'character_dob': str(feature.get('date of birth (P569)', "")),
                             'character_dod': str(feature.get('date of death (P570)', "")),
                             'character_first_name': str(title).split("_")[0],
                             'character_last_name': " ".join(str(title).split("_")[1:len(title)]),
                             'character_occupation':str("".join(feature.get('occupation (P106)'))),
                             'character_photo_path': str(feature.get('url_img', "")),
                             'title': title,
                             'comment_count': 0,
                             'rating_count': 0,
                             'character_creation_timestamp': '2011-03-13 02:53:50'
                             })
        except:
            print("Caught it")
    df = pd.DataFrame(profiles)
    #
    engine = create_engine("mysql://admin:admin123@localhost/charvalue")
    # # conn = pymysql.connect(host='localhost',
    # #                        port=3306,
    # #                        user='admin',
    # #                        passwd='admin@123',
    # #                        db='charvalue',
    # #                        charset='utf8')
    #
    df.to_sql(con=engine, name='character_in', if_exists='append', index=False)

    # print(df)

       # list_features = []
    # try:
    #     for idx in range(len(character_values)):
    #         list_features.extend(character_values[idx].keys())
    # except:
    #     print("Caught it!")
    # return [keys for keys in sorted(list(set(list_features))) if 'ID' not in keys]


def get_character_names(json_path):
    with open(json_path, 'r') as j:
        characters = json.loads(j.read())
    return characters


print(get_features_character(
    '/home/abhi/IdeaProjects/charvalue-2021/dataScrapperPython/layer_2_profile_scrapped/data/profile_data_politicians.json'))
