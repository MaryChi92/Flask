from flask import render_template, Blueprint
from werkzeug.exceptions import NotFound

# from blog.models import Article

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: ['Top 3 Restaurants in Alanya', "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at magna lorem. Sed elementum tellus tortor, id tempus turpis malesuada ut. Ut fringilla tellus augue."],
    2: ['How I Spent My Holidays', "Suspendisse velit turpis, finibus sit amet accumsan et, rutrum vel neque."],
    3: ['Do U Like Veggies?', "Aliquam luctus semper mi non faucibus. Phasellus maximus in purus id porta. Phasellus ante felis, convallis eget ipsum tempus, finibus aliquam eros. Nam ipsum enim, egestas in ante quis, commodo laoreet purus. In nec malesuada sapien."],
}


@articles.route('/', endpoint='list')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@articles.route('/<int:article_id>', endpoint='details')
def article_details(article_id: int):
    try:
        article_name = ARTICLES[article_id][0]
        article_text = ARTICLES[article_id][1]
    except KeyError:
        raise NotFound(f"Article {article_id} doesn't exist!")
    return render_template('articles/details.html', article_id=article_id, article_name=article_name, article_text=article_text)
