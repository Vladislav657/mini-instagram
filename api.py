from flask import Blueprint, jsonify, abort
from utils import get_posts_all, get_post_by_pk
import logging

api = Blueprint('api', __name__)

logger = logging.getLogger('api')
logger.setLevel(logging.INFO)
log = logging.FileHandler('api.log', encoding='utf-8')
log.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(log)


@api.route('/api/posts')
def get_posts():
    posts = get_posts_all()
    logger.info('Выполнен запрос /api/posts')
    return jsonify(posts)


@api.route('/api/posts/<int:s>')
def get_post_id(s):
    post = get_post_by_pk(s)
    if post == ValueError:
        logger.error(f'Данных по запросу /api/posts/{s} не существет')
        abort(404)
    logger.info(f'Запрос /api/posts/{s} выполнен успешно')
    return jsonify(post)
