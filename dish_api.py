import flask
from flask import jsonify

from data import db_session
from data.dishes import Dish

blueprint = flask.Blueprint(
    'dishes_api',
    __name__,
    template_folder='templates'
)

db_session.global_init('db/Dbase.db')


@blueprint.route('/api/dishes/<int:schoolId>')
def get_dishes(schoolId):
    db_sess = db_session.create_session()
    a = []
    for i in db_sess.query(Dish).filter(Dish.schoolId == schoolId):
        a.append({"id": i.id,
                  "name": i.name,
                  "count": i.count,
                  "isHere": i.isHere
                  })
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/dishes/<int:schoolId>/now')
def get_now_dishes(schoolId):
    db_sess = db_session.create_session()
    a = []
    for i in db_sess.query(Dish).filter(Dish.schoolId == schoolId).filter(Dish.isHere):
        a.append({"id": i.id,
                  "name": i.name,
                  "count": i.count,
                  "isHere": i.isHere
                  })
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/dishes/<int:schoolId>/add/<string:nameDish>/<int:count>/<int:isHere>')
def add_dish(schoolId, nameDish, count, isHere):
    db_sess = db_session.create_session()
    dish = db_sess.query(Dish).filter(Dish.schoolId == schoolId).filter(Dish.name == nameDish).first()
    if not dish:
        dish = Dish(schoolId=schoolId,
                    name=nameDish,
                    count=count,
                    isHere=isHere)
        db_sess.add(dish)
        db_sess.commit()
    db_sess.close()
    return jsonify({
        "name": nameDish,
        "count": count,
        "isHere": isHere
    })


@blueprint.route('/api/dishes/<int:schoolId>/set/<string:nameDish>/<int:count>/<int:isHere>')
def set_dish(schoolId, nameDish, count, isHere):
    db_sess = db_session.create_session()
    dish = db_sess.query(Dish).filter(Dish.schoolId == schoolId).filter(Dish.name == nameDish).first()
    dish.count = count
    dish.isHere = isHere
    db_sess.commit()
    db_sess.close()
    return jsonify({
        "name": nameDish,
        "count": count,
        "isHere": isHere
    })


@blueprint.route('/api/dishes/<int:schoolId>/del/<string:nameDish>')
def del_dish(schoolId, nameDish):
    db_sess = db_session.create_session()
    dish = db_sess.query(Dish).filter(Dish.schoolId == schoolId).filter(Dish.name == nameDish).first()
    db_sess.delete(dish)
    db_sess.commit()
    db_sess.close()
    return "Delete"
