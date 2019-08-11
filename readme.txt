When normal user opened home page
	1)When user lands on the home page based on cookie is retrieved from the browser and sent to server.
	2)When server reads the cookie it gets the user details and fetched recently viewed products and its rating retrieved from database
	  and sent to client browser.
	3)Results are displayed on the browser
	4)Fig:landing_user_architecture.png is the architecture diagram

When user tries to login to system
	1)When user tries to login to system.
	2)Server authenticates the user using the database values.
	3)once user is authenticated server fetches the products which are delivered to used by not rated by user.
	4)Server also fetches the top rated products from database.
	5)Step 3&4 results are sent to user.
	6)Results are displayed in browser asking user to rate unrated products.
	7)Fig:login_user_architecture.png is the architecture diagram

When user gives rating to a product
	1) When user rates a product, product details, rating details, user details are sent to server.
	2) Store the rating in database by the user 
	3) Calculate the average rating of the product with new value and store in another table.
	4) Excute the above two queries using the batch update.
	5) Send the response to the user.
	6) Fig:user_giving_rating_architecture.png is the architecture diagram
	
Database architecture:
	1) We have two databases one is primary and another is backup
	2) Backup is used when primary is down so system will be avaiable all the time
	3) There is replicator between primary and backup to replicate the database
	4) Fig: storage_arch.png is the architecture diagram 
	
Serever Database query execute interface architecture:
	1) During server startup we intialize both primary database and backup database connection pooling
	2) When we want to execute a query we get a connection from connection pool and use it.
	3) If pool is exhausted then we create a temporary connection and close once it is used.
	4) If connection from primary pool is not usable then we switch to backup pool. 