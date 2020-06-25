require("dotenv").config()

const getClient = require("./get-client")
const query = `
  query {
    posts {
      nodes {
        id
        title
      }
    }
  }
`

async function upload({ type = "posts" } = {}) {
  const client = await getClient().catch((err) => {
    console.warn(err)
  })

  // const data = await client.request(query).catch((e) => {
  //   console.warn(e)
  // })
  console.log(data)
}

upload()
