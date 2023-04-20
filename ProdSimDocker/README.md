# ProdSimDocker
This is the code that is used to build the docker image that is hosted under the Kyma cluster at the '...001' address (https://bcx-prod-sim-001.c-07113c9.kyma.ondemand.com) 
That endpoint is being called by my own version of the restapi widget:
 - It returns a string with: 
    1) the topn list of products, and 
    2) the x, y, z coords of the top 25 most similar products
