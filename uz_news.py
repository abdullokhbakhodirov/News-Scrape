import requests


all_news_uz = {}


def get_big_news_uz():
    url = 'https://kun.uz/uz/news/category/uzbekiston'  
    def get_html(url):
        response = requests.get(url)
        return response.text

    html_code = get_html(url)
    ind_start = html_code.find("big-news__title")
    ind_end = html_code.find('''</span><span class="big-news__description">''')
    st = html_code[ind_start+17:ind_end]

    ind1 = html_code.find('''<a class="big-news" href="''')
    ind2 = html_code[ind1+26:]
    ind3 = ind2.find(">")
    ind4 = ind2[:ind3]
    ind5 = f"https:/kun.uz{ind4[:-1]}"
    all_news_uz[st] = ind5
    return 1


def get_small_news_uz():
    url = 'https://kun.uz/uz/news/category/uzbekiston'  
    def get_html(url):
        response = requests.get(url)
        return response.text

    html_code = get_html(url)
    cout = html_code.count("small-news__title")
    cout1 = cout
    while cout != 0:
        ind_start = html_code.find("small-news__title")
        s = html_code[ind_start+19:]
        ind_end = s.find('''>''')
        st = s[:ind_end]
        length = len(st)
        n = html_code[ind_start+19+length:]
        n1 = n.find("<")
        n2 = n[1:n1]

        ind1 = html_code.find('''<a class="small-news__title" href="''')
        ind2 = html_code[ind1+35:]
        ind3 = ind2.find(">")
        ind4 = ind2[:ind3]
        ind5 = f"https:/kun.uz{ind4[:-1]}"
        cout -= 1
        all_news_uz[n2] = ind5
        html_code = html_code[:ind_start] + html_code[ind_start+19+length:]

    return cout1


def get_middle_news_uz():
    url = 'https://kun.uz/uz/news/category/uzbekiston'  
    def get_html(url):
        response = requests.get(url)
        return response.text

    html_code = get_html(url)
    cout = html_code.count('''<a class="news__title" href="''')
    cout1 = cout
    while cout != 0:
        ind_start = html_code.find('''<a class="news__title" href="''')
        s = html_code[ind_start+29:]
        ind_end = s.find('''>''')
        st = s[:ind_end]
        length = len(st)
        n = html_code[ind_start+29+length:]
        n1 = n.find("<")
        n2 = n[1:n1]

        ind1 = html_code.find('''<a class="news__title" href="''')
        ind2 = html_code[ind1+29:]
        ind3 = ind2.find(">")
        ind4 = ind2[:ind3]
        ind5 = f"https:/kun.uz{ind4[:-1]}"
        cout -= 1
        all_news_uz[n2] = ind5
        html_code = html_code[:ind_start] + html_code[ind_start+29+length:]
    return cout1


def get_news_uz():
    new1 = get_big_news_uz()
    new2 = get_small_news_uz()
    new3 = get_middle_news_uz()
    return new1+new2+new3, all_news_uz


#main function is get_news_uz()
