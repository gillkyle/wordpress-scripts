require("dotenv").config()
const { GraphQLClient } = require("graphql-request")
const getClient = require("./get-client")

// const client = new GraphQLClient(`${process.env.WORDPRESS_URL}/graphql`)

const importPosts = async () => {
  const client = await getClient().catch((err) => {
    console.warn(err)
  })

  const data = await client.request(
    `
    query AuthorQuery {
      users {
        nodes {
          id
          name
          nicename
          userId
        }
      }
    }
  
  `,
    {
      nicename: `Some name...`,
    }
  )

  console.log(data.users.nodes)
}

importPosts()
