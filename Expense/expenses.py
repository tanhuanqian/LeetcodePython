from flask import Blueprint, request, jsonify
from models import Expense
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date

expenses = Blueprint('expenses', __name__)

@expenses.route('/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_expense = Expense(
        user_id=user_id,
        amount=data['amount'],
        category=data['category'],
        date=data['date'],
        description=data.get('description', '')
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Expense added"}), 201

@expenses.route('/expenses/<int:id>', methods=['PUT'])
@jwt_required()
def update_expense(id):
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=id, user_id=user_id).first()
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    data = request.get_json()
    expense.amount = data.get('amount', expense.amount)
    expense.category = data.get('category', expense.category)
    expense.date = data.get('date', expense.date)
    expense.description = data.get('description', expense.description)
    db.session.commit()
    return jsonify({"message": "Expense updated"}), 200

@expenses.route('/expenses/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_expense(id):
    user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=id, user_id=user_id).first()
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted"}), 200

@expenses.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    user_id = get_jwt_identity()
    start_date = request.args.get('start_date', '2020-01-01')
    end_date = request.args.get('end_date', date.today())
    expenses = Expense.query.filter(Expense.user_id == user_id, Expense.date.between(start_date, end_date)).all()
    return jsonify([expense.to_dict() for expense in expenses]), 200
