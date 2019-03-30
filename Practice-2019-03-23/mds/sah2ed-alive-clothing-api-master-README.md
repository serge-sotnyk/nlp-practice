# Aerohive Alive Clothing API
The app was developed on Windows 8.1 but should hopefully work on other platforms unchanged.

## 1.0. Prerequisities

- node v5.9.0
- npm 3.7.3
- swagger 2.0
- MongoDB 3.2.6


## 2.0. Database Setup
### 2.1. Local MongoDB Setup
```
# Create MongoDB data and log folders
mkdir D:\Apps\MongoDB\data
mkdir D:\Apps\MongoDB\log

# Create a MongoDB config file
cat > D:\Apps\MongoDB\mongod.cfg
dbpath=D:\Apps\MongoDB\data
logpath=D:\Apps\MongoDB\log\mongod.log

# Install MongoDB as a service
SET PATH=D:\Apps\MongoDB\Server\3.2\bin;%PATH%
mongod -f D:\Apps\MongoDB\mongod.cfg --install

# Start the MongoDB server
net start MongoDB
```


## 3.0. Application Setup
Navigate to the application folder on your machine.
```
cd aerohive/
```

### 3.1. Configuration Setup
Customize the app settings to match your environment.

#### 3.1.1. MongoDB
At a minimum, you will need to specify the MongoDB URI for the app to work.
```
vim config.js
```

Alternatively, you can set the MongoDB URI using environment variables.
- On Windows
`set MONGOLAB_URI=mongodb://<dbuser>:<dbpassword>@ds023902.mlab.com:23902/aliveclothing`

- On Linux
`MONGOLAB_URI=mongodb://<dbuser>:<dbpassword>@ds023902.mlab.com:23902/aliveclothing`

- On Heroku
`heroku config:set MONGOLAB_URI=mongodb://<dbuser>:<dbpassword>@ds023902.mlab.com:23902/aliveclothing`


#### 3.1.2. SSL/TLS
The self-signed SSL certificate included in the cert/ folder of the submission was generated with:
```
cd aerohive/cert
openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -keyout server.key -out server.crt
```


### 3.2. Test Data Setup
Insert some test data into the MongoDB server specified in your config file.
```
node test_files/drop.js
node test_files/testdata.js
```

This should insert 5 test staff accounts, 5 test customer accounts, 20 test products and 
a variety of orders for each customer containing random items. 

Of course, you can modify the number of inserted records by updating `config.js`.


### 3.3. View the Data
Using `mongo`, you can browse the test data that was inserted and use the fields to test out the endpoints.

```
// Select the app database
use AliveClothing
switched to db AliveClothing

// View the inserted documents
show collections
customers
devices
orderitems
orders
products
users

// View the inserted data
db.users.find()     // Equivalent to SELECT * FROM users;
db.customers.find()
db.devices.find()
db.orderitems.find()
db.orders.find()
db.products.find()
```

### 3.4. Run the Tests 
#### 3.4.1. Install Mocha
```
npm install -g mocha
```

#### 3.4.2. Run Mocha
```
mocha
```

### 3.5. Run the app
```
node app.js
```

### 3.6. Test the API using Swagger
Instead of writing lots of tests in Mocha which can go out of sync, I opted to use 
Swagger which offers an easy-to-use and graphical way of testing API endpoints.

You can run tests against the live API using the Swagger editor, simply launch it via:
```
swagger project edit
```
Then visit the URL printed to the console.


### 3.7. REST Endpoints
You should be able to test log-ins using the credentials `user1/user1` against the `/auth/login` endpoint.
These are the available endpoints:
```
/auth/login 
/auth/logout
/user
/user/{username}
/customer
/customer/{id}
/device
/store/surge
/store/presence
/swagger
```

### 3.8. Aerohive API
Since HiveManager (HM) needs to POST presence info to the webhook that we define, the webhook must be hosted at 
a publicly accessible address (i.e. https://localhost will not work). 

This is a screen shot of how the webhook was set up.
![screenshot](docs/alive-clothing.png)
Instructions on how to set up a presence webhook are provided in [docs/Aerohive_API_Webhook.md](docs/Aerohive_API_Webhook.md).

Therefore, to receive HM payloads, I've deployed it to Heroku. 

The app can be viewed at: https://alive-clothing.herokuapp.com/

(Note: Heroku forces free apps to sleep when the daily quota of 18h is exhausted.)




## 4.0. Development
### 4.1. Install Swagger globally
```
npm install -g swagger
```

### 4.2. Run the app in debug mode
```
# Enable debug output
set DEBUG=swagger-tools:middleware:*

# On Linux, omit the 'set' keyword 
# DEBUG=swagger-tools:middleware:*

# Launch the app
swagger project start aerohive
```

### 4.3. Aerohive API Testing
Use the script below to simulate the POSTing of presence data by HiveManager to the `/api/store/presence` REST endpoint.

```
cd aerohive/test_files
chmod +x ./post-presence.sh
./post-presence.sh
```
