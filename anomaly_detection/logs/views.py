# from django.http import JsonResponse
# from kafka import KafkaProducer
# import json

# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# def produce_log(request):
#     log = {"message": "Test log entry"}
#     producer.send('logs', log)
#     return JsonResponse({"status": "Log sent"})
