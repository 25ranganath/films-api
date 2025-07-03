from flask import Blueprint, request, jsonify
from db import get_db_connection

movies_bp = Blueprint('movies_bp', __name__)

# GET movies with pagination
@movies_bp.route('/api/movies', methods=['GET'])
def get_movies():
    start = int(request.args.get('start', 0))
    limit = int(request.args.get('limit', 10))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM movie LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, start))

    movies = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(movies)

# POST movie
@movies_bp.route('/api/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    required_fields = ['title', 'year', 'date_published', 'duration', 'country']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """INSERT INTO movie (title, year, date_published, duration, country, worlwide_gross_income, languages, production_company)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        data['title'],
        data['year'],
        data['date_published'],
        data['duration'],
        data['country'],
        data.get('worlwide_gross_income'),
        data.get('languages'),
        data.get('production_company')
    )

    cursor.execute(query, values)
    conn.commit()

    new_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({'message': 'Movie added successfully', 'id': new_id}), 201
