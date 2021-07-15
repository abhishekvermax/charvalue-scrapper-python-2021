import wptools
import pandas as pd

indian_actors_data = 'Category:Indian_actors'
profiles = []

for profile in wptools.category(indian_actors_data).get_members().data.get('members'):
    profiles.append({'profiles': profile.get('pageid'), 'title': profile.get('title')})
sub_category_list = wptools.category(indian_actors_data) \
    .get_members().data.get('subcategories')

sub_category_titles = [sub_cat.get('title') for sub_cat in sub_category_list]

for sub_sub_cat in sub_category_titles:
    if len(wptools.category(sub_sub_cat).get_members().data.get('members'))>0:
        for profile in wptools.category(sub_sub_cat).get_members().data.get('members'):
            profiles.append({'profiles': profile.get('pageid'), 'title': profile.get('title')})

sub_2_cat_categories = [wptools.category(sub_sub_cat).get_members().data
                        .get('subcategories',[]) for sub_sub_cat in sub_category_titles]

sub_2_cat_titles = set([item.get('title') for sublist in sub_2_cat_categories for item in sublist])

for sub_cats in sub_2_cat_titles:
    if len(wptools.category(sub_cats).get_members().data.get('members')) > 0:
        for profile in wptools.category(sub_cats).get_members().data.get('members'):
            profiles.append({'page_id': profile.get('pageid'), 'title': profile.get('title')})

df = pd.DataFrame(profiles)
df.to_csv('/home/abhi/IdeaProjects/charvalue-2021/dataScrapperPython/scrapped_data'
          '/wiki_page_id_title_actors_india.csv')
