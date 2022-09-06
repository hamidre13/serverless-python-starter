def hello(event, context):
  print ("just got a request!")
  response = {
        "statusCode": 200,
        "body": 'body'
    }

  return response
