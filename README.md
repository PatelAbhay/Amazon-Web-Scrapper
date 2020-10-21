# AmazonWebScrapper

This is a console based webscrapper that you can use to track prices in Amazon.  
The user inputs the link of the product they wish to track and can have the 
application running in the background. Final version of the application will be 
able to track multiple links. Currently a single page scrapper is fully implemented
whereas the multiple page scrapper is in the works.

## To-Do List
* Make a GUI for better User Experience
* Create automated bot that will search for products given product name
    * Will search Amazon for the product inputted by User
    * Grabs the first 5 product links from the first few pages (User can choose how many pages to search) 
    * Product links are grabbed based on User preference
        * By Price
        * Shipping Cost/Prime Availability
        * Number of Stars
* Fix bug where the tracker fails to get product price on the third iteration (present only in master branch)

## License
[MIT](https://choosealicense.com/licenses/mit/)