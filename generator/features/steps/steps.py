from behave import given, when
import requests, json


@given('the outfit generator is live on the website')
def outfit_generator(context):
    context.requests = []
    context.history_outfits = []
    context.history_articles = []

@when('users buy the {outfit} outfit {n} times with top {top_article}, trousers {trouser_article} and shoes {shoes_article}')
def users_buy(context, outfit, n, top_article, trouser_article, shoes_article):

    context.history_outfits.append(outfit)
    context.history_articles.extend([top_article, trouser_article, shoes_article])

    request = {"articles":
                [{"look": outfit,
                     "category": "shoes", "articleId": shoes_article},
                 {"look": outfit,
                     "category": "trousers", "articleId": trouser_article},
                 {"look": outfit,
                     "category": "tops", "articleId": top_article}]}
    context.requests.append(request)

    for _ in range(int(n)):
        response = requests.post("http://127.0.0.1:5000/generate", json=request)

    context.response = response.json()

@then('we generate a HTML {scenario} file with a new outfit')
def dump_html(context, scenario):

    items = []
    print(context.response)
    outfit = context.response["name"]
    for category, article in context.response.items():
        if category in ["shoes", "tops", "trousers"]:
            article["category"] = category
            items.append(article)

    html_str = ""

    # red if exploitation
    color = '#0000FF'

    # if list(category.keys())[0] in context.categories:
    #     # blue if exploration
    #     color = '#FF0000'

    recs_img = ""

    for item in items:
        print(item["articleId"])
        print(context.history_articles)
        if item["articleId"] in context.history_articles:
            color = '#FF0000'
        else:
            color = '#0000FF'
        recs_img += f"<td><h1>" + item["category"] + f"</h1> <img src='{item['url']}' style='width: 80%; height: auto; border: 3px solid " + color + ";'/></td>"

    # assert 1 == 2
    if str(outfit) in context.history_outfits:
        outfit_color = "red"
    else:
        outfit_color = "blue"

    html_str += f"""<h1 style="color:"""+ outfit_color + """; margin-left:160px;">Outfit Generator: '""" + str(outfit) +"""' Outfit Generated</h1>"""

    html_str += f"""<table>
              <tr>
              {recs_img}
              </tr>"""

    html_str += "</table>"
    html_str += '<br/><button type="button">GENERATE NEW OUTFIT</button>'
    html_str += '<br/><br/><button type="button">BUY OUTFIT</button>'
    file = open("features/" + scenario + ".html", "w")
    file.write(html_str)
    file.close()
