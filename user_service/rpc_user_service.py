from modernrpc.core import rpc_method
from .models import UserModels
from datetime import datetime

# api gateway
@rpc_method
def create_user(user_data):
    try:
        check_user = UserModels.objects.filter(name=user_data['name'])
        if check_user.exists():
                data_response = {
                    "status": 403,
                    "message": f"user {check_user.name} already exist",
                }
                return data_response
        if user_data['type'] not in ['regular', 'VIP', 'wholesale']:
                data_response = {
                    "status": 403,
                    "message": f"type {check_user.name} not standart",
                }
                return data_response
        
        # add validation when name is already taken
        save_user = UserModels.objects.create(
            name=user_data['name'],
            user_type=user_data['type']
        )
        data_response = {
            "status": 201,
            "message": "create user is success",
            "data": {
                    "uuid": save_user.uuid, 
                    "name": save_user.name,
                    "type": save_user.user_type,
                        "created_at":save_user.created_at,
                        "updated_at":save_user.updated_at,
                        "deleted_at":None,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def find_all_user():
    try:
        all_user = UserModels.objects.all()
        data = []
        for user in all_user:
            user_data = {
                'uuid': user.uuid,
                'name': user.name,
                'user_type': user.user_type,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
            }
            data.append(user_data)
        data_response = {
            "status": 200,
            "message": "list user",
            "data": data
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def find_user_by_uuid(user_uuid):
    try:
        user_object = UserModels.objects.get(uuid=user_uuid)
        data_response = {
            "status": 200,
            "message": "user is exist",
            "data": {
                    "uuid": "uuid-number", 
                    "name": user_object.name,
                    "type": user_object.user_type,
                        "created_at":user_object.created_at,
                        "updated_at":user_object.updated_at,
                        "deleted_at":None,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def update_user_by_uuid(user_uuid, user_data):
    try:
        user_object = UserModels.objects.get(uuid=user_uuid)
        if user_data.get('name', None) is not None:
            user_object.name = user_data['name']
        if user_data.get('type', None) is not None:
            user_object.user_type = user_data['type']
        user_object.save()
        data_response = {
            "status": 200,
            "message": "user is updated",
            "data": {
                    "uuid": "uuid-number", 
                    "name": user_object.name,
                    "type": user_object.user_type,
                        "created_at":user_object.created_at,
                        "updated_at":user_object.updated_at,
                        "deleted_at":None,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def delete_user_by_uuid(user_uuid):
    try:
        user_object = UserModels.objects.get(uuid=user_uuid)
        user_object.delete()
        now = datetime.now()
        data_response = {
            "status": 200,
            "message": "user is deleted",
            "data": {
                    "uuid": "uuid-number", 
                    "name": user_object.name,
                    "type": user_object.user_type,
                        "created_at":user_object.created_at,
                        "updated_at":user_object.updated_at,
                        "deleted_at":now.strftime("%m/%d/%Y, %H:%M:%S"),
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response


# transaction service
@rpc_method
def filter_user_by_name(item_data):
    try:
        for user in item_data['transaction']:
            user_objects = UserModels.objects.filter(name=user['buyer'])
            if not user_objects.exists():
                data_response = {
                    "status": 404,
                    "message": f"user with name {user['buyer']} not exist",
                }
                return data_response
        data_response = {
            "status": 200,
            "message": "user is exist",
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def find_user_by_name(user_name):
    try:
        user_object = UserModels.objects.get(name=user_name)
        data_response = {
            "status": 200,
            "message": "user is exist",
            "data": {
                    "uuid": user_object.uuid, 
                    "name": user_object.name,
                    "type": user_object.user_type,
                        "created_at":user_object.created_at,
                        "updated_at":user_object.updated_at,
                        "deleted_at":None,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "user not is exist",
            "data": str(e)
        }
        return data_response