FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /bank
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN sh ops/scripts/install.sh


CMD exec python app.py < input.txt