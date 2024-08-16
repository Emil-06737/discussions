from db import db
from sqlalchemy.sql import text

def get_stats():
    sql = """SELECT da.id, da.topic, COUNT(DISTINCT dc.id), COUNT(m.id), MAX(m.sent_at)
             FROM discussion_areas da LEFT JOIN discussion_chains dc
             ON da.id = dc.discussion_area_id LEFT JOIN messages m ON dc.id = m.discussion_chain_id
             GROUP BY da.id ORDER BY da.id"""
    return db.session.execute(text(sql)).fetchall()

def add_discussion_area(topic, confidentiality):
    try:
        sql = """INSERT INTO discussion_areas (topic, confidential)
                 VALUES (:topic, :confidentiality)"""
        db.session.execute(text(sql), {"topic":topic, "confidentiality":confidentiality})
        db.session.commit()
        return True
    except:
        return False

def is_confidential(id):
    sql = "SELECT confidential FROM discussion_areas WHERE id = :id"
    return db.session.execute(text(sql), {"id":id}).fetchone()[0]

def get_users_of_confidential_area(id):
    sql = """SELECT user_id FROM users_of_confidential_discussion_areas
             WHERE discussion_area_id = :id"""
    list = db.session.execute(text(sql), {"id":id}).fetchall()
    return [row[0] for row in list]

def get_chains(id):
    sql = "SELECT id, header FROM discussion_chains WHERE discussion_area_id = :id ORDER BY id"
    return db.session.execute(text(sql), {"id":id}).fetchall()

def get_topic(id):
    sql = "SELECT topic FROM discussion_areas WHERE id = :id"
    return db.session.execute(text(sql), {"id":id}).fetchone()[0]