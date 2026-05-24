FROM python:3.11-alpine
RUN apk --update add bash nano g++
WORKDIR /vampi
COPY . .
RUN pip install -r requirements.txt
# Thêm user không quyền root
RUN addgroup -S vampigroup && adduser -S vampiuser -G vampigroup
RUN chown -R vampiuser:vampigroup /vampi
USER vampiuser
ENTRYPOINT ["python"]
CMD ["app.py"]
