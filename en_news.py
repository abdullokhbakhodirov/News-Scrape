import requests
import feedparser

all_news_en = {}

# First way getting news from BBC.com
def get_big_news_en():
    url = 'https://www.bbc.com/news'
    def get_html(url):
        response = requests.get(url=url)
        return response.text
    
    html_code = get_html(url)
    string = '''<a class="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor" href="'''
    ent_str = '''"><'''
    ind_start = html_code.find(string)
    st = html_code[ind_start+len(string):]
    ind_end = st.find(ent_str)
    link = st[:ind_end]
    html_code.replace(html_code[ind_start:ind_end],'')
    html_code2 = get_html(f'https://www.bbc.com/{link}')
    string2 = '''<h1 tabindex="-1" id="main-heading" class="ssrcss-15xko80-StyledHeading e1fj1fc10">'''
    end_str = '''</h1>'''
    ind_start2 = html_code2.find(string2)
    st2 = html_code2[ind_start2+len(string2):]
    int_end = st2.find(end_str)
    title = st2[:int_end]
    all_news_en[title] = link
    return 1


# Second way getting news from BBC.com
def get_news_en():
    url = 'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml'
    data = feedparser.parse(url)
    i=0
    while i < len(data):
        for entry in data.entries:
            all_news_en[entry.title] = entry.link
            i += 1
