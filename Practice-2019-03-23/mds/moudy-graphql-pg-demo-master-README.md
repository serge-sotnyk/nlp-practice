
## Install
```sh
git clone git@github.com:moudy/graphql-pg-demo.git
cd graphql-pg-demo
npm install
```

## Setup Postgres DB
```
# The name should match the path of DATABASE_URL in `.env`
createdb graphqldemo

npm run migrate
npm run seed
```

## Running app
```sh
npm run dev
open http://localhost:3021/graphql
```

### Notes
- [knex.js](http://knexjs.org/) is used to interact with Postgres
- [Dataloader](https://github.com/facebook/dataloader) is used in `app/services/store/sqlLoader.js` to batch SQL calls usinging `app/services/pg.js` (which is basically knex.js).
- [express-graphql](https://github.com/graphql/express-graphql) is used to create an Express GraphQL server
- There is no "Client app" but the data can be explored through [Graphiql](https://github.com/graphql/graphiql) at http://localhost:3021/graphql (try clicking around "Docs" in the upper right corner).
- the logged in user is hard-coded [here](https://github.com/moudy/graphql-pg-demo/blob/master/app/routers/graphql.js#L53)
- [Here is an example query](http://localhost:3021/graphql?query=query%20%7B%0A%20%20viewer%20%7B%0A%20%20%20%20posts%20%7B%0A%20%20%20%20%20%20edges%20%7B%0A%20%20%20%20%20%20%20%20node%20%7B%0A%20%20%20%20%20%20%20%20%20%20text%0A%20%20%20%20%20%20%20%20%20%20user%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20id%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D) that returns a list of posts with it's text and user.
- Here is an exmple of a mutation (the "(" in the url messes up the markdown parser)  
   `http://localhost:3021/graphql?query=mutation%20CreatePostQuery(%24input%3A%20createPostInput!)%20%7B%0A%20%20createPost(input%3A%20%24input)%20%7B%0A%20%20%20%20newPostEdge%20%7B%0A%20%20%20%20%20%20node%20%7B%0A%20%20%20%20%20%20%20%20text%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D&variables=%7B%0A%20%20%22input%22%3A%20%7B%0A%20%20%09%22text%22%3A%20%22New%20post!%22%2C%0A%20%20%20%20%22clientMutationId%22%3A%200%0A%09%7D%0A%7D`   
  You have click the run button for it to actually add post.



