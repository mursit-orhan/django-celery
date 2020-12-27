One family of classes DRF has is Serializers. 
They're used to convert the data sent in a HTTP request to a 
Django object and a Django object to a valid response data.

We'll build an API for a Cafe:

    We'll need an endpoint that creates orders in the cafe;
    Orders have a table number and a list of meals;
    A meal has a title and a price
    a GET method for listing the orders and;
    a POST method to create a new order.
    In the GET requests, I want to receive a list of all the orders and, for each order, I want to see every meal requested;
    In the GET requests, I also want to have the total price of each order;
    In the POST requests, since meals are pre-registered in the system, I want to send only the meals ids instead of the whole meal object.

