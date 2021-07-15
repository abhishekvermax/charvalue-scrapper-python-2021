from sqlalchemy import create_engine
import pandas as pd
import wptools


def title_data(title):
    return wptools.page(title).get().data.get('wikidata')


def get_features_character(title, charcter_id_db):
    profile_dict = title_data(title)
    # for title, title in enumerate(profile_dict.items()):
    character = {'character_id': charcter_id_db,
                 'aggregated_rating': 0,
                 'category': 1,
                 'character_achievements': "",#str(profile_dict.get('award received (P166)', "")),
                 'character_birth_place': str(profile_dict.get('place of birth (P19)', "")),
                 'character_description':
                     str({'Position': "".join(profile_dict.get('position held (P39)', "")),
                          'Member of political party': profile_dict.get('member of political party (P102)', ""),
                          'Candidacy in election': profile_dict.get('candidacy in election (P3602)', "")
                          }),
                 'character_dob': str(profile_dict.get('date of birth (P569)', "")),
                 'character_dod': str(profile_dict.get('date of death (P570)', "")),
                 'character_first_name': str(title).split("_")[0],
                 'character_last_name': " ".join(str(title).split("_")[1:len(title)]),
                 'character_occupation': str(profile_dict.get('occupation (P106)')),
                 'character_photo_path': "",
                 'title': title,
                 'comment_count': 0,
                 'rating_count': 0,
                 'character_creation_timestamp': '2011-03-13 02:53:50'
                 }

    df = pd.DataFrame(character, index=[0])
    print("insert done")
    return df


engine = create_engine("mysql://admin:admin@123@localhost/charvalue")
get_features_character('Narendra_Modi', 8939).to_sql(con=engine,
                                                     name='character_in',
                                                     if_exists='append',
                                                     index=False)
