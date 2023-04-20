FROM python:3.7-slim-buster
COPY models/prod2vec.100d.model models/prod2vec.100d.model
COPY prodsim_app.py prodsim_app.py
COPY products.csv products.csv 
RUN pip install flask
RUN pip install flask_restful
RUN pip install --upgrade gensim
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install numpy
EXPOSE 8888
CMD [ "python", "./prodsim_app.py"]