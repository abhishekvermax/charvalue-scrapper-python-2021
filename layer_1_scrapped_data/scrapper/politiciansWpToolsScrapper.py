import wptools
import pandas as pd


politicians_state_ut_india = 'Category:Indian politicians by state or union territory'
sub_category_list = wptools.category(politicians_state_ut_india) \
    .get_members().data.get('subcategories')

sub_category_titles = [sub_cat.get('title') for sub_cat in sub_category_list]

sub_2_cat_categories = [wptools.category(sub_sub_cat).get_members().data
                        .get('subcategories') for sub_sub_cat in sub_category_titles]

sub_2_cat_titles = set([item.get('title') for sublist in sub_2_cat_categories for item in sublist])

profiles = []
for sub_cats in sub_2_cat_titles:
    if len(wptools.category(sub_cats).get_members().data.get('members')) > 0:
        for profile in wptools.category(sub_cats).get_members().data.get('members'):
            profiles.append({'page_id': profile.get('pageid'), 'title': str(profile.get('title')).replace(" ", "_")})

df = pd.DataFrame(profiles)

df["wiki_link_complete"] = 'https://en.wikipedia.org/wiki/' + df["title"]

df.to_csv('/home/abhi/Documents/owngit/charvalue-2021/dataScrapperPython/scrapped_data/wiki_page_id_title_politicians_india.csv')
