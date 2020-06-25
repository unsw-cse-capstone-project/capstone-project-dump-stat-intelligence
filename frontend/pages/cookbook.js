import Head from "next/head";

import Hello from "../components/Hello";

export default function Home() {
  return (
    <>
      <Head>
        <title>Pantry Pirate | Cookbook</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-6">
            <h1 className="title">/cookbook</h1>
            <p>Probs good idea to read README.md</p>
            <Hello/>
          </div>
        </div>
      </div>
    </>
  );
}
