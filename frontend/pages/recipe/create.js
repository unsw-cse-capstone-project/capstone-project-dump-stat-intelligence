import Head from "next/head";

import Hello from "../../components/Hello";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Pantry Pirate</title>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-6">
            <h1 className="title">/recipe/create</h1>
            <p>Probs good idea to read README.md</p>
            <Hello />
          </div>
        </div>
      </div>
    </div>
  );
}
