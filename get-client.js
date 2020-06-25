require("dotenv").config()

const { GraphQLClient } = require("graphql-request")

const getClient = async () => {
  const tempClient = new GraphQLClient(`${process.env.WORDPRESS_URL}/graphql`)
  console.log(process.env.USER)
  const data = await tempClient.request(
    `
  mutation LoginUser($username: String!, $password: String!) {
    login(input: {clientMutationId: "uniqueId", username: $username, password: $password}) {
      authToken
      user {
        id
        name
      }
    }
  }
  
  `,
    {
      username: `kylegill`,
      password: process.env.PASSWORD,
    }
  )

  return new GraphQLClient(`${process.env.WORDPRESS_URL}/graphql`, {
    headers: {
      authorization: `Bearer ${data.login.authToken}`,
    },
  })
}

module.exports = getClient
