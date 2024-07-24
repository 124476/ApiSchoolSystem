import flask
from flask import jsonify

from data import db_session
from data.schools import School

blueprint = flask.Blueprint(
    'schools_api',
    __name__,
    template_folder='templates'
)

db_session.global_init('db/Dbase.db')


@blueprint.route('/api/schools')
def get_schools():
    db_sess = db_session.create_session()
    a = []
    for i in db_sess.query(School):
        a.append({"id": i.id,
                  "name": i.name
                  })
    db_sess.close()

    return jsonify(a)


@blueprint.route('/api/schools/add/<string:schoolName>')
def add_school(schoolName):
    db_sess = db_session.create_session()
    school = db_sess.query(School).filter(School.name == schoolName).first()
    if not school:
        school = School(name=schoolName)
        db_sess.add(school)
    db_sess.commit()

    schoolId = school.id
    db_sess.close()
    return jsonify({
        "id": schoolId,
        "name": schoolName
    })


@blueprint.route('/api/schools/set/<int:schoolId>/<string:schoolName>')
def set_school(schoolId, schoolName):
    db_sess = db_session.create_session()
    school = db_sess.query(School).filter(School.id == schoolId).first()
    if school:
        school.name = schoolName
    db_sess.commit()
    db_sess.close()

    return jsonify({
        "id": schoolId,
        "name": schoolName
    })


@blueprint.route('/api/schools/del/<int:schoolId>')
def del_school(schoolId):
    db_sess = db_session.create_session()
    school = db_sess.query(School).filter(School.id == schoolId).first()
    db_sess.delete(school)
    db_sess.commit()
    db_sess.close()
    return "Delete"
