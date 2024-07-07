FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

COPY lambda/ .

COPY docker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["lambda_function.lambda_handler"]
