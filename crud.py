from typing import Optional, List, Dict, Any
from app.db import get_database
from bson import ObjectId


async def create_user(user: Dict[str, Any]) -> ObjectId:
    db = get_database()
    res = await db.users.insert_one(user)
    return res.inserted_id


async def get_user_by_id(user_id: str) -> Optional[Dict[str, Any]]:
    if not ObjectId.is_valid(user_id):
        return None
    db = get_database()
    doc = await db.users.find_one({"_id": ObjectId(user_id)})
    return doc


async def find_users(
    q: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    is_active: Optional[bool] = None,
    skip: int = 0,
    limit: int = 10,
    ) -> List[Dict[str, Any]]:
    db = get_database()
    query = {}
    if q:
        # busca simples em name (case-insensitive)
        query['name'] = {"$regex": q, "$options": 'i'}
    if min_age is not None or max_age is not None:
        age_query = {}
    if min_age is not None:
        age_query['$gte'] = min_age
    if max_age is not None:
        age_query['$lte'] = max_age
        query['age'] = age_query
    if is_active is not None:
        query['is_active'] = is_active


    cursor = db.users.find(query).sort('name', 1).skip(skip).limit(limit)
    return await cursor.to_list(length=limit)


async def update_user(user_id: str, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if not ObjectId.is_valid(user_id):
        return None
    db = get_database()
    res = await db.users.find_one_and_update(
    {"_id": ObjectId(user_id)},
    {"$set": payload},
    return_document=True,
    )
    return res


async def delete_user(user_id: str) -> bool:
    if not ObjectId.is_valid(user_id):
        return False
    db = get_database()
    res = await db.users.delete_one({"_id": ObjectId(user_id)})
    return res.deleted_count == 1