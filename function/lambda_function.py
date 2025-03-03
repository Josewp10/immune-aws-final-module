import boto3
import os
from boto3.dynamodb.conditions import Key

DYNAMO_IMMUNE = os.environ['DYNAMO_IMMUNE']


class DynamoAccessor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self, dni):
        # Consultamos la tabla utilizando el dni como clave de partición
        response = self.table.query(KeyConditionExpression=Key('dni').eq(dni))
        return response["Items"][0] if any(response["Items"]) else None

    def save_data_to_dynamo(self, dni, data):
        # Guardamos un nuevo registro en la tabla DynamoDB
        # Suponemos que 'data' es un diccionario que contiene los atributos a guardar
        data['dni'] = dni  # Aseguramos que el dni sea parte del registro
        self.table.put_item(Item=data)
        return {"status": "success", "message": "Registro guardado exitosamente"}


def lambda_handler(event, context):
    dynamo_backend = DynamoAccessor(DYNAMO_IMMUNE)
    
    if 'dni' in event:  # Si solo estamos consultando un registro por dni
        db_element = dynamo_backend.get_data_from_dynamo(event['dni'])
        return db_element
    
    if 'dni' in event and 'data' in event:  # Si estamos guardando un nuevo registro
        result = dynamo_backend.save_data_to_dynamo(event['dni'], event['data'])
        return result
