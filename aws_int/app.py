import dotenv
import os
import time
from src.treat import Treat
import boto3
import json

dotenv.load_dotenv()

sqs_client = boto3.client(
                'sqs', 
                region_name=os.getenv('AWS_REGION'),
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

s3_client = boto3.client(
                's3',
                region_name=os.getenv('AWS_REGION'),
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

if __name__ == "__main__":
    SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL')
    while True:
        print(f'Waiting for data on queue {SQS_QUEUE_URL.split("/")[-1]}...')
        # Escutar fila SQS
        r = sqs_client.receive_message(QueueUrl=SQS_QUEUE_URL, MaxNumberOfMessages=10)
        try:
            if r:
                for m in r.get("Messages", []):
                    m = json.loads(json.dumps(m))
                    # Processar mensagem
                    body = json.loads(m["Body"])
                    print(f'Processing data... {body.get("Message")}')
                    tr = Treat(json.loads(body.get("Message")))
                    tr.add_time()
                    # Enviar para S3
                    s3_client.put_object(
                        Bucket=os.getenv('S3_BUCKET_NAME_INPUT'), 
                        Key=f"entrada/{tr.data['id']}.json", 
                        Body=json.dumps(tr.data)
                    )
                    # Deletar mensagem da fila
                    sqs_client.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=m["ReceiptHandle"])
                    print(f'Mensagem {tr.data} processada e removida da fila.')
        except Exception as e:
            print(f'Erro ao processar mensagem: {e}')
        time.sleep(2)